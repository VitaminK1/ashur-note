---
title: 캐릭터 정보 - 옷장
publish: true
icon: fontawesome/solid/shirt
subtitle: 스파인 뷰어
tags:
  - 캐릭터정보
---

# 캐릭터 정보 - 옷장
+ 스탠딩과 전투 모습이 보이지 않는다면 새로고침을 시도해주세요.
+ 터치나 마우스를 댄 후 나오는 컨트롤러의 사람 버튼을 누른 뒤 모션을 고르면 다른 모션을 감상할 수 있습니다.

## 사복 설명
{{ tabs([
    ['기본 사복', image('ashurdesc_2.png', height=300, caption='에슈르 기본 사복 설명')],
    ['아이스크림 메이커', image('ashurdesc_1.png', height=300, caption='에슈르 아이스크림 메이커 사복 설명')],
    ['평온한 온천 여행', image('ashurdesc_3.png', height=300, caption='에슈르 평온한 온천 여행 사복 설명')],
]) }}

## 스탠딩
{{ tabs([
    ['기본 사복', spine_viewer('player-container1', 'spine/standing/Ashur.skel', 'spine/standing/Ashur.atlas', width=360, height=450, background='#ffffffff', animation='Idle_1', show_controls=True, style='margin:0 auto')],
    ['아이스크림 메이커', spine_viewer('player-container3', 'spine/standingskin1/AshurSkin1.skel', 'spine/standingskin1/AshurSkin1.atlas', width=360, height=450, background='#ffffffff', animation='Idle_1', show_controls=True, style='margin:0 auto')],
    ['평온한 온천 여행', spine_viewer('player-container5', 'spine/standingskin2/AshurSkin2.skel', 'spine/standingskin2/AshurSkin2.atlas', width=360, height=450, background='#ffffffff', animation='Idle_1', show_controls=True, style='margin:0 auto')],
]) }}


<br>

## 전투
{{ tabs([
    ['기본 사복', spine_viewer('player-container2', 'spine/battle/Ashur.skel', 'spine/battle/Ashur.atlas', width=360, height=450, background='#ffffffff', animation='Idle', show_controls=True, style='margin:0 auto')],
    ['아이스크림 메이커', spine_viewer('player-container4', 'spine/battleskin1/AshurSkin1.skel', 'spine/battleskin1/AshurSkin1.atlas', width=360, height=450, background='#ffffffff', animation='Idle', show_controls=True, style='margin:0 auto')],
    ['평온한 온천 여행', spine_viewer('player-container6', 'spine/battleskin2/AshurSkin2.skel', 'spine/battleskin2/AshurSkin2.atlas', width=360, height=450, background='#ffffffff', animation='Idle', show_controls=True, style='margin:0 auto')],
]) }}

<br>
<br>
