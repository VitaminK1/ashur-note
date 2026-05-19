---
title: 메인 스토리 시즌 3
publish: true
icon: fontawesome/solid/book-tanakh
description: 메인 스토리 시즌 3에서 에슈르가 등장하거나 언급되는 챕터 바로가기입니다.
subtitle: 챕터 바로가기
tags:
  - 목차
---
# 시즌 3
{{ section_nav() }}
## {{ section_flag('s3-main') }}메인 스토리
{% set cards %}
{{ story_card('챕터 1 - 푸름 끝에 싹트는 약속', 'chapterimg/ChapterImage_S3_1.png', '../s3_main/c1.md', freq='보통 등장') }}
{{ story_card('챕터 2 - 틈새에 숨은 그림자', 'chapterimg/ChapterImage_S3_2.png', '../s3_main/c2.md', freq='가끔 등장') }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('s3-event') }}이벤트 스토리
{% set cards %}
{{ story_card('네가 없는 사이에 보내는 편지', 'chapterimg/ChapterImage_ThemeEvent56.png', '../s3_event/dayapureshine.md', freq='가끔 등장') }}
{{ story_card('당신을 위한 응원!', 'chapterimg/ChapterImage_SkinSet13.png', '../s3_event/cheerleader.md', freq='보통 등장') }}
{{ story_card('여왕님의 마음으로 만든 나라', 'chapterimg/ChapterImage_ThemeEvent60.png', '../s3_event/erpinroyale.md', freq='기타 등장') }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('s3-sado') }}사도 스토리
{% set cards %}
{{ story_card('아멜리아(R41)', 'characterstory/Character_AmeliaR41_Story_1.png', '../s3_sado/ameliaR41.md', freq='보통 등장') }}
{{ story_card('에르핀(왕도)', 'characterstory/Character_ErpinRoyale_Story_1.png', '../s3_sado/erpinroyale.md', freq='자주 등장') }}
{{ story_card('레비(졸업)', 'characterstory/Character_LeviGraduate_Story_1.png', '../s3_sado/levigraduate.md', freq='가끔 등장') }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('s3-etc') }}기타
{% set cards %}
{{ story_card('연회장', 'chapterimg/ScheduleStory_Ashur_1.png', '../s3_etc/restaurant.md', freq='기타 등장') }}
{{ story_card('두근 두근 대환장쇼!', 'chapterimg/ChapterImage_SkinSet14.png', '../s3_etc/aprilfool.md', freq='기타 등장') }}
{% endset %}
{{ card_grid(cards) }}