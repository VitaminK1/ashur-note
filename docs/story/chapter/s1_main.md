---
title: 메인 스토리 시즌 1
publish: true
icon: fontawesome/solid/book-tanakh
description: 메인 스토리 시즌 1에서 에슈르가 등장하거나 언급되는 챕터 바로가기입니다.
subtitle: 챕터 바로가기
tags:
  - 목차
---
# 시즌 1
## {{ section_flag('s1-main') }}메인 스토리
{% set cards %}
{{ story_card('챕터 1 - 최소한 잼은 발라줘', 'chapterimg/ChapterImage_S1_1.png', '../s1_main/c1.md', freq='자주 등장') }}
{{ story_card('챕터 4 - 왕국 폭발 5분 전', 'chapterimg/ChapterImage_S1_4.png', '../s1_main/c4.md', freq='자주 등장') }}
{{ story_card('챕터 5 - 옆 집 불구경', 'chapterimg/ChapterImage_S1_5.png', '../s1_main/c5.md', freq='보통 등장') }}
{{ story_card('챕터 6 - 네 번 절하고 네 번 박아', 'chapterimg/ChapterImage_S1_6.png', '../s1_main/c6.md', freq='자주 등장') }}
{{ story_card('챕터 7 - 빠따가 약이다', 'chapterimg/ChapterImage_S1_7.png', '../s1_main/c7.md', freq='자주 등장') }}
{{ story_card('챕터 8 - 파.워. 하우스', 'chapterimg/ChapterImage_S1_8.png', '../s1_main/c8.md', freq='가끔 등장') }}
{{ story_card('챕터 9 - 막판 뒤집어버리기', 'chapterimg/ChapterImage_S1_9.png', '../s1_main/c9.md', freq='자주 등장') }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('s1-event') }}이벤트 스토리
{% set cards %}
{{ story_card('멜트다운 버터', 'chapterimg/ChapterImage_ThemeEvent1.png', '../s1_event/butter.md', freq='자주 등장') }}
{{ story_card('강철의 지옥 단련', 'chapterimg/ChapterImage_ThemeEvent8.png', '../s1_event/leets.md', freq='가끔 등장') }}
{{ story_card('피코라의 멘토 콤플렉스', 'chapterimg/ChapterImage_ThemeEvent9.png', '../s1_event/picora.md', freq='자주 등장') }}
{{ story_card('미드나잇 마리오네트', 'chapterimg/ChapterImage_ThemeEvent20.png', '../s1_event/barong.md', freq='보통 등장') }}
{{ story_card('누구를 위하여 기도를 올리나', 'chapterimg/ChapterImage_ThemeEvent24.png', '../s1_event/joanne.md', freq='자주 등장') }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('s1-sado') }}사도 스토리
{% set cards %}
{{ story_card('에슈르', 'characterstory/Character_Ashur_Story_1.png', '../s1_sado/ashur.md', freq='자주 등장') }}
{{ story_card('네르', 'characterstory/Character_Ner_Story_1.png', '../s1_sado/ner.md', freq='보통 등장') }}
{{ story_card('에르핀', 'characterstory/Character_Erpin_Story_1.png', '../s1_sado/erpin.md', freq='언급됨') }}
{{ story_card('슈팡', 'characterstory/Character_Shoupan_Story_1.png', '../s1_sado/shoupan.md', freq='자주 등장') }}
{{ story_card('사리', 'characterstory/Character_Sari_Story_1.png', '../s1_sado/sari.md', freq='자주 등장') }}
{{ story_card('리스티', 'characterstory/Character_Risty_Story_1.png', '../s1_sado/risty.md', freq='언급됨') }}
{{ story_card('빅우드', 'characterstory/Character_BigWood_Story_1.png', '../s1_sado/bigwood.md', freq='자주 등장') }}
{{ story_card('앨리스', 'characterstory/Character_Alice_Story_1.png', '../s1_sado/alice.md', freq='가끔 등장') }}
{{ story_card('에피카', 'characterstory/Character_Epica_Story_1.png', '../s1_sado/epica.md', freq='가끔 등장') }}
{{ story_card('가끔 등장', 'characterstory/Character_Snorky_Story_1.png', '../s1_sado/etc.md', freq='보통 등장') }}
{{ story_card('언급됨', 'characterstory/Character_Sherum_Story_1.png', '../s1_sado/etc2.md', freq='언급됨') }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('s1-etc') }}기타 스토리
{% set cards %}
{{ story_card('코미의 일기', 'story/Diary_Komi_1.png', '../s1_etc/s1_etc.md', freq='언급됨') }}
{% endset %}
{{ card_grid(cards) }}
