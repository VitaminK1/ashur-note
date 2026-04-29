---
title: 메인 스토리 시즌 1
publish: true
icon: fontawesome/solid/book-tanakh
description: 메인 스토리 시즌 1에서 에슈르가 등장하거나 언급되는 챕터 바로가기입니다.
subtitle: 챕터 바로가기
tags:
  - 목차
---
# 메인 스토리 시즌 1

아래 카드에서 각 챕터 이미지를 눌러 이동할 수 있습니다.

{% set cards %}
{{ story_card('챕터 1 - 최소한 잼은 발라줘', 'chapterimg/ChapterImage_S1_1.png', '../s1_main/c1.md') }}
{{ story_card('챕터 4 - 왕국 폭발 5분 전', 'chapterimg/ChapterImage_S1_4.png', '../s1_main/c4.md') }}
{{ story_card('챕터 5 - 옆 집 불구경', 'chapterimg/ChapterImage_S1_5.png', '../s1_main/c5.md') }}
{{ story_card('챕터 6 - 네 번 절하고 네 번 박아', 'chapterimg/ChapterImage_S1_6.png', '../s1_main/c6.md') }}
{{ story_card('챕터 7 - 빠따가 약이다', 'chapterimg/ChapterImage_S1_7.png', '../s1_main/c7.md') }}
{{ story_card('챕터 8 - 파.워. 하우스', 'chapterimg/ChapterImage_S1_8.png', '../s1_main/c8.md') }}
{{ story_card('챕터 9 - 막판 뒤집어버리기', 'chapterimg/ChapterImage_S1_9.png', '../s1_main/c9.md') }}
{% endset %}

{{ card_grid(cards) }}
