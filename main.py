import json
import os
from html import escape

def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """
    
    def clean_rel_path(path):
        return str(path).lstrip('/').replace('\\', '/')

    def attr(value):
        return escape(str(value), quote=True)

    def indent_html(value, spaces=4):
        prefix = " " * spaces
        return prefix + str(value).replace("\n", "\n" + prefix)

    def multiline(value):
        if isinstance(value, (list, tuple)):
            return "<br>".join(str(item) for item in value)
        return str(value)

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
    def present_card(title, description, image_path, letter_path="letter.png", image_alt="item image"):
        return f"""<div class="vk-card-outer">
  <div class="vk-card">
    <div class="vk-card__left">
      <img class="vk-card__img-placeholder" src="{get_asset_path(image_path)}" alt="{attr(image_alt)}">
    </div>
    <div class="vk-card__right">
      <h3 class="vk-title">{title}</h3>
      <p class="vk-sub vk-small">{description}</p>
    </div>
    <div class="vk-letter">
      <img src="{get_asset_path(letter_path)}" alt="">
    </div>
  </div>
</div>"""

    @env.macro
    def intimacy_table(title, rows, notes=None):
        note_html = ""
        if notes:
            note_html = "\n".join(f"  <span> - {note}</span><br>" for note in notes)
            note_html += "\n"

        body_rows = []
        for row in rows:
            label, text = row[:2]
            values = list(text) if isinstance(text, (list, tuple)) else [text]
            rowspan_attr = f' rowspan="{len(values)}"' if len(values) > 1 else ""
            body_rows.append(
                f'        <tr><td class="intimacy-level"{rowspan_attr}>{label}</td>'
                f'<td class="intimacy-text">{values[0]}</td></tr>'
            )
            for value in values[1:]:
                body_rows.append(f'        <tr><td class="intimacy-text">{value}</td></tr>')

        body = "\n".join(body_rows)
        return f"""<div class="intimacy-wrap">
  <h3 class="intimacy-title">{title}</h3>
{note_html}  <div class="intimacy-table-wrap">
    <table class="intimacy-table">
      <tbody>
{body}
      </tbody>
    </table>
  </div>
</div>"""

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
        {desc}
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
      <p class="battle-copy">{description}</p>
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
            width=320,
            height=450,
            background="#ffffff",
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
        <div class="rk-desc">{description}</div>
      </div>
    </div>
    <div class="rk-tmi-row">
      <div class="rk-tmi-pill">TMI</div>
      <div class="rk-tmi-sep" aria-hidden="true"></div>
      <div class="rk-tmi-right">
        <div class="rk-mini-avatar" title="{attr(name)}">
          <img class="rk-mini-avatar-img" src="{get_asset_path(mini_avatar)}" alt="{attr(name)}">
        </div>
        <span class="rk-tmi-text">{tmi}</span>
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
          <div class="kj-text">{text}</div>
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
            img_indent_extra = int(icon[3]) if len(icon) > 3 else 0
            img_indent = " " * (10 + img_indent_extra)
            icon_path = get_asset_path(f"sadoicon/Icon_GraduateSkill_{image}.png")
            return (
                f'          <div class="pref-icon pref-circle-{size}" title="{title}">\n'
                f'{img_indent}<img class="frame circle" src="{icon_path}" alt="food">\n'
                "          </div>"
            )

        def row_html(row):
            label, icons = row
            icon_lines = "\n".join(icon_html(icon) for icon in icons)
            icon_block = f"\n{icon_lines}\n" if icon_lines else "\n"
            return f"""      <tr>
        <td class="pref-icon-cell"><span>{label}</span></td>
        <td>{icon_block}        </td>
      </tr>"""

        body = "\n".join(row_html(row) for row in rows)
        return f"""<div class="prefs-table-alt-wrap pref-size-md">
  <table class="prefs-table-alt">
    <thead><tr>
        <th>거리</th>
        <th><div class="th-cell"><span>사도</span></div></th>
      </tr></thead>
    <tbody>
{body}
    </tbody>
  </table>
</div>
<br>
<br>"""

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
        return f""":sadoicon-{char_id}:{{:.big-emoji}}<span class="tag-box" data-sado="{char_id}">{name}</span><br><div class="speech-bubble">{text}</div>"""

    @env.macro
    def mind_speech(text):
        return f"""<div class="mind-bubble">{text}</div>"""

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
    def tabs(items):
        return tab_block(items)

    # --- Media Macros ---
    @env.macro
    def youtube(video_id, caption="", width=600, height=None):
        style = ["margin: 0 auto;", "width: 100%;"]
        if width:
            style.append(f"max-width: {width if str(width).endswith(('px', '%')) else str(width) + 'px'};")
        if height:
            style.append(f"max-height: {height if str(height).endswith(('px', '%')) else str(height) + 'px'};")
        
        style_attr = f' style="{" ".join(style)}"' if style else ''
        iframe = f'<iframe class="video" src="https://www.youtube.com/embed/{video_id}" allowfullscreen></iframe>'
        
        if caption:
            return f'<figure{style_attr} markdown="1"><div class="video-wrapper">{iframe}</div><figcaption markdown="1">{caption}</figcaption></figure>'
        else:
            return f"""<div class="video-wrapper"{style_attr}>{iframe}</div>"""

    @env.macro
    def story_card(title, img_path, link):
        """Creates a stylized card for story chapters."""
        img_url = get_asset_path(img_path)
        
        # Resolve the markdown link extension based on MkDocs configuration
        if '.md' in link:
            use_dir_urls = env.conf.get('use_directory_urls', True)
            if use_dir_urls:
                link = link.replace('.md', '/')
            else:
                link = link.replace('.md', '.html')
                
        return f'<a href="{link}" class="story-card">' \
               f'<div class="story-card-img" style="background-image: url(\'{img_url}\');"></div>' \
               f'<div class="story-card-title">{attr(title)}</div>' \
               f'</a>'

    @env.macro
    def card_grid(content):
        """Wraps cards in a grid container."""
        return f'<div class="card-grid">{content}</div>'

    @env.macro
    def video(path, caption="", width=500, height=None, autoplay=True, loop=True):
        src = get_asset_path(path)
        attrs = ['controls', 'preload="metadata"']
        if autoplay: attrs.append('autoplay')
        if loop: attrs.append('loop')
        if width: attrs.append(f'width="{width}"')
        if height: attrs.append(f'height="{height}"')
        
        video_tag = f'<video {" ".join(attrs)}><source src="{src}" type="video/mp4"></video>'
        
        if caption:
            return f'<figure markdown="1">{video_tag}<figcaption markdown="1">{caption}</figcaption></figure>'
        else:
            return video_tag

    @env.macro
    def spine_viewer(
        container_id,
        skel_path,
        atlas_path,
        width=320,
        height=450,
        animation="Idle_1",
        skin="Normal",
        background="#ffffff",
        alpha=False,
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
        extra_style = f";{style.strip().rstrip(';')}" if style else ""
        viewer_style = f"width:{as_css_size(width)};height:{as_css_size(height)}{extra_style};"
        options = {
            "skelUrl": get_asset_path(skel_path),
            "atlasUrl": get_asset_path(atlas_path),
            "backgroundColor": background,
            "alpha": bool(alpha),
            "preserveDrawingBuffer": True,
            "skin": skin,
            "showControls": bool(show_controls),
            "animation": animation,
            "showLoading": bool(show_loading),
        }
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
    def image(path, caption="", width=500, height=None):
        # Handle multiple paths
        paths = [path] if isinstance(path, str) else path
        
        img_attr = []
        if width:
            img_attr.append(f'width="{width}"')
        if height:
            img_attr.append(f'height="{height}"')
        
        img_tags = ""
        for p in paths:
            src = get_asset_path(p)
            img_tags += f'<img src="{src}" {" ".join(img_attr)} alt="{attr(caption if caption else "Image")}">'
        
        if caption:
            return f'<figure markdown="1">{img_tags}<figcaption markdown="1">{caption}</figcaption></figure>'
        else:
            return img_tags
