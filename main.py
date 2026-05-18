import json
import os
import re
from html import escape

GAP_MARKUP = '<div class="md-source-gap" aria-hidden="true">&#8203;</div>'
LIST_ITEM_RE = re.compile(r"^[ ]{0,3}(?:[-+*] |\d+[.)] )")
FENCE_RE = re.compile(r"^[ ]{0,3}(?:```|~~~)")
TAB_HEADER_RE = re.compile(r'^[ ]{0,3}===\s+"')
HTML_TAG_RE = re.compile(r"^[ ]{0,3}</?([A-Za-z][\w:-]*)")
VOID_HTML_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


def _indent_width(line):
    expanded = line.expandtabs(4)
    return len(expanded) - len(expanded.lstrip(" "))


def _is_attribute_list(line):
    if not line:
        return False

    stripped = line.strip()
    if not (stripped.startswith("{") and stripped.endswith("}")):
        return False

    inner = stripped[1:-1].strip()
    if not inner:
        return False

    return any(
        token.startswith((".", "#")) or "=" in token
        for token in inner.split()
    )


def _is_list_item(line):
    return bool(LIST_ITEM_RE.match(line))


def _is_tab_header(line):
    return bool(TAB_HEADER_RE.match(line))


def _is_html_open_tag(line):
    stripped = line.strip()
    tag_name = _html_tag_name(stripped)
    return (
        stripped.startswith("<")
        and not stripped.startswith(("</", "<!", "<?"))
        and "</" not in stripped[1:]
        and stripped.endswith(">")
        and not stripped.endswith("/>")
        and tag_name not in VOID_HTML_TAGS
    )


def _is_html_close_tag(line):
    return line.strip().startswith("</")


def _html_tag_name(line):
    match = HTML_TAG_RE.match(line.strip())
    if not match:
        return None
    return match.group(1).lower()


def _normalize_dom_id(value, default="item"):
    text = re.sub(r"[^a-z0-9_-]+", "-", str(value).strip().lower()).strip("-")
    return text or default


def _find_anchor(lines, start, step):
    idx = start
    while 0 <= idx < len(lines):
        line = lines[idx]
        if line.strip() and _indent_width(line) <= 3:
            return line
        idx += step
    return None


def _find_nonblank_line(lines, start, step):
    idx = start
    while 0 <= idx < len(lines):
        line = lines[idx]
        if line.strip():
            return line
        idx += step
    return None


def _should_insert_gap(prev_anchor, next_anchor):
    if not prev_anchor or not next_anchor:
        return False

    if _is_attribute_list(prev_anchor) or _is_attribute_list(next_anchor):
        return False

    if _is_html_open_tag(prev_anchor) or _is_html_close_tag(next_anchor):
        return False

    if _is_tab_header(prev_anchor) and _is_tab_header(next_anchor):
        return False

    if _is_list_item(prev_anchor) and _is_list_item(next_anchor):
        if _indent_width(prev_anchor) == _indent_width(next_anchor):
            return False

    return True


def _insert_blankline_spacers(markdown_text):
    lines = markdown_text.splitlines()
    output = []
    idx = 0
    in_fence = False

    while idx < len(lines):
        line = lines[idx]
        if FENCE_RE.match(line):
            in_fence = not in_fence
            output.append(line)
            idx += 1
            continue

        if in_fence or line.strip():
            output.append(line)
            idx += 1
            continue

        blank_start = idx
        while idx < len(lines) and not lines[idx].strip():
            idx += 1
        blank_count = idx - blank_start

        prev_line = _find_nonblank_line(lines, blank_start - 1, -1)
        next_line = _find_nonblank_line(lines, idx, 1)
        if (
            prev_line
            and next_line
            and _indent_width(prev_line) > 3
            and _indent_width(next_line) > 3
        ):
            output.extend(lines[blank_start:idx])
            continue

        if _is_attribute_list(prev_line) or _is_attribute_list(next_line):
            output.extend(lines[blank_start:idx])
            continue

        prev_anchor = _find_anchor(lines, blank_start - 1, -1)
        next_anchor = _find_anchor(lines, idx, 1)

        if _should_insert_gap(prev_anchor, next_anchor):
            output.extend([GAP_MARKUP] * blank_count)
        else:
            output.extend(lines[blank_start:idx])

    trailing_newline = "\n" if markdown_text.endswith("\n") else ""
    return "\n".join(output) + trailing_newline


def on_page_markdown(markdown, **kwargs):
    return _insert_blankline_spacers(markdown)


def on_post_page_macros(env):
    env.markdown = _insert_blankline_spacers(env.markdown)

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """
    
    import json
    
    # Auto-generate docs/css/sado_colors.css from sado_colors.json
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, "sado_colors.json")
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                sado_colors = json.load(f)
            
            css_lines = ["/* 이 파일은 sado_colors.json의 설정을 바탕으로 자동 생성됩니다. 직접 수정하지 마세요. */"]
            for sado_id, styles in sado_colors.items():
                css_lines.append(f".tag-box[data-sado=\"{sado_id}\"] {{")
                if "bg" in styles:
                    css_lines.append(f"  background-color: {styles['bg']};")
                if "color" in styles:
                    css_lines.append(f"  color: {styles['color']};")
                css_lines.append("}\n")
            
            css_content = "\n".join(css_lines)
            css_path = os.path.join(base_dir, "docs", "css", "sado_colors.css")
            
            needs_write = True
            if os.path.exists(css_path):
                with open(css_path, "r", encoding="utf-8") as f:
                    if f.read() == css_content:
                        needs_write = False
            
            if needs_write:
                os.makedirs(os.path.dirname(css_path), exist_ok=True)
                with open(css_path, "w", encoding="utf-8") as f:
                    f.write(css_content)
    except Exception as e:
        print(f"Failed to generate sado_colors.css: {e}")

    def clean_rel_path(path):
        return str(path).lstrip('/').replace('\\', '/')

    def attr(value):
        return escape(str(value), quote=True)

    def indent_html(value, spaces=4):
        prefix = " " * spaces
        return prefix + str(value).replace("\n", "\n" + prefix)

    def figure_with_caption(content, caption, figure_attrs=""):
        return (
            f'<figure{figure_attrs} markdown="1">\n'
            f"{content}\n"
            '<figcaption markdown="1">\n'
            f"{caption}\n"
            "</figcaption>\n"
            "</figure>"
        )

    def wrap_figure_content(content):
        return f'<div class="figure-media">{content}</div>'

    def caption_needs_block_markdown(caption):
        text = str(caption).replace("\r\n", "\n").replace("\r", "\n")
        lines = text.split("\n")

        if any(_is_attribute_list(line) for line in lines):
            return True

        if any(_is_list_item(line) for line in lines):
            return True

        return "\n\n" in text

    def render_figure(content, caption, figure_attrs=""):
        wrapped_content = wrap_figure_content(content)

        if caption_needs_block_markdown(caption):
            return figure_with_caption(wrapped_content, caption, figure_attrs)

        return (
            f'<figure{figure_attrs} markdown="1">{wrapped_content}'
            f'<figcaption markdown="1">{multiline(caption)}</figcaption>'
            "</figure>"
        )

    def caption_alt_text(caption, default="Image"):
        if not caption:
            return default

        text = str(caption).replace("\r\n", "\n").replace("\r", "\n")
        for line in text.split("\n"):
            stripped = line.strip()
            if stripped:
                return stripped
        return default

    def markdown_link_href(link):
        text = str(link)
        path, sep, fragment = text.partition("#")
        if ".md" not in path:
            return text

        use_dir_urls = env.conf.get("use_directory_urls", True)
        if use_dir_urls:
            path = path.replace(".md", "/")
        else:
            path = path.replace(".md", ".html")
        return f"{path}{sep}{fragment}" if sep else path

    def multiline(value):
        if isinstance(value, (list, tuple)):
            return "<br>".join(str(item) for item in value)
        text = str(value).replace("\r\n", "\n").replace("\r", "\n")
        lines = text.split("\n")
        rendered = lines[0] if lines else ""

        for line in lines[1:]:
            if rendered.rstrip().endswith(("<br>", "<br/>", "<br />")):
                rendered += line.lstrip()
            else:
                rendered += "<br>" + line

        return rendered

    def tab_block(items):
        return "\n\n".join(
            f'=== "{title}"\n{indent_html(content)}'
            for title, content in items
        )

    def get_doc_path(path):
        clean_path = clean_rel_path(path)
        if hasattr(env, 'resolve_doc_path'):
            return env.resolve_doc_path(clean_path)

        src_path = env.page.file.src_path.replace('\\', '/')
        dir_name = os.path.dirname(src_path)
        levels = len(dir_name.split('/')) if dir_name else 0
        prefix = "../" * levels
        return f"{prefix}{clean_path}"

    @env.macro
    def get_asset_path(path):
        path = clean_rel_path(path)
        if hasattr(env, 'resolve_asset_path'):
            return env.resolve_asset_path(path)

        # Calculate depth based on the directory of the source file
        src_path = env.page.file.src_path.replace('\\', '/')
        dir_name = os.path.dirname(src_path)
        # If dir_name is empty, we are at the root
        levels = len(dir_name.split('/')) if dir_name else 0
        prefix = "../" * levels
        return f"{prefix}assets/{path}"

    @env.macro
    def stat_pill(icon_name, text, value):
        icon_path = get_asset_path(f"CharacterInfo/stats/Icon_{icon_name}.png")
        return f"""<div class="stat-pill"><div class="pill-left"><span class="icon-circle"><img src="{icon_path}" width="20"></span><span class="pill-text">{text}</span></div><div class="stat-num">{value}</div></div>"""

    @env.macro
    def pref_icon(frame_color, food_id):
        frame_path = get_asset_path(f"common/itemslot/ItemSlot_{frame_color}.png")
        food_path = get_asset_path(f"common/food/Icon_Food_{food_id}.png")
        return f"""<div class="pref-icon">
  <img class="frame" src="{frame_path}" alt="frame">
  <img class="overlay" src="{food_path}" alt="food">
</div>"""

    @env.macro
    def pref_row_header(icon_type, text):
        icon_path = get_asset_path(f"common/food/{icon_type}.png")
        return f"""<td class="pref-icon-cell"><div class="pref-icon-mini"><img src="{icon_path}" alt="icon"></div><span>{text}</span></td>"""

    @env.macro
    def preference_table(rows, item_header="음식"):
        def cell_content(items):
            if isinstance(items, str):
                return items
            return "\n".join(pref_icon(frame_color, food_id) for frame_color, food_id in items)

        body = "\n".join(
            f"""      <tr>
        {pref_row_header(icon_type, label)}
        <td>
{indent_html(cell_content(items), 10)}
        </td>
      </tr>"""
            for icon_type, label, items in rows
        )
        return f"""<div class="prefs-table-wrap">
  <table class="prefs-table">
    <thead>
      <tr>
        <th>선호도</th>
        <th>
          <div class="th-cell">
            <span>{item_header}</span>
          </div>
        </th>
      </tr>
    </thead>
    <tbody>
{body}
    </tbody>
  </table>
</div>"""

    @env.macro
    def preference_value_table(headers, rows):
        header_html = "\n".join(
            f"""        <th>
          <div class="th-cell">
            <img class="th-badge" src="{get_asset_path(image_path)}" alt="badge">
            <span>{label}</span>
          </div>
        </th>"""
            for image_path, label in headers
        )
        body = "\n".join(
            f"""      <tr>
        {pref_row_header(icon_type, label)}
        {"".join(f"<td>{value}</td>" for value in values)}
      </tr>"""
            for icon_type, label, values in rows
        )
        return f"""<div class="prefs-table-wrap intimacy-prefs">
  <table class="prefs-table">
    <thead>
      <tr>
        <th>선호도</th>
{header_html}
      </tr>
    </thead>
    <tbody>
{body}
    </tbody>
  </table>
</div>"""

    @env.macro
    def adv_skill(icon_id, label, is_main=False):
        icon_path = get_asset_path(f"CharacterInfo/alba/LifeSkill{icon_id}.png")
        badge_html = '\n  <div class="rel-badge">메인</div>' if is_main else ''
        main_class = ' rel-main' if is_main else ''
        return f"""<div class="rel-card{main_class}">
  <div class="rel-icon"><img src="{icon_path}" alt="icon"></div>
  <div class="rel-label">{label}</div>{badge_html}
</div>"""

    @env.macro
    def rank_row(rank_level, stats_html):
        return f"""<div class="rank-row">
  <div class="rank-label">RANK {rank_level}</div>
  <div class="rank-content">
    {stats_html}
  </div>
</div>"""

    @env.macro
    def stat_row(icon_name, text, value):
        icon_path = get_asset_path(f"CharacterInfo/stats/Icon_{icon_name}.png")
        return f"""<div class="stat-row"><span class="icon-circle"><img src="{icon_path}" width="20"></span><span class="stat-text">{text}</span><span class="stat-num">{value}</span></div>"""
        
    @env.macro
    def intimacy_row(level, text, rowspan=1):
        rowspan_attr = f' rowspan="{rowspan}"' if rowspan > 1 else ''
        return f"""<tr>
  <td{rowspan_attr}>Lv.{level}</td>
  <td>{text}</td>
</tr>"""

    @env.macro
    def present_card(title, description, image_path, letter_path="letter.png", image_alt="item image", voices=None):
        voice_html = ""
        if voices:
            voice_items = []
            for voice in voices:
                label, audio = voice if isinstance(voice, (list, tuple)) else ("재생", voice)
                audio_url = get_asset_path(f"audio/{audio}")
                voice_items.append(
                    '<span class="vk-letter-voice-item">'
                    f'<span>{attr(label)}</span>'
                    f'<button class="voice-btn" data-src="{attr(audio_url)}"'
                    f' aria-label="{attr(f"{label} 음성 재생")}"'
                    f' title="{attr(f"{label} 음성 재생")}" type="button">&#9654;</button>'
                    "</span>"
                )
            voice_html = (
                '      <div class="vk-letter-voice">\n'
                "        <span>편지 음성</span>\n"
                f'        <div class="voice-btn-group">{"".join(voice_items)}</div>\n'
                "      </div>\n"
            )
        return f"""<div class="vk-card-outer">
  <div class="vk-card">
    <div class="vk-card__left">
      <img class="vk-card__img-placeholder" src="{get_asset_path(image_path)}" alt="{attr(image_alt)}">
    </div>
    <div class="vk-card__right">
      <h3 class="vk-title">{title}</h3>
      <p class="vk-sub vk-small">{multiline(description)}</p>
    </div>
    <div class="vk-letter">
{voice_html}\
      <img src="{get_asset_path(letter_path)}" alt="">
    </div>
  </div>
</div>"""

    @env.macro
    def intimacy_table(title, rows, notes=None):
        note_html = ""
        if notes:
            note_html = "".join(f'<span> - {note}</span><br>' for note in notes)

        def render_text_cell(item):
            if _is_audio_pair(item):
                text = item[0]
                audios = item[1] if isinstance(item[1], (list, tuple)) else item[1:]
                
                buttons_html = ""
                for audio in audios:
                    audio_url = get_asset_path(f"audio/{audio}")
                    buttons_html += (
                        f'<button class="voice-btn" data-src="{attr(audio_url)}"'
                        f' aria-label="재생" type="button">&#9654;</button>'
                    )
                return f'<div class="voice-row"><span>{text}</span><div class="voice-btn-group">{buttons_html}</div></div>'
            return str(item)

        def _is_audio_pair(item):
            """Check if item is a (text, audio_path) pair or (text, audio1, audio2)."""
            if not isinstance(item, (list, tuple)) or len(item) < 2:
                return False
            if not isinstance(item[0], str):
                return False
            
            # Case 1: item[1] is a list of audio strings
            if isinstance(item[1], (list, tuple)):
                return all(isinstance(x, str) and x.endswith(('.mp3', '.wav', '.ogg')) for x in item[1])
            
            # Case 2: item[1:] are all audio strings
            return all(isinstance(x, str) and x.endswith(('.mp3', '.wav', '.ogg')) for x in item[1:])

        body_rows = []
        for row in rows:
            label = row[0]
            if len(row) > 2 and all(isinstance(x, str) and x.endswith(('.mp3', '.wav', '.ogg')) for x in row[2:]):
                values = [row[1:]]
            else:
                text = row[1]
                if _is_audio_pair(text):
                    values = [text]
                elif isinstance(text, (list, tuple)):
                    values = list(text)
                else:
                    values = [text]
            rowspan_attr = f' rowspan="{len(values)}"' if len(values) > 1 else ""
            body_rows.append(
                f'<tr><td class="intimacy-level"{rowspan_attr}>{label}</td>'
                f'<td class="intimacy-text">{render_text_cell(values[0])}</td></tr>'
            )
            for value in values[1:]:
                body_rows.append(f'<tr><td class="intimacy-text">{render_text_cell(value)}</td></tr>')

        body = "".join(body_rows)
        return (
            '<div class="intimacy-wrap">'
            f'<h3 class="intimacy-title">{title}</h3>'
            f"{note_html}"
            '<div class="intimacy-table-wrap">'
            '<table class="intimacy-table">'
            "<tbody>"
            f"{body}"
            "</tbody>"
            "</table>"
            "</div>"
            "</div>"
        )

    @env.macro
    def intimacy_tabs(entries):
        tab_items = []
        for entry in entries:
            tab_title = entry[0]
            table_title = entry[1]
            rows = entry[2]
            notes = entry[3] if len(entry) > 3 else None
            tab_items.append((tab_title, intimacy_table(table_title, rows, notes)))
        return tabs(tab_items)

    @env.macro
    def character_stat_card(avatar_path, icons, labels, stats, title="기본정보 (Lv 100 기준)"):
        icon_html = "\n".join(
            f'        <div class="icon-pill"><img src="{get_asset_path(path)}" alt="{attr(label)}"></div>'
            for path, label in zip(icons, labels)
        )
        label_html = "\n".join(f'        <span class="pill">{label}</span>' for label in labels)
        stat_html = "\n".join(
            f"""        <div class="stat-row">
          <div class="stat-key"><img src="{get_asset_path(f"CharacterInfo/stats/Icon_{icon}.png")}" width="25" alt=""> {name}</div>
          <div class="stat-value">{value}</div>
        </div>"""
            for icon, name, value in stats
        )
        return f"""<div class="stat-card">
  <header class="stat-header">
    <div class="stat-avatar-wrap">
      <img class="stat-avatar" src="{get_asset_path(avatar_path)}" alt="avatar">
    </div>
    <div class="stat-meta">
      <div class="stat-icons">
{icon_html}
      </div>
      <div class="stat-pills">
{label_html}
      </div>
    </div>
  </header>
  <section class="stat-body">
    <h4 class="stat-section-title">{title}</h4>
    <div class="stat-table">
{stat_html}
    </div>
  </section>
</div>"""

    def battle_skill_header(icon_path, title, subtitle="", alt=""):
        title_class = "lore-title" if subtitle else "lore-title lore-title--flush"
        subtitle_html = (
            f'\n        <div class="lore-subtitle">{subtitle}</div>'
            if subtitle else ""
        )
        return (
            '    <div class="lore-header">\n'
            f'      <img src="{get_asset_path(icon_path)}" alt="{attr(alt or title)}" class="lore-avatar">\n'
            "      <div>"
            f"{subtitle_html}\n"
            f'        <div class="{title_class}">{title}</div>\n'
            "      </div>\n"
            "    </div>"
        )

    @env.macro
    def battle_skill_tabs(items, width=500, height=300, autoplay=True, loop=True):
        tab_items = []
        for item in items:
            title, path = item[:2]
            caption = item[2] if len(item) > 2 else f"{title} 모습"
            item_width = item[3] if len(item) > 3 else width
            item_height = item[4] if len(item) > 4 else height
            tab_items.append(
                (
                    title,
                    video(
                        path,
                        caption=caption,
                        width=item_width,
                        height=item_height,
                        autoplay=autoplay,
                        loop=loop,
                    ),
                )
            )
        return tabs(tab_items)

    @env.macro
    def battle_skill_inline_stat(label, values, suffix="%"):
        return {
            "type": "inline_dynamic",
            "label": label,
            "values": list(values),
            "suffix": suffix,
        }

    @env.macro
    def battle_skill_dynamic_stat(label, values, suffix="%", extras=None):
        return {
            "type": "dynamic",
            "label": label,
            "values": list(values),
            "suffix": suffix,
            "extras": list(extras or []),
        }

    @env.macro
    def battle_skill_text_stat(label, text):
        return {
            "type": "text",
            "label": label,
            "text": text,
        }

    @env.macro
    def battle_skill_slider_card(
        key,
        icon_path,
        title,
        description,
        stats,
        subtitle="",
        alt="",
        summary="",
        level_min=1,
        initial_level=None,
    ):
        dom_id = _normalize_dom_id(key, "battle-skill")
        stats = list(stats)
        dynamic_stats = [stat for stat in stats if stat.get("type") == "dynamic"]
        if not dynamic_stats:
            raise ValueError(f"battle_skill_slider_card({key!r}) requires at least one dynamic stat")

        values = list(dynamic_stats[0]["values"])
        if not values:
            raise ValueError(f"battle_skill_slider_card({key!r}) requires at least one stat value")

        level_min = int(level_min)
        level_max = level_min + len(values) - 1
        initial_level = level_min if initial_level is None else int(initial_level)
        if not level_min <= initial_level <= level_max:
            raise ValueError(
                f"battle_skill_slider_card({key!r}) initial_level must be between {level_min} and {level_max}"
            )

        initial_index = initial_level - level_min
        series_map = {}
        stat_rows = []

        for stat_index, stat in enumerate(stats):
            stat_type = stat.get("type")
            if stat_type == "text":
                label_prefix = f'{stat["label"]}: ' if stat.get("label") else ""
                stat_rows.append(
                    f'    <div class="lore-stat-row">{label_prefix}{multiline(stat["text"])}</div>'
                )
                continue

            if stat_type != "dynamic":
                raise ValueError(f"battle_skill_slider_card({key!r}) received unsupported stat type {stat_type!r}")

            stat_values = list(stat["values"])
            if len(stat_values) != len(values):
                raise ValueError(
                    f"battle_skill_slider_card({key!r}) stat {stat.get('label', stat_index)!r} length must match level count"
                )

            value_id = f"{dom_id}-stat-{stat_index}"
            series_map[value_id] = stat_values
            inline_html = ""

            for extra_index, extra in enumerate(stat.get("extras", [])):
                extra_values = list(extra["values"])
                if len(extra_values) != len(values):
                    raise ValueError(
                        f"battle_skill_slider_card({key!r}) inline stat {extra.get('label', extra_index)!r} length must match level count"
                    )

                extra_id = f"{dom_id}-stat-{stat_index}-extra-{extra_index}"
                extra_label = f'{extra["label"]}:' if extra.get("label") else ""
                series_map[extra_id] = extra_values
                inline_html += (
                    f' ({extra_label}<span class="lore-number-highlight" id="{extra_id}">{extra_values[initial_index]}</span>{extra.get("suffix", "%")})'
                )

            stat_rows.append(
                f'    <div class="lore-stat-row">{stat["label"]}: '
                f'<span class="lore-number-highlight" id="{value_id}">{stat_values[initial_index]}</span>{stat.get("suffix", "%")}'
                f"{inline_html}</div>"
            )

        slider_attrs = [
            f'id="{dom_id}-slider"',
            'type="range"',
            f'min="{level_min}"',
            f'max="{level_max}"',
            f'value="{initial_level}"',
            'data-lore-slider="1"',
            f'data-level-target="{dom_id}-level"',
            f"data-lore-series='{attr(json.dumps(series_map, ensure_ascii=False, separators=(',', ':')))}'",
        ]
        summary_html = f'    <div class="lore-stat-row">{multiline(summary)}</div>\n' if summary else ""
        stat_html = "\n".join(stat_rows)

        return (
            '  <article class="lore-card">\n'
            f"{battle_skill_header(icon_path, title, subtitle=subtitle, alt=alt)}\n"
            '    <div class="lore-slider-wrapper">\n'
            f'      <div id="{dom_id}-level" class="lore-level-box lore-lvl">Lv.{initial_level}</div>\n'
            f'      <input {" ".join(slider_attrs)}>\n'
            "    </div>\n"
            f"{summary_html}"
            f'    <p class="lore-desc">{multiline(description)}</p>\n'
            f"{stat_html}\n"
            "  </article>"
        )

    @env.macro
    def battle_skill_static_card(icon_path, title, sections, subtitle="", alt=""):
        section_html = "\n".join(
            (
                '    <div class="battle-pill-group">\n'
                f'      <div class="battle-pill battle-pill--basic">{badge}</div>\n'
                "    </div>\n"
                f'    <p class="lore-desc">{multiline(description)}</p>\n'
                f'    <div class="lore-stat-row">{multiline(stats)}</div>'
            )
            for badge, description, stats in sections
        )
        return (
            '  <article class="lore-card">\n'
            f"{battle_skill_header(icon_path, title, subtitle=subtitle, alt=alt)}\n"
            f"{section_html}\n"
            "  </article>"
        )

    @env.macro
    def battle_skill_grid(cards):
        cards_html = "\n".join(str(card) for card in cards if card)
        return f"""<div class="lore-grid">
{cards_html}
</div>"""

    @env.macro
    def aside_panel(title, description, image_path, skills):
        def skill_html(skill):
            icon_path, star_path, name, desc, stats = skill[:5]
            stat_lines = "<br>\n".join(
                f'        {label}: <span class="skill-percent">{value}</span>{suffix}'
                for label, value, suffix in stats
            )
            return f"""    <div class="skill-card">
      <img class="icon" src="{get_asset_path(icon_path)}" alt="">
      <div class="meta">
        <div class="skill-head">
      <img class="badge-stars" src="{get_asset_path(star_path)}" alt="">
          <div class="skill-name">{name}</div>
        </div>
        <div class="skill-desc">
        {multiline(desc)}
        </div>
        <div class="skill-stats">
{stat_lines}
        </div>
      </div>
    </div>"""

        skills_html = "\n".join(skill_html(skill) for skill in skills)
        return f"""<div class="battle-panel">
  <div class="battle-header">
    <img class="battle-header-img" src="{get_asset_path(image_path)}" alt="portrait">
    <div class="battle-header-copy">
      <h2 class="battle-title">{title}</h2>
      <p class="battle-copy">{multiline(description)}</p>
    </div>
  </div>

  <div class="skill-list">
{skills_html}
  </div>
</div>"""

    @env.macro
    def profile_book(
        subtitle,
        name,
        headline,
        description,
        tmi,
        boxes,
        portrait_container_id="player-container",
        portrait_skel="spine/standing/Ashur.skel",
        portrait_atlas="spine/standing/Ashur.atlas",
        mini_avatar="Minimi.png",
    ):
        box_html = "\n".join(
            f"""      <div class="rk-box">
        <div class="rk-box-head">{head}</div>
        <div class="rk-box-body">{body}</div>
      </div>"""
            for head, body in boxes
        )
        portrait = spine_viewer(
            portrait_container_id,
            portrait_skel,
            portrait_atlas,
            width="100%",
            height="100%",
            background="#00000000",
            alpha=True,
            animation="Idle_1",
        )
        return f"""<div class="rk-book">
  <aside class="rk-left">
    <div class="rk-frame">
      <div class="rk-left-head">
        <div class="rk-left-sub">{subtitle}</div>
        <div class="rk-left-name">{name}</div>
      </div>
      <div class="rk-portrait-wrap">
        {portrait}
      </div>
    </div>
  </aside>
  <section class="rk-right">
    <div class="rk-right-title">
        <div>
        <div class="rk-head-large">{headline}</div>
        <div class="rk-head-line" aria-hidden="true"></div>
        <div class="rk-desc">{multiline(description)}</div>
      </div>
    </div>
    <div class="rk-tmi-row">
      <div class="rk-tmi-pill">TMI</div>
      <div class="rk-tmi-sep" aria-hidden="true"></div>
      <div class="rk-tmi-right">
        <div class="rk-mini-avatar" title="{attr(name)}">
          <img class="rk-mini-avatar-img" src="{get_asset_path(mini_avatar)}" alt="{attr(name)}">
        </div>
        <span class="rk-tmi-text">{multiline(tmi)}</span>
      </div>
    </div>
    <div class="rk-grid">
{box_html}
    </div>
  </section>
</div>"""

    @env.macro
    def record_cards(title, entries):
        cards = "\n".join(
            f"""      <article class="kj-card" role="listitem">
        <div class="kj-card-inner">
          <h4 class="kj-level">{level}</h4>
          <div class="kj-text">{multiline(text)}</div>
        </div>
      </article>"""
            for level, text in entries
        )
        return f"""<div class="kj-record-wrap">
  <div class="kj-record">
    <div class="kj-title">{title}</div>
    <div class="kj-cards" role="list">
{cards}
    </div>
  </div>
</div>"""

    def relationship_table(rows):
        def icon_html(icon):
            size, title, image = icon[:3]
            icon_path = get_asset_path(f"sadoicon/Icon_GraduateSkill_{image}.png")
            return (
                f'<div class="pref-icon pref-circle-{size}" title="{attr(title)}">'
                f'<img class="frame circle" src="{icon_path}" alt="food">'
                "</div>"
            )

        def row_html(row):
            label, icons = row
            icon_block = "".join(icon_html(icon) for icon in icons)
            return (
                f'<tr><td class="pref-icon-cell"><span>{label}</span></td>'
                f"<td>{icon_block}</td></tr>"
            )

        body = "".join(row_html(row) for row in rows)
        return (
            '<div class="prefs-table-alt-wrap pref-size-md">'
            '<table class="prefs-table-alt">'
            "<thead><tr>"
            "<th>거리</th>"
            '<th><div class="th-cell"><span>사도</span></div></th>'
            "</tr></thead>"
            f"<tbody>{body}</tbody>"
            "</table>"
            "</div>"
        )

    @env.macro
    def relationship_tabs(periods):
        return tabs((title, relationship_table(rows)) for title, rows in periods)

    @env.macro
    def rp_note_panel(columns):
        def item_icon(frame_color, food_id, overlay_indent):
            frame_path = get_asset_path(f"common/itemslot/ItemSlot_{frame_color}.png")
            food_path = get_asset_path(f"common/food/Icon_Food_{food_id}.png")
            return (
                f'<div class="pref-icon"><img class="frame" src="{frame_path}" alt="frame">\n'
                f'{overlay_indent}<img class="overlay" src="{food_path}" alt="food"></div>'
            )

        def emote_icon(icon_type):
            return f'<img src="{get_asset_path(f"common/food/{icon_type}.png")}" alt="emote">'

        def mini_html(mini):
            if not mini:
                return ""

            frame_color, food_id, emote_type, label = mini
            frame_path = get_asset_path(f"common/itemslot/ItemSlot_{frame_color}.png")
            food_path = get_asset_path(f"common/food/Icon_Food_{food_id}.png")
            return f"""
            <div class="rp-mini">
              <div class="rp-mini-icon">
                <div class="pref-mini-icon">
                  <img class="frame" src="{frame_path}" alt="frame">
                  <img class="overlay" src="{food_path}" alt="food">
                </div>
                <div class="rp-mini-emote">{emote_icon(emote_type)}</div>
              </div>
              <div class="rp-mini-label">{label}</div>
            </div>"""

        def row_html(item):
            frame_color, food_id, emote_type, title, desc, mini, overlay_indent = item
            return f"""        <div class="rp-row">
          {item_icon(frame_color, food_id, overlay_indent)}
          <div class="rp-emote">{emote_icon(emote_type)}</div>
          <div class="rp-body">
            <div class="rp-item-title">{title}</div>
            <div class="rp-item-desc">{desc}</div>{mini_html(mini)}
          </div>
        </div>"""

        column_html = "\n".join(
            "      <div class=\"rp-list\">\n"
            + "\n".join(row_html(item) for item in column)
            + "\n      </div>"
            for column in columns
        )
        return f"""<!-- New rp-* relationship panel (independent styles) -->
<div class="rp-panel">
  <div class="rp-inner">
    <div class="rp-columns">
{column_html}
    </div>
  </div>
</div>"""

    # --- Story Macros ---
    @env.macro
    def speech(char_id, name, text):
        return (
            '<div class="speech-line" markdown="span">'
            f':sadoicon-{char_id}:{{:.big-emoji}}<span class="tag-box" data-sado="{char_id}">{name}</span><br>'
            f'<div class="speech-bubble">{multiline(text)}</div>'
            "</div>"
        )

    @env.macro
    def mind_speech(text):
        return f"""<div class="speech-line"><div class="mind-bubble">{multiline(text)}</div></div>"""

    @env.macro
    def narrate(text):
        return f"""<div class="speech-line"><div class="narrate-text">{multiline(text)}</div></div>"""

    @env.macro
    def char_tag(char_id, name):
        return f"""<span class="tag-box" data-sado="{char_id}">{name}</span>"""

    @env.macro
    def speaker(char_id, name):
        return f""":sadoicon-{char_id}:{{:.big-emoji}} <span class="tag-box" data-sado="{char_id}">{name}</span><br>"""

    @env.macro
    def story_badge(icon, text):
        return f"""<span class="badge badge-version"><span class="badge-icon">:material-{icon}:</span>{text}</span>"""

    @env.macro
    def section_flag(flag_id):
        return f'<span id="{attr(flag_id)}"></span>'

    @env.macro
    def redirect_to(target):
        href = markdown_link_href(target)
        return (
            "<script>\n"
            f"window.location.replace(new URL({json.dumps(href, ensure_ascii=False)}, window.location.href));\n"
            "</script>"
        )

    @env.macro
    def tabs(items):
        return f"{tab_block(items)}\n<!-- md-tab-group -->"

    # --- Media Macros ---
    @env.macro
    def youtube(video_id, caption="", width=600, height=None):
        style = ["margin-left: auto;", "margin-right: auto;", "width: 100%;"]
        if width:
            style.append(f"max-width: {width if str(width).endswith(('px', '%')) else str(width) + 'px'};")
        if height:
            style.append(f"max-height: {height if str(height).endswith(('px', '%')) else str(height) + 'px'};")
        
        style_attr = f' style="{" ".join(style)}"' if style else ''
        iframe = f'<iframe class="video" src="https://www.youtube.com/embed/{video_id}" allowfullscreen></iframe>'
        
        if caption:
            return render_figure(f'<div class="video-wrapper">{iframe}</div>', caption, style_attr)
        else:
            return f"""<div class="video-wrapper"{style_attr}>{iframe}</div>"""

    @env.macro
    def story_card(title, img_path, link, freq=None, state=None):
        """Creates a stylized card for story chapters."""
        img_url = get_asset_path(img_path)

        if '.md' in link:
            use_dir_urls = env.conf.get('use_directory_urls', True)
            if use_dir_urls:
                link = link.replace('.md', '/')
            else:
                link = link.replace('.md', '.html')

        freq_badge = ""
        if freq:
            freq_badge = f'<div class="story-card-freq" data-freq="{attr(freq)}">{attr(freq)}</div>'

        state_class = ""
        state_badge = ""
        tag_name = "a"
        href_attr = f'href="{link}"'
        
        if state == "작업 중":
            state_class = " story-card--working"
            state_badge = f'<div class="story-card-state">🛠️ 작업 중</div>'
        elif state == "추가 예정":
            state_class = " story-card--todo"
            state_badge = f'<div class="story-card-state">⏳ 추가 예정</div>'
            tag_name = "div"
            href_attr = ""

        return (
            f'<{tag_name} {href_attr} class="story-card{state_class}">'
            f'<div class="story-card-img-wrap">'
            f'<div class="story-card-img" style="background-image: url(\'{img_url}\');"></div>'
            f'{state_badge}'
            f'{freq_badge}'
            f'</div>'
            f'<div class="story-card-title">{attr(title)}</div>'
            f'</{tag_name}>'
        )

    @env.macro
    def card_grid(content):
        """Wraps cards in a grid container."""
        return f'<div class="card-grid">{content}</div>'


    @env.macro
    def timeline(items):
        cards = []
        for item in items:
            title = item["title"]
            bg_url = get_asset_path(item["bg"])
            primary_href = markdown_link_href(item["href"])
            link_tags = "".join(
                f'<a href="{markdown_link_href(link)}">{attr(label)}</a>'
                for label, link in item.get("links", [])
            )
            cards.append(
                f'<div class="timeline-item" data-href="{primary_href}">'
                f'<div class="timeline-bg" style="background-image: url(\'{bg_url}\');"></div>'
                f'<div class="timeline-overlay"></div>'
                f'<div class="timeline-content">'
                f'<div class="timeline-title">{attr(title)}</div>'
                f'<div class="timeline-links">{link_tags}</div>'
                f'</div></div>'
            )
        inner = "".join(cards)
        return (
            f'<div class="timeline-wrapper">'
            f'<div class="timeline-scroll-container" id="timelineScroll">'
            f"{inner}"
            f"</div></div>"
        )
    @env.macro
    def video(path, caption="", width=500, height=None, autoplay=False, loop=True):
        # Handle multiple paths
        paths = [path] if isinstance(path, str) else path
        
        attrs = ['controls', 'preload="metadata"']
        if autoplay: attrs.append('autoplay')
        if loop: attrs.append('loop')
        if width: attrs.append(f'width="{width}"')
        if height: attrs.append(f'height="{height}"')
        
        video_tags = ""
        for p in paths:
            src = get_asset_path(p)
            video_tags += f'<video {" ".join(attrs)}><source src="{src}" type="video/mp4"></video>'
        
        if caption:
            return render_figure(video_tags, caption)
        else:
            return video_tags

    @env.macro
    def spine_viewer(
        container_id,
        skel_path,
        atlas_path,
        width=320,
        height=450,
        animation="Idle_1",
        skin="Normal",
        background="#00000000",
        alpha=True,
        show_controls=False,
        show_loading=False,
        include_assets=True,
        style="",
    ):
        def as_css_size(value):
            if isinstance(value, str) and value.endswith(("px", "%", "rem", "em", "vh", "vw")):
                return value
            return f"{value}px"

        player_js = get_doc_path("javascripts/spine-player.min.js")
        player_css = get_doc_path("css/spine-player.css")
        studio_js = get_doc_path("javascripts/spine-studio.js")
        studio_css = get_doc_path("css/spine-studio.css")
        
        extra_style = f";{style.strip().rstrip(';')}" if style else ""
        viewer_style = f"width:{as_css_size(width)};height:{as_css_size(height)}{extra_style};"
        
        options = {
            "skelUrl": get_asset_path(skel_path),
            "atlasUrl": get_asset_path(atlas_path),
            "backgroundColor": "#00000000" if show_controls else background,
            "alpha": True if show_controls else bool(alpha),
            "preserveDrawingBuffer": True,
            "skin": skin,
            "showControls": bool(show_controls),
            "animation": animation,
            "showLoading": bool(show_loading),
        }
        
        if show_controls:
            script = (
                f"(function init() {{"
                f"    if (!window.spine || !window.spine.SpinePlayer || !window.initSpineStudio) {{"
                f"        console.log('[Spine Init] Waiting... spine:', !!window.spine, 'initSpineStudio:', !!window.initSpineStudio);"
                f"        setTimeout(init, 100);"
                f"        return;"
                f"    }}"
                f"    window.initSpineStudio({json.dumps(container_id)}, {json.dumps(options)});"
                f"}})();"
            )
            
            assets_html = (
                f'<link rel="stylesheet" href="{attr(player_css)}">'
                f'<link rel="stylesheet" href="{attr(studio_css)}">'
                f'<script src="{attr(player_js)}"></script>'
                f'<script src="{attr(studio_js)}"></script>'
                if include_assets else ""
            )

            html = (
                f'{assets_html}'
                f'<div id="{attr(container_id)}_wrapper" class="spine-studio-wrapper">'
                f'  <div class="spine-studio-main">'
                f'    <div id="{attr(container_id)}" class="spine-studio-canvas" style="{attr(viewer_style)}"></div>'
                f'  </div>'
                f'</div>'
                f'<script>{script}</script>'
            )
            return html
        else:
            script = (
                "(function(){"
                "if(!window.spine||!window.spine.SpinePlayer)return;"
                f"new spine.SpinePlayer({json.dumps(container_id)},{json.dumps(options)});"
                "})();"
            )

            assets_html = (
                f'<link rel="stylesheet" href="{attr(player_css)}">'
                f'<script src="{attr(player_js)}"></script>'
                if include_assets else ""
            )

            return (
                assets_html
                + f'<div id="{attr(container_id)}" class="spine-viewer" style="{attr(viewer_style)}"></div>'
                + f'<script>{script}</script>'
            )

    @env.macro
    def spine_multi_viewer(container_id, costumes, default_index=0):
        """Unified Spine viewer with costume switching via dropdown.

        costumes: list of dicts with keys:
            label, skel_path, atlas_path, animation (optional), skin (optional)
        """
        player_js = get_doc_path("javascripts/spine-player.min.js")
        player_css = get_doc_path("css/spine-player.css")
        multi_js = get_doc_path("javascripts/spine-multi.js")
        multi_css = get_doc_path("css/spine-multi.css")

        costume_data = []
        for c in costumes:
            costume_data.append({
                "label": c["label"],
                "skelUrl": get_asset_path(c["skel_path"]),
                "atlasUrl": get_asset_path(c["atlas_path"]),
                "animation": c.get("animation", "Idle_1"),
                "skin": c.get("skin", "Normal"),
            })

        # Build costume dropdown options
        costume_options = "".join(
            f'<option value="{i}"{" selected" if i == default_index else ""}>'
            f'{escape(c["label"])}</option>'
            for i, c in enumerate(costumes)
        )

        cid = escape(container_id)

        script = (
            f"(function init() {{"
            f"    if (!window.spine || !window.spine.SpinePlayer || !window.initSpineMultiViewer) {{"
            f"        setTimeout(init, 100); return;"
            f"    }}"
            f"    window.initSpineMultiViewer("
            f"        {json.dumps(container_id)},"
            f"        {json.dumps(costume_data)},"
            f"        {json.dumps(default_index)}"
            f"    );"
            f"}})();"
        )

        return (
            f'<link rel="stylesheet" href="{escape(player_css)}">'
            f'<link rel="stylesheet" href="{escape(multi_css)}">'
            f'<script src="{escape(player_js)}"></script>'
            f'<script src="{escape(multi_js)}"></script>'
            f'<div id="{cid}_wrapper" class="smv-wrapper">'
            # Canvas
            f'  <div id="{cid}" class="smv-canvas"></div>'
            # Controls
            f'  <div class="smv-controls">'
            f'    <div class="smv-timeline">'
            f'      <span class="smv-time">0.0</span>'
            f'      <input type="range" class="smv-slider" min="0" max="1" value="0" step="0.001">'
            f'      <span class="smv-duration">0.0</span>'
            f'    </div>'
            f'    <div class="smv-btn-row">'
            f'      <button class="smv-play-btn" title="재생/일시정지">'
            f'        <svg class="smv-play-icon" viewBox="0 0 24 24" fill="currentColor">'
            f'          <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>'
            f'        </svg>'
            f'      </button>'
            f'      <select class="smv-select smv-anim-select" title="애니메이션"></select>'
            f'      <select class="smv-select smv-skin-select" title="스킨"></select>'
            f'      <select class="smv-select smv-speed-select" title="속도">'
            f'        <option value="0.25">0.25x</option>'
            f'        <option value="0.5">0.5x</option>'
            f'        <option value="1" selected>1.0x</option>'
            f'        <option value="1.5">1.5x</option>'
            f'        <option value="2">2.0x</option>'
            f'      </select>'
            f'    </div>'
            f'    <div class="smv-btn-row-secondary">'
            f'      <select class="smv-select smv-costume-select" title="코스튬">'
            f'        {costume_options}'
            f'      </select>'
            f'      <div class="smv-sep"></div>'
            f'      <button class="smv-parts-toggle" title="파츠 토글">'
            f'        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>'
            f'      </button>'
            f'      <button class="smv-reset-btn" title="파츠 전체 켜기">'
            f'        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 5V1L7 6l5 5V7c3.31 0 6 2.69 6 6s-2.69 6-6 6-6-2.69-6-6H4c0 4.42 3.58 8 8 8s8-3.58 8-8-3.58-8-8-8z"/></svg>'
            f'      </button>'
            f'      <button class="smv-undo-btn" title="되돌리기">'
            f'        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.5 8c-2.65 0-5.05.99-6.9 2.6L2 7v9h9l-3.62-3.62c1.39-1.16 3.16-1.88 5.12-1.88 3.54 0 6.55 2.31 7.6 5.5l2.37-.78C21.08 11.03 17.15 8 12.5 8z"/></svg>'
            f'      </button>'
            f'      <div class="smv-sep"></div>'
            f'      <button class="smv-export-png" title="PNG 저장">'
            f'        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M9 2L7.17 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2h-3.17L15 2H9zm3 15c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5z"/></svg>'
            f'        PNG'
            f'      </button>'
            f'      <button class="smv-export-gif" title="GIF 저장">'
            f'        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M18 4l2 4h-3l-2-4h-2l2 4h-3l-2-4H8l2 4H7L5 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2h-2z"/></svg>'
            f'        GIF'
            f'      </button>'
            f'    </div>'
            f'  </div>'
            # Collapsible parts panel
            f'  <div class="smv-parts-panel">'
            f'    <div class="smv-parts-header">'
            f'      <input type="text" class="smv-parts-search" placeholder="파츠 검색...">'
            f'      <button class="smv-parts-reset">전체 켜기</button>'
            f'    </div>'
            f'    <div class="smv-parts-list"></div>'
            f'  </div>'
            # GIF progress overlay
            f'  <div class="smv-gif-overlay">'
            f'    <div>GIF 렌더링 중...</div>'
            f'    <div class="smv-gif-progress-bar"><div class="smv-gif-progress"></div></div>'
            f'  </div>'
            f'</div>'
            f'<script>{script}</script>'
        )

    @env.macro
    def image(path, caption="", width=500, height=None):
        # Handle multiple paths
        paths = [path] if isinstance(path, str) else path
        alt_text = caption_alt_text(caption)
        
        img_attr = []
        if width:
            img_attr.append(f'width="{width}"')
        if height:
            img_attr.append(f'height="{height}"')
        
        img_tags = ""
        for p in paths:
            src = get_asset_path(p)
            img_tags += f'<img src="{src}" {" ".join(img_attr)} alt="{attr(alt_text)}">'
        
        if caption:
            return render_figure(img_tags, caption)
        else:
            return img_tags

    # Ordered list of major sections: (label, src_path relative to docs/)
    _SECTIONS = [
        ("🏡", "index.md"),
        ("소개", "overview/overview.md"),
        ("캐릭터 정보", "info/viewer.md"),
        ("시즌 1", "story/chapter/s1_main.md"),
        ("시즌 2", "story/chapter/s2_main.md"),
        ("시즌 3", "story/chapter/s3_main.md"),
        ("기타", "others/others_main.md"),
    ]

    @env.macro
    def section_nav():
        src = env.page.file.src_path.replace("\\", "/")
        idx = None
        for i, (_, path) in enumerate(_SECTIONS):
            if src == path:
                idx = i
                break
        if idx is None:
            return ""

        src_dir = os.path.dirname(src)
        levels = len(src_dir.split("/")) if src_dir else 0
        prefix = "../" * levels

        def make_href(md_path):
            return f"{prefix}{md_path[:-3]}.html"

        prev_html = ""
        next_html = ""
        if idx > 0:
            prev_label, prev_path = _SECTIONS[idx - 1]
            prev_href = make_href(prev_path)
            prev_html = (
                f'<a class="section-nav-btn section-nav-prev" href="{attr(prev_href)}">'
                f'<span class="section-nav-arrow">&#10094;</span>'
                f'<span class="section-nav-label">{prev_label}</span></a>'
            )
        if idx < len(_SECTIONS) - 1:
            next_label, next_path = _SECTIONS[idx + 1]
            next_href = make_href(next_path)
            next_html = (
                f'<a class="section-nav-btn section-nav-next" href="{attr(next_href)}">'
                f'<span class="section-nav-label">{next_label}</span>'
                f'<span class="section-nav-arrow">&#10095;</span></a>'
            )
        return f'<nav class="section-nav-bar">{prev_html}{next_html}</nav>'
