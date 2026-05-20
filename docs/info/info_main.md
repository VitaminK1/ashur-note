---
title: 캐릭터 정보
publish: true
icon: fontawesome/solid/book-tanakh
description: 캐릭터 정보 바로가기
subtitle:
tags:
  - 목차
---
# 캐릭터 정보
{{ section_nav() }}
## {{ section_flag('info-main') }}캐릭터 정보
{% set cards %}
{{ story_card('기록', 'chapterimg/Character_Ashur_Story_1.png', '../info/viewer.md') }}
{{ story_card('전투', 'chapterimg/Character_Ashur_Story_2.png', '../info/battle.md') }}
{{ story_card('육성', 'chapterimg/ChapterImage_Reminiscenceend1.png', '../info/growth.md') }}
{% endset %}
{{ card_grid(cards) }}
