---
title: 소프트웨어공학 목차
publish: true
icon: fontawesome/solid/book-tanakh
description: 소프트웨어공학 챕터 바로가기
subtitle: 챕터 바로가기
tags:
  - 목차
---
# 소프트웨어공학
{{ section_nav() }}
## {{ section_flag('software-main') }}메인 챕터
{% set cards %}
{{ story_card('챕터 1 - 데이터베이스 개요', 'chapterimg/ChapterImage_S1_1.png', 'c1.md', freq=0) }}
{{ story_card('챕터 2 - 데이터 저장 및 파일구조', 'chapterimg/ChapterImage_S1_2.png', 'c2.md', freq=0) }}
{{ story_card('챕터 3 - 데이터베이스 설계', 'chapterimg/ChapterImage_S1_3.png', 'c3.md', freq=0) }}
{{ story_card('챕터 4 - 데이터 모델링', 'chapterimg/ChapterImage_S1_4.png', 'c4.md', freq=0) }}
{{ story_card('챕터 5 - 관계 데이터 구조', 'chapterimg/ChapterImage_S1_5.png', 'c5.md', freq=0) }}
{{ story_card('챕터 6 - 관계 데이터 연산', 'chapterimg/ChapterImage_S1_6.png', 'c6.md', freq=0) }}
{{ story_card('챕터 7 - 관계 데이터베이스 언어', 'chapterimg/ChapterImage_S1_7.png', 'c7.md', freq=0) }}
{{ story_card('챕터 8 - 데이터 종속성과 정규화', 'chapterimg/ChapterImage_S1_8.png', 'c8.md', freq=0) }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('software-etc') }}기타
{% set cards %}
{{ story_card('용어 정리', 'chapterimg/ChapterImage_ThemeEvent1.png', 'e1.md', freq=0) }}
{% endset %}
{{ card_grid(cards) }}