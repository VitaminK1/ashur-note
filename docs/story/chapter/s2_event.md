---
title: 이벤트 스토리 시즌 2
publish: true
icon: fontawesome/solid/book-medical
tags:
  - 목차
---
# 이벤트 스토리 시즌 2

+ 해당 챕터의 이미지를 눌러 이동할 수 있습니다.

{% set cards %}
{{ story_card('슬기로운 메이드 생활', 'chapterimg/ChapterImage_ThemeEvent27.png', '../s2_event/speaki.md', freq='언급됨') }}
{{ story_card('파티에는 축복과 위로를', 'chapterimg/ChapterImage_ThemeEvent29.png', '../s2_event/opal.md', freq='자주 등장') }}
{{ story_card('불 붙은 불행 속 쓰나미', 'chapterimg/ChapterImage_ThemeEvent33.png', '../s2_event/shasha.md', freq='보통 등장') }}
{{ story_card('수상한 요리사의 쿠킹비망록', 'chapterimg/ChapterImage_ThemeEvent38.png', '../s2_event/ricota.md', freq='언급됨') }}
{{ story_card('댄스 쇼다운! 꿈꾸는 포도!', 'chapterimg/ChapterImage_ThemeEvent42.png', '../s2_event/arco.md', freq='외부 등장') }}
{{ story_card('그을음 끝에 피어나는 빛무리', 'chapterimg/ChapterImage_ThemeEvent49.png', '../s2_event/uros.md', freq='언급됨') }}
{{ story_card('즐겁고 힘든 온천기행!', 'chapterimg/ChapterImage_SkinSet8.png', '../s2_event/onsen.md', freq='자주 등장') }}
{% endset %}

{{ card_grid(cards) }}