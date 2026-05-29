---
title: Study
publish: true
icon: material/book-open-variant
description: 
subtitle: Study
search:
  exclude: true
tags:
  - study
---

# {{ section_flag('study-main') }}공부 정리 자료
{% set cards %}
{{ story_card('데이터베이스론', 'chapterimg/ChapterImage_WeekEnd_CookingTycoon_Story_1.png', 'dbms/main.md') }}
{{ story_card('소프트웨어공학', 'chapterimg/ChapterImage_WeekEnd_WWElias_Story_1.png', 'software/main.md') }}
{{ story_card('자료구조론', 'chapterimg/ChapterImage_WeekEnd_TricDice_Story_1.png', 'datastructure/main.md') }}
{{ story_card('정보보호론', 'chapterimg/ChapterImage_Aside1.png', 'security/main.md') }}
{{ story_card('PSAT', 'chapterimg/ChapterImage_WeekEnd_TowerBattle_Story_1.png', 'psat/main.md') }}
{% endset %}
{{ card_grid(cards) }}
