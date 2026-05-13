---
title: 메인 스토리 시즌 2
publish: true
icon: fontawesome/solid/book-tanakh
tags:
  - 목차
---
# 메인 스토리 시즌 2

+ 해당 챕터의 이미지를 눌러 이동할 수 있습니다.

{% set cards %}
{{ story_card('챕터 3 - 난장판 내 마음', 'chapterimg/ChapterImage_S2_3.png', '../s2_main/c3.md', freq='언급됨') }}
{{ story_card('챕터 4 - 어제와 내일과 함께', 'chapterimg/ChapterImage_S2_4.png', '../s2_main/c4.md', freq='자주 등장') }}
{{ story_card('챕터 10 - 작고 소중해', 'chapterimg/ChapterImage_S2_10.png', '../s2_main/c10.md', freq='언급됨') }}
{% endset %}

{{ card_grid(cards) }}