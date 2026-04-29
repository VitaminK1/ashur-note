---
title: 사도 스토리 시즌 1
publish: true
icon: fontawesome/solid/address-book
tags:
  - 목차
---
# 사도 스토리 시즌 1

+ 해당 챕터의 이미지를 눌러 이동할 수 있습니다.

{% set cards %}
{{ story_card('에슈르', 'characterstory/Character_Ashur_Story_1.png', '../s1_sado/ashur.md') }}
{{ story_card('네르', 'characterstory/Character_Ner_Story_1.png', '../s1_sado/ner.md') }}
{{ story_card('에르핀', 'characterstory/Character_Erpin_Story_1.png', '../s1_sado/erpin.md') }}
{{ story_card('슈팡', 'characterstory/Character_Shoupan_Story_1.png', '../s1_sado/shoupan.md') }}
{{ story_card('사리', 'characterstory/Character_Sari_Story_1.png', '../s1_sado/sari.md') }}
{{ story_card('리스티', 'characterstory/Character_Risty_Story_1.png', '../s1_sado/risty.md') }}
{{ story_card('빅우드', 'characterstory/Character_BigWood_Story_1.png', '../s1_sado/bigwood.md') }}
{{ story_card('앨리스', 'characterstory/Character_Alice_Story_1.png', '../s1_sado/alice.md') }}
{{ story_card('에피카', 'characterstory/Character_Epica_Story_1.png', '../s1_sado/epica.md') }}
{{ story_card('가끔 등장', 'characterstory/Character_Snorky_Story_1.png', '../s1_sado/etc.md') }}
{{ story_card('언급됨', 'characterstory/Character_Sherum_Story_1.png', '../s1_sado/etc2.md') }}
{% endset %}

{{ card_grid(cards) }}