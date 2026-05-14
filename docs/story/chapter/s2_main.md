---
title: 메인 스토리 시즌 2
publish: true
icon: fontawesome/solid/book-tanakh
subtitle: 챕터 바로가기
tags:
  - 목차
---
# 시즌 2
## {{ section_flag('s2-main') }}메인 스토리
{% set cards %}
{{ story_card('챕터 3 - 난장판 내 마음', 'chapterimg/ChapterImage_S2_3.png', '../s2_main/c3.md', freq='언급됨') }}
{{ story_card('챕터 4 - 어제와 내일과 함께', 'chapterimg/ChapterImage_S2_4.png', '../s2_main/c4.md', freq='보통 등장') }}
{{ story_card('챕터 10 - 작고 소중해', 'chapterimg/ChapterImage_S2_Bonus01.png', '../s2_main/c10.md', freq='언급됨') }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('s2-event') }}이벤트 스토리
{% set cards %}
{{ story_card('불 붙은 불행 속 쓰나미', 'chapterimg/ChapterImage_ThemeEvent33.png', '../s2_event/shasha.md', freq='보통 등장') }}
{{ story_card('수상한 요리사의 쿠킹비망록', 'chapterimg/ChapterImage_ThemeEvent38.png', '../s2_event/ricota.md', freq='언급됨') }}
{{ story_card('댄스 쇼다운! 꿈꾸는 포도!', 'chapterimg/ChapterImage_ThemeEvent42.png', '../s2_event/arco.md', freq='기타 등장') }}
{{ story_card('그을음 끝에 피어나는 빛무리', 'chapterimg/ChapterImage_ThemeEvent49.png', '../s2_event/uros.md', freq='언급됨') }}
{{ story_card('즐겁고 힘든 온천기행!', 'chapterimg/ChapterImage_SkinSet8.png', '../s2_event/onsen.md', freq='자주 등장') }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('s2-sado') }}사도 스토리
{% set cards %}
{{ story_card('슈로', 'characterstory/Character_Suro_Story_1.png', '../s2_sado/suro.md', freq='자주 등장') }}
{{ story_card('마요(멋짐)', 'characterstory/Character_MayoCool_Story_1.png', '../s2_sado/mayocool.md', freq='자주 등장') }}
{{ story_card('디아나(왕년)', 'characterstory/Character_DianaYester_Story_1.png', '../s2_sado/dianayester.md', freq='등장 없음') }}
{{ story_card('시저', 'characterstory/Character_Scizor_Story_1.png', '../s2_sado/scizor.md', freq='보통 등장') }}
{{ story_card('가끔 등장', 'characterstory/Character_Kathy_Story_1.png', '../s2_sado/etc.md', freq='언급됨') }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('s2-etc') }}기타
{% set cards %}
{{ story_card('연회장 대사', 'chapterimg/ScheduleStory_Ashur_1.png', '../s2_etc/restaurant.md', freq='기타 등장') }}
{{ story_card('엉망진창 대환장 대소동', 'chapterimg/ChapterImage_Fake1.png', '../s2_etc/aprilfool.md', freq='기타 등장') }}
{% endset %}
{{ card_grid(cards) }}