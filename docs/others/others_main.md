---
title: 기타 - 인게임
publish: true
icon: fontawesome/solid/book-tanakh
description: 기타에서 에슈르가 등장하거나 언급되는 챕터 바로가기입니다.
subtitle:
tags:
  - 목차
---
# 기타
## {{ section_flag('others-main') }}인게임
{% set cards %}
{{ story_card('미니게임', 'chapterimg/ChapterImage_WeekEnd_TowerBattle_Story_1.png', '../others/minigame.md') }}
{{ story_card('연관 에셋', 'chapterimg/Character_Ashur_Story_2.png', '../others/asset.md') }}
{% endset %}
{{ card_grid(cards) }}

## {{ section_flag('others-external') }}외부
{% set cards %}
{{ story_card('공식 이벤트', 'chapterimg/ChapterImage_WeekEnd_CookingTycoon_Story_1.png', '../others/event.md') }}
{{ story_card('밈/여담', 'chapterimg/ChapterImage_WeekEnd_WWElias_Story_1.png', '../others/meme.md') }}
{{ story_card('구릭컬', 'chapterimg/ChapterImage_WeekEnd_TricDice_Story_1.png', '../others/old.md') }}
{{ story_card('기타', 'chapterimg/ChapterImage_Aside1.png', '../others/etc.md') }}
{% endset %}
{{ card_grid(cards) }}