---
title: 캐릭터 정보 - 전투
publish: true
icon: material/sword-cross
description: 에슈르의 기본 스탯, 스킬 영상, 어사이드 효과를 정리한 전투 정보 페이지입니다.
subtitle: 스탯, 스킬, 어사이드
tags:
  - 캐릭터정보
---

# 캐릭터 정보 - 전투
!!! warning "주의"
    게임 내 성능 인플레이션으로 인해 해당 캐릭터는 모든 전투 컨텐츠에서 육성 우선순위가 낮습니다.<br>
    극 초반에 우울 시너지를 위해 채용하거나 애정으로 키우는 것이 아니면 육성을 권장하지 않습니다.

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

=== "일반 공격"
    {{ video('CharacterInfo/skill/AshurAttack.mp4', caption='일반공격 모습', width=500, height=300) }}

=== "저학년 스킬 - 빵템피드"
    {{ video('CharacterInfo/skill/AshurSkill1.mp4', caption='빵템피드 시전 모습', width=500, height=300) }}

=== "고학년 스킬 - 빵테오"
    {{ video('CharacterInfo/skill/AshurSkill2.mp4', caption='빵테오 시전 모습', width=500, height=300) }}

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
