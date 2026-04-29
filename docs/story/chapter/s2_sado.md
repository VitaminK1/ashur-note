---
title: 사도 스토리 시즌 2
publish: true
icon: fontawesome/solid/address-book
tags:
  - 목차
---
# 사도 스토리 시즌 2

+ 해당 챕터의 이미지를 눌러 이동할 수 있습니다.

{% set cards %}
{{ story_card('그윈', 'characterstory/Character_Guin_Story_1.png', '../s2_sado/guin.md') }}
{{ story_card('폴랑', 'characterstory/Character_Polan_Story_1.png', '../s2_sado/polan.md') }}
{{ story_card('슈로', 'characterstory/Character_Suro_Story_1.png', '../s2_sado/suro.md') }}
{{ story_card('오팔', 'characterstory/Character_Opal_Story_1.png', '../s2_sado/opal.md') }}
{{ story_card('마요(멋짐)', 'characterstory/Character_MayoCool_Story_1.png', '../s2_sado/mayocool.md') }}
{{ story_card('스피키(메이드)', 'characterstory/Character_SpeakiMaid_Story_1.png', '../s2_sado/speakimaid.md') }}
{{ story_card('디아나(왕년)', 'characterstory/Character_DianaYester_Story_1.png', '../s2_sado/dianayester.md') }}
{{ story_card('시저', 'characterstory/Character_Scizor_Story_1.png', '../s2_sado/scizor.md') }}
{{ story_card('가끔 등장', 'characterstory/Character_Kathy_Story_1.png', '../s2_sado/etc.md') }}
{% endset %}

{{ card_grid(cards) }}