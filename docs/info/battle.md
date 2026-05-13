---
title: 캐릭터 정보 - 전투
publish: true
icon: material/sword-cross
description: 에슈르의 기본 스탯, 스킬 영상, 어사이드 효과를 정리한 전투 정보 페이지입니다.
subtitle: 스탯, 스킬, 어사이드, 보드, 랭크효과
tags:
  - 캐릭터정보
---

# 캐릭터 정보 - 전투
!!! warning "주의"
    게임 내 성능 인플레이션으로 인해 해당 캐릭터는 모든 전투 컨텐츠에서 육성 우선순위가 낮습니다.
    극 초반에 우울 시너지를 위해 채용하거나 애정으로 키우는 것이 아니면 육성을 권장하지 않습니다.
!!! warning "주의2"
    글로벌 버전에서는 에슈르의 성능이 개선된 채로 출시되었고 아직 사도들이 많이 출시되지 않아 어느정도 기용되는 편입니다.
에슈르는 출시 초기에도 성능이 나빴기 때문에 우울속성 9명을 채우기 위해서만 종종 사용되었다.

이후 우울 사도들이 많이 등장하며 금방 퇴출되었고, 업데이트가 없는 빈 기간에 상향을 받긴 했으나 전혀 성능이 나아지지 않아 다시 쓰이는 일은 없었다.

어사이드 출시 직후 어사이드 레벨을 올리면 그만큼 체급이 증가하는 점이 기대를 샀지만 그닥 경쟁이 되지 못하였고, 9우울 덱에서 어사이드 3성의 뎀증 효과를 지닌 토템으로써 억지로 쓰였다. 물몸인 후열 딜러가 2성으로 '직접 피해를 받을 경우' 효과를 가지고 있어 한때 '에슈르는 사실 후열 딜러였다'는 조롱성 밈이 이때 생겼다.

이후 어사이드를 가진 사도들이 점차 많아지고 인플레로 인해 완전한 상위호환 3성 효과들도 등장하면서 애정을 가진 교주들조차도 쓰기 힘들어하는 수준에 달했는데, 기존 어사이드 개편 소식 화면에 에슈르의 어사이드가 등장해 유의미한 상향이 있을 것이라고 추측되었다. {==하지만 1년이 넘는 기간 동안 이루어지지 않았다.==}

이후 빈 기간에 셰이디와 에슈르의 어사이드 및 스킬의 개편이 진행되었다. 하지만 글로벌 버전에서 변경된 사항을 그대로 가져왔고 애정을 가진 교주들이 억지로 침략에 쓸 수는 있는 정도로만 개선이 되었기 때문에, 쓰이지 않는 상황은 전혀 달라지지 않았다.

## 기본 스탯
{{ character_stat_card(
    'Ashur_profile.png',
    [
        'CharacterInfo/3star.png',
        'CharacterInfo/position/Common_UnitRace_Fairy.png',
        'CharacterInfo/position/PickUpPersonality_Gloomy.png',
        'CharacterInfo/position/Common_UnitClass_0001.png',
        'CharacterInfo/position/Common_UnitAttackMagic.png',
        'CharacterInfo/position/Common_PositionBack.png',
    ],
    ['3성', '요정', '우울', '딜러', '마법', '후열'],
    [
        ['Hp', 'HP', '18,010'],
        ['Sp', 'SP', '350'],
        ['AttackPhysic', '물리 공격력', '0'],
        ['AttackMagic', '마법 공격력', '2,718'],
        ['DefensePhysic', '물리 방어력', '2,556'],
        ['DefenseMagic', '마법 방어력', '2,560'],
        ['CriticalRate', '치명타', '3,068'],
        ['CriticalMult', '치명 피해', '3,074'],
        ['CriticalResist', '치명타 저항', '2,593'],
        ['CriticalMultResist', '치명 피해 저항', '2,437'],
    ],
) }}

## 스킬
{{ battle_skill_tabs([
    ['일반 공격', 'CharacterInfo/skill/AshurAttack.mp4', '일반공격 모습'],
    ['저학년 스킬 - 빵템피드', 'CharacterInfo/skill/AshurSkill1.mp4', '빵템피드 시전 모습'],
    ['고학년 스킬 - 빵테오', 'CharacterInfo/skill/AshurSkill2.mp4', '빵테오 시전 모습'],
], width=300, height=200) }}

{{ battle_skill_grid([
    battle_skill_slider_card(
        'ashur-admission',
        'CharacterInfo/skill/Icon_AdmissionSkill_Ashur.png',
        '빵템피드',
        '빵 <span class="red-text">6</span>개를 보내 <span class="red-text">공격력이 가장 높은 적</span>에게 범위 마법 피해를 입힌다.',
        [
            battle_skill_dynamic_stat(
                '총 마법 피해',
                [413, 435, 462, 495, 534, 578, 622, 671, 732, 792, 828, 864, 900],
            ),
        ],
        subtitle='저학년 스킬',
        summary='SP :<span class="lore-number-highlight"> 200</span> / <span class="lore-number-highlight"> 350</span> (<span class="lore-number-highlight"> +14/sec, +1/hit </span>)',
    ),
    battle_skill_slider_card(
        'ashur-graduate',
        'CharacterInfo/skill/Icon_GraduateSkill_Ashur.png',
        '빵테오',
        '거대한 케이크를 낙하시켜 <span class="red-text">가운데 있는 적</span>에게 범위 마법 피해를 입히고 <span class="red-text">기절</span>을 건다.<br>주변에 다른 적이 있다면 조각 케이크가 튕겨 마법 피해를 입힌다. 조각 케이크는 최대 <span class="red-text">3</span>명에게 튕긴다.<br><span class="red-text">기절: 행동불가 상태가 된다.</span>',
        [
            battle_skill_dynamic_stat(
                '마법 피해',
                [960, 1020, 1080, 1140, 1200, 1260, 1320, 1380, 1440, 1500, 1560, 1620, 1680],
                extras=[
                    battle_skill_inline_stat(
                        'PvP',
                        [634, 673, 713, 752, 792, 832, 871, 911, 950, 990, 1030, 1069, 1109],
                    ),
                ],
            ),
            battle_skill_text_stat(
                '기절 지속시간',
                '<span class="lore-number-highlight">4</span>초',
            ),
            battle_skill_dynamic_stat(
                '조각 케이크 마법 피해',
                [480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840],
                extras=[
                    battle_skill_inline_stat(
                        'PvP',
                        [317, 337, 356, 376, 396, 416, 436, 455, 475, 495, 515, 535, 554],
                    ),
                ],
            ),
        ],
        subtitle='고학년 스킬',
        summary='재사용 대기시간 <span class="lore-number-highlight">42초</span> (PvP:<span class="lore-number-highlight">24초</span>)',
    ),
    battle_skill_static_card(
        'CharacterInfo/skill/Magic_NormalAttack.png',
        '일반 공격',
        [
            ['기본', '화염 주문을 발사해 적에게 마법 피해를 입히고 화상을 건다.<br><span class="red-text">화상: 매 초 피해를 입는다.</span>', '마법 피해: <span class="lore-number-highlight">55</span>%<br>화상 지속시간: <span class="lore-number-highlight">2</span>초'],
            ['강화', '일정 확률로 불타는 빵을 발사해 적에게 마법 피해를 입히고 <span class="red-text">화상</span>을 건다.<br>공격한 적 일정 거리 뒤에 다른 적이 있다면 빵 조각이 튕겨 마법 피해를 입히고 <span class="red-text">화상</span>을 건다.<br>빵 조각은 최대 <span class="red-text">2</span>명에게 튕긴다.<br><span class="red-text">화상: 매 초 피해를 입는다.</span>', '마법 피해: <span class="lore-number-highlight">70</span>%<br>2타 마법 피해: <span class="lore-number-highlight">70</span>%<br>화상 지속시간: <span class="lore-number-highlight">2</span>초'],
        ],
    ),
]) }}

## 어사이드
{{ aside_panel(
    '궁극의 그리모어',
    '궁극의 마법을 정리한 마법서. 풀리지 않는 마법 난제들의 해석들이 담겨있다.',
    'CharacterInfo/AsideIcon_Ashur.png',
    [
        [
            'CharacterInfo/skill/Aside_Skill_Ashur_1.png',
            'CharacterInfo/1star.png',
            '마법책빵',
            '착용한 사도의 최대 HP, 마법 공격력, 치명타, 치명 피해가 증가한다.',
            [
                ['최대 HP 증가', '6', '%'],
                ['마법 공격력 증가', '6', '%'],
                ['치명타 증가', '6', '%'],
                ['치명 피해 증가', '6', '%'],
            ],
        ],
        [
            'CharacterInfo/skill/Aside_Skill_Ashur_2.png',
            'CharacterInfo/2star.png',
            '빵센디오',
            '<span class="red-text">저학년 스킬 사용 후</span> 일정 횟수 동안 일반 공격은 <span class="red-text">강화 공격</span>으로 시전된다.<br><span class="red-text">저학년 스킬 사용 시</span> 일정 시간 동안 <span class="red-text">주변 아군의 마법 피해량</span>을 증가시킨다.',
            [
                ['강화 공격 시전 횟수', '6', '회'],
                ['마법 피해량 증가', '50', '%'],
                ['마법 피해량 증가 지속시간', '8', '초']
            ],
        ],
        [
            'CharacterInfo/skill/Aside_Skill_Ashur_3.png',
            'CharacterInfo/3star.png',
            '빵빵한 브레드',
            '<span class="red-text">모든 아군의 적에게 주는 피해량</span>이 증가한다. 또한, 전체 보유 사도의 마법 공격력과 치명타가 증가한다.',
            [
                ['피해량 증가', '22.5', '%'],
                ['마법 공격력 증가', '3', '%'],
                ['치명타 증가', '3', '%'],
            ],
        ],
    ],
) }}

## 보드
+ 전투나 모험회에 사용하기에 부적합하므로 보드에서 주요 칸만 색칠하고 장비랭크만 여유될 때 후순위로 올리십시오.
+ 1관에는 우선순위가 높은 :stat-boardhp:{.medium-emoji}:stat-boardattack:{.medium-emoji}가 있습니다.
+ 2관에는 우선순위가 높은 :stat-boardattack:{.medium-emoji}:stat-boardcritdmg:{.medium-emoji}과 우선순위가 낮은:stat-boardmagicdef:{.medium-emoji}:stat-boardphysicdef:{.medium-emoji}가 있습니다. 체력이나 치명피해가 필요하시다면 왼쪽 길로 돌아가서 찍는 것을 추천합니다.
+ 3관에는 :stat-boardattack:{.medium-emoji}:stat-boardattack:{.medium-emoji}:stat-boardhp:{.medium-emoji}:stat-boardcritdmg:{.medium-emoji}:stat-boardmagicdef:{.medium-emoji}:stat-boardphysicdef:{.medium-emoji}가 있습니다.
=== "보드 1관"
    {{ image('CharacterInfo/board/board1.png', width=250, caption='에슈르 보드 1관') }}
=== "보드 2관"
    {{ image('CharacterInfo/board/board2.png', width=250, caption='에슈르 보드 2관') }}
=== "보드 3관"
    {{ image('CharacterInfo/board/board3.png', width=250, caption='에슈르 보드 3관') }}

## 전체 랭크 효과
캐릭터의 장비 랭크가 오를 때마다 모든 사도들의 해당 능력치가 수치만큼 오릅니다.

<div class="rank-list">
  {{ rank_row(2, stat_pill('DefensePhysic', '물리 방어력', '57') + stat_pill('DefenseMagic', '마법 방어력', '57')) }}
  {{ rank_row(3, stat_pill('CriticalRate', '치명타', '43') + stat_pill('CriticalMult', '치명 피해', '43')) }}
  {{ rank_row(4, stat_pill('CriticalResist', '치명타 저항', '43') + stat_pill('Hp', 'HP', '567')) }}
  {{ rank_row(5, stat_pill('CriticalMultResist', '치명 피해 저항', '43') + stat_pill('AttackPhysic', '물리 공격력', '28')) }}
  {{ rank_row(6, stat_pill('AttackMagic', '마법 공격력', '28') + stat_pill('DefensePhysic', '물리 방어력', '113')) }}
  {{ rank_row(7, stat_pill('DefenseMagic', '마법 방어력', '113') + stat_pill('CriticalRate', '치명타', '85')) }}
  {{ rank_row(8, stat_pill('CriticalMult', '치명 피해', '85') + stat_pill('CriticalResist', '치명타 저항', '85')) }}
  {{ rank_row(9, stat_pill('CriticalMultResist', '치명 피해 저항', '85') + stat_pill('Hp', 'HP', '1133')) }}
  {{ rank_row(10, stat_pill('AttackPhysic', '물리 공격력', '57') + stat_pill('AttackMagic', '마법 공격력', '57')) }}
  {{ rank_row(11, stat_pill('DefensePhysic', '물리 방어력', '128') + stat_pill('DefenseMagic', '마법 방어력', '128')) }}
</div>

## 리워크 이전 스킬
{{ battle_skill_tabs([
    ['일반 공격', 'CharacterInfo/skill/AshurAttack.mp4', '일반공격 모습'],
    ['저학년 스킬 - 빵템피드', 'CharacterInfo/skill/AshurSkill1.mp4', '빵템피드 시전 모습'],
    ['고학년 스킬 - 빵테오', 'CharacterInfo/skill/AshurSkill2.mp4', '빵테오 시전 모습'],
], width=500, height=300) }}

<div class="lore-grid">
  <!-- Column 1 -->
  <article class="lore-card">
    <div class="lore-header">
  <img src="{{ get_asset_path('CharacterInfo/skill/Icon_AdmissionSkill_Ashur.png') }}" alt="빵템피드" class="lore-avatar">
      <div>
        <div class="lore-subtitle">저학년 스킬</div>
        <div class="lore-title">빵템피드</div>
      </div>
    </div>
    <div class="lore-slider-wrapper">
      <div id="left-level" class="lore-level-box lore-lvl">Lv.1</div>
  <input id="left-slider" type="range" min="1" max="13" value="1" data-level-values='[421,443,471,504,544,589,634,684,746,807,844,881,918]'>
    </div>
    <div class="lore-stat-row">SP :<span class="lore-number-highlight">  200</span> / <span class="lore-number-highlight">  350</span> (<span class="lore-number-highlight"> +14/sec, +1/hit </span>)</div>
    <p class="lore-desc">빵 6개를 보내 폭발시켜 적들에게 범위 마법 피해를 입힌다.</p>
  <div class="lore-stat-row">총 마법 피해: <span id="left-damage" class="lore-number-highlight">421</span>%</div>
  </article>
  <!-- Column 2 -->
  <article class="lore-card">
    <div class="lore-header">
  <img src="{{ get_asset_path('CharacterInfo/skill/Icon_GraduateSkill_Ashur.png') }}" 
      alt="빵테오" class="lore-avatar">
      <div>
        <div class="lore-subtitle">고학년 스킬</div>
        <div class="lore-title">빵테오</div>
      </div>
    </div>
    <div class="lore-slider-wrapper">
      <div id="mid-level" class="lore-level-box lore-lvl">Lv.1</div>
      <input id="mid-slider" type="range" min="1" max="13" value="1"
        data-level-values='[670,710,760,810,870,940,1020,1100,1190,1290,1340,1390,1440]'
        data-level-cooldowns='[503,533,570,608,653,705,765,825,893,968,1005,1043,1080]'>
    </div>
    <div class="lore-stat-row">재사용 대기시간 <span class="lore-number-highlight">42초</span></div>
    <p class="lore-desc">거대한 빵을 낙하시켜 적들에게 범위 마법 피해를 입히고 <span class="red-text">기절</span>을 건다.<br><span class="red-text">기절: 행동불가 상태가 된다.</span></p>
  <div class="lore-stat-row">마법 피해: <span class="lore-number-highlight" id="mid-damage">670</span>% (PvP:<span class="lore-number-highlight" id="mid-cooldown-sec">503</span>%)<br>기절 지속시간: <span class="lore-number-highlight">4</span>초</div>
  </article>
    <!-- Column 3 -->
  <article class="lore-card">
    <div class="lore-header">
  <img src="{{ get_asset_path('CharacterInfo/skill/Magic_NormalAttack.png') }}" alt="일반 공격" class="lore-avatar">
      <div>
        <div class="lore-title lore-title--flush">일반 공격</div>
      </div>
    </div>
    <div class="battle-pill-group">
      <div class="battle-pill battle-pill--basic">기본</div>
    </div>
    <p class="lore-desc">화염 주문을 발사해 적에게 마법 피해를 입힌다.</p>
    <div class="lore-stat-row">마법 피해: <span class="lore-number-highlight">55</span>%</div>
    <div class="battle-pill-group">
      <div class="battle-pill battle-pill--basic">강화</div>
    </div>
      <p class="lore-desc">일정 확률로 강화된 화염 주문을 발사해 적에게 마법 피해를 입히고 <span class="red-text">화상</span>을 건다.<br><span class="red-text">화상: 매 초 피해를 입는다.</span></p>
      <div class="lore-stat-row">마법 피해: <span class="lore-number-highlight">70</span>%<br>화상 지속시간: <span class="lore-number-highlight">2</span>초</div>
  </article>
</div>

## 리워크 이전 어사이드
{{ aside_panel(
    '궁극의 그리모어',
    '궁극의 마법을 정리한 마법서. 풀리지 않는 마법 난제들의 해석들이 담겨있다.',
    'CharacterInfo/AsideIcon_Ashur.png',
    [
        [
            'CharacterInfo/skill/Aside_Skill_Ashur_1.png',
            'CharacterInfo/1star.png',
            '마법책빵',
            '착용한 사도의 최대 HP, 마법 공격력, 치명타, 치명 피해가 증가한다.',
            [
                ['최대 HP 증가', '6', '%'],
                ['마법 공격력 증가', '6', '%'],
                ['치명타 증가', '6', '%'],
                ['치명 피해 증가', '6', '%'],
            ],
        ],
        [
            'CharacterInfo/skill/Aside_Skill_Ashur_2.png',
            'CharacterInfo/2star.png',
            '빵센디오',
            '기본 공격 적중 시 HP를 회복한다.<br><span class="red-text">직접 피해</span>를 받으면 고학년 스킬의 재사용 대기 시간이 줄어든다.<br><span class="red-text">직접 피해: 상태이상 피해, 반사 피해, 저주 피해를 제외한 직접 공격에 의한 피해</span>',
            [
                ['HP 회복', '3', '%'],
                ['재사용 대기 시간 감소', '1', '초'],
            ],
        ],
        [
            'CharacterInfo/skill/Aside_Skill_Ashur_3.png',
            'CharacterInfo/3star.png',
            '빵빵한 브레드',
            '모든 아군이 적에게 주는 피해량이 증가한다. 또한, 전체 사도의 마법 공격력과 치명타가 증가한다.',
            [
                ['피해량 증가', '10', '%'],
                ['마법 공격력 증가', '3', '%'],
                ['치명타 증가', '3', '%'],
            ],
        ],
    ],
) }}