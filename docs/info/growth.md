---
title: 캐릭터 정보 - 육성
publish: true
icon: material/notebook-edit
description:
subtitle: 보드, 선호도, 모험회, 랭크효과
tags:
  - 캐릭터정보
---

# 캐릭터 정보 - 육성

## 보드
+ 1관에는 우선순위가 높은 :stat-boardhp:{.medium-emoji}:stat-boardattack:{.medium-emoji}가 있습니다. 오른쪽 길로 가면서 둘 다 찍는 것을 추천합니다.
+ 2관에는 우선순위가 높은 :stat-boardattack:{.medium-emoji}:stat-boardcritdmg:{.medium-emoji}과 우선순위가 낮은:stat-boardmagicdef:{.medium-emoji}:stat-boardphysicdef:{.medium-emoji}가 있습니다. 체력이나 치명피해가 필요하시다면 왼쪽 길로 돌아가서 찍는 것을 추천합니다.
+ 3관에는 :stat-boardattack:{.medium-emoji}:stat-boardattack:{.medium-emoji}:stat-boardhp:{.medium-emoji}:stat-boardcritdmg:{.medium-emoji}:stat-boardmagicdef:{.medium-emoji}:stat-boardphysicdef:{.medium-emoji}가 있습니다.

=== "보드 1관"
    {{ image('CharacterInfo/board/board1.png', width=250, caption='에슈르 보드 1관') }}

=== "보드 2관"
    {{ image('CharacterInfo/board/board2.png', width=250, caption='에슈르 보드 2관') }}

=== "보드 3관"
    {{ image('CharacterInfo/board/board3.png', width=250, caption='에슈르 보드 3관') }}
<br>
<br>

## 선호도
좋아하는 음식들의 등급이 모두 낮으며, 싫어하는 음식들의 등급이 모두 높아 애정레벨 육성 난이도가 높습니다.<br>
가성비 등을 고려했을 때, 에슈르가 특히 좋아하는 ```UFC 야채 튀김```을 권장합니다.

{{ preference_table([
    ['hate', '싫어함', [
        ['Blue', 22],
        ['Purple', 13],
        ['Purple', 59],
        ['Gold', 63],
    ]],
    ['like', '좋아함', [
        ['Gray', 4],
        ['Gray', 28],
        ['Green', 43],
    ]],
    ['like', '좋아함(공통)', [
        ['Blue', 33],
        ['Blue', 34],
        ['Blue', 35],
        ['Blue', 36],
        ['Blue', 37],
        ['Purple', 31],
        ['Purple', 32],
    ]],
    ['love', '특히 좋아함', [
        ['Green', 42],
    ]],
    ['good', '그럭저럭', '이외의 모든 음식들'],
]) }}
<br>
<br>

## 친밀도
음식의 등급과 캐릭터의 선호도에 따라 친밀도 증가량이 달라집니다.<br>
이후 대화 선택지에 따라 선호도가 추가로 ```+1~+3``` 증가합니다.

{{ preference_value_table(
    [
        ['common/itemslot/ItemSlot_Gray.png', '일반'],
        ['common/itemslot/ItemSlot_CardPet_2.png', '고급'],
        ['common/itemslot/ItemSlot_CardPet_3.png', '희귀'],
        ['common/itemslot/ItemSlot_CardPet_4.png', '전설'],
        ['common/itemslot/ItemSlot_Gold.png', '개쩜'],
    ],
    [
        ['hate', '싫어함', ['15', '20', '25', '30', '35']],
        ['good', '그럭저럭', ['20', '30', '40', '50', '60']],
        ['like', '좋아함', ['25', '40', '55', '70', '80']],
        ['love', '특히 좋아함', ['-', '46', '64', '82', '100']],
    ],
) }}
<br>
<br>


## 모험회
모험회는 한 사도가 1-2개의 재료를 담당하도록 분배하는 것이 좋습니다.<br>
에슈르의 메인 기술은 손기술은 '혼모노의 증표' 아이템을 위한 '피규어 채색' 태스크에 중요하지만 해당 테스크에는 림(혼돈)이 더 적합합니다.<br> 
따라서 미보유 사도가 많은 경우가 아니라면 추천하지 않습니다.

<div class="rel-panel">
  <div class="rel-panel-inner">
    <p class="rel-title">에슈르의 모험회 스킬</p>
    <div class="rel-grid">
      {{ adv_skill(10, '손기술', True) }}
      {{ adv_skill(8, '암산') }}
      {{ adv_skill(1, '육체노동') }}
      {{ adv_skill(31, '추진력') }}
      {{ adv_skill(32, '직감') }}
    </div>
  </div>
</div>
<br>

## 전체 랭크 효과
캐릭터의 장비 랭크가 오를 때마다 모든 사도들의 해당 능력치가 수치만큼 오릅니다.<br>
<br>
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
<br>
<br>
