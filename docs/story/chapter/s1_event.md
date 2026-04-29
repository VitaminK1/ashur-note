---
title: 이벤트 스토리 시즌 1
publish: true
icon: fontawesome/solid/book-medical
tags:
  - 목차
---
# 이벤트 스토리 시즌 1

+ 해당 챕터의 이미지를 눌러 이동할 수 있습니다.

{% set cards %}
{{ story_card('멜트다운 버터', 'chapterimg/ChapterImage_ThemeEvent1.png', '../s1_event/butter.md') }}
{{ story_card('강철의 지옥 단련', 'chapterimg/ChapterImage_ThemeEvent8.png', '../s1_event/leets.md') }}
{{ story_card('피코라의 멘토 콤플렉스', 'chapterimg/ChapterImage_ThemeEvent9.png', '../s1_event/picora.md') }}
{{ story_card('미드나잇 마리오네트', 'chapterimg/ChapterImage_ThemeEvent20.png', '../s1_event/barong.md') }}
{{ story_card('누구를 위하여 기도를 올리나', 'chapterimg/ChapterImage_ThemeEvent24.png', '../s1_event/joanne.md') }}
{% endset %}

{{ card_grid(cards) }}