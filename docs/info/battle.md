---
title: 캐릭터 정보 - 전투
publish: true
icon: material/battery-medium
description:
subtitle: 스탯, 스킬, 어사이드
tags:
  - 캐릭터 정보
---

# 캐릭터 정보 - 전투

## 기본 스탯

## 스킬
<div class="lore-grid">
  <!-- Column 1 -->
  <article class="lore-card">
    <div class="lore-header">
  <img src="../assets/characterinfo/skill/Icon_AdmissionSkill_Ashur.png" alt="빵템피드" class="lore-avatar">
      <div>
        <div class="lore-subtitle">저학년 스킬</div>
        <div class="lore-title">빵템피드</div>
      </div>
    </div>
    <div class="lore-slider-wrapper">
      <div id="left-level" class="lore-level-box lore-lvl">Lv.1</div>
  <input id="left-slider" type="range" min="1" max="13" value="1" data-level-values='[421,443,471,504,544,589,634,684,746,807,844,881,918]'>
    </div>
    <div class="lore-stat-row">SP :<span class="lore-number-highlight">  200</span></span> / <span class="lore-number-highlight">  350</span> (<span class="lore-number-highlight"> +14/sec, +1/hit </span>)</div>
    <p class="lore-desc">빵 6개를 보내 폭발시켜 적들에게 범위 마법 피해를 입힌다.</p>
  <div class="lore-stat-row">총 마법 피해: <span id="left-damage" class="lore-number-highlight">421</span>%</div>
  </article>

  <!-- Column 2 -->
  <article class="lore-card">
    <div class="lore-header">
      <img src="../assets/characterinfo/skill/Icon_GraduateSkill_Ashur.png" 
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
    <p class="lore-desc">거대한 빵을 낙하시켜 적들에게 범위 마법 피해를 입히고 <span style="color:#ff6b6b">기절</span>을 건다.<br><span style="color:#ff6b6b">기절: 행동불가 상태가 된다.</span></p>
  <div class="lore-stat-row">마법 피해: <span class="lore-number-highlight" id="mid-damage">670</span>% (PvP:<span class="lore-number-highlight" id="mid-cooldown-sec">503</span>%)<br>기절 지속시간: <span class="lore-number-highlight">4</span>초</div>
  </article>

  <!-- Column 3 -->
  <article class="lore-card">
    <div class="lore-header">
      <img src="../assets/characterinfo/skill/Magic_NormalAttack.png" alt="일반 공격" class="lore-avatar">
      <div>
        <div class="lore-title" style="margin-top:0">일반 공격</div>
      </div>
    </div>
    <div style="margin-top:12px;margin-bottom:6px">
      <div style="display:inline-block;background:#b8ff5d;color:#052006;padding:2px 12px;border-radius:18px">기본</div>
    </div>
    <p class="lore-desc">화염 주문을 발사해 적에게 마법 피해를 입힌다.</p>
    <div class="lore-stat-row">마법 피해: <span class="lore-number-highlight">55</span>%</div>
    <div style="margin-top:12px;margin-bottom:6px">
      <div style="display:inline-block;background:#b8ff5d;color:#052006;padding:2px 12px;border-radius:18px">강화</div>
    </div>
      <p class="lore-desc">일정 확률로 강화된 화염 주문을 발사해 적에게 마법 피해를 입히고 <span style="color:#ff6b6b;">화상</span>을 건다.<br><span style="color:#ff6b6b">화상: 매 초 피해를 입는다.</span></p>
      <div class="lore-stat-row">마법 피해: <span class="lore-number-highlight">70</span>%<br>화상 지속시간: <span class="lore-number-highlight">2</span>초</div>
    </div>
  </article>
</div>
<br>
<br>

## 어사이드

<div class="battle-panel">
  <div class="battle-header">
    <img class="battle-header-img" style="margin-left: auto; margin-right: auto; display: block;" src="https://vitamink1.github.io/mkdocs-test/assets/characterinfo/AsideIcon_Ashur.png" alt="portrait"/>
    <div style="margin-left: 10px; width: 100%">
      <h2 class="battle-title">궁극의 그리모어</h2>
      <p style="margin:0 0 10px 0;">궁극의 마법을 정리한 마법서. 풀리지 않는 마법 난제들의 해석들이 담겨있다.</p>
    </div>
  </div>

  <div class="skill-list" style="margin-top:12px;">
    <div class="skill-card">
      <img class="icon" src="../assets/characterinfo/skill/Aside_Skill_Ashur_1.png" alt="아이콘"/>
      <div class="meta">
        <div style="display:flex;align-items:center;gap:8px;">
          <img class="badge-stars" src="../assets/characterinfo/1star.png" alt="아이콘"/>
          <div class="skill-name">마법책빵</div>
        </div>
        <div class="skill-desc">
        착용한 사도의 최대 HP, 마법 공격력, 치명타, 치명 피해가 증가한다.
        </div>
        <div class="skill-stats">
        최대 HP 증가 : <span class="skill-percent">6</span>%<br/>
        마법 공격력 증가 : <span class="skill-percent">6</span>%<br/>
        치명타 증가 : <span class="skill-percent">6</span>%<br/>
        치명 피해 증가 : <span class="skill-percent">6</span>%</div>
      </div>
    </div>
    <div class="skill-card">
      <img class="icon" src="../assets/characterinfo/skill/Aside_Skill_Ashur_2.png" alt="아이콘"/>
      <div class="meta">
        <div style="display:flex;align-items:center;gap:8px;">
          <img class="badge-stars" src="../assets/characterinfo/2star.png" alt="아이콘"/>
          <div class="skill-name">빵센디오</div>
        </div>
        <div class="skill-desc">
        기본 공격 적중 시 HP를 회복한다.<br/>
        <span class="red-text">직접 피해</span>를 받으면 고학년 스킬의 재사용 대기 시간이 줄어든다.<br/>
        <span class="red-text">직접 피해: 상태이상 피해, 반사 피해, 저주 피해를 제외한 직접 공격에 의한 피해</span><br/>
        </div>
        <div class="skill-stats">
        HP 회복 : <span class="skill-percent">3</span>%<br/>
        재사용 대기 시간 감소 : <span class="skill-percent">1</span>초
        </div>
      </div>
    </div>
    <div class="skill-card">
      <img class="icon" src="../assets/characterinfo/skill/Aside_Skill_Ashur_3.png" alt="아이콘"/>
      <div class="meta">
        <div style="display:flex;align-items:center;gap:8px;">
          <img class="badge-stars" src="../assets/characterinfo/3star.png" alt="아이콘"/>
          <div class="skill-name">빵빵한 브레드</div>
        </div>
        <div class="skill-desc">
        모든 아군이 적에게 주는 피해량이 증가한다. 또한, 전체 사도의 마법 공격력과 치명타가 증가한다.</div>
        <div class="skill-stats">
        피해량 증가: <span class="skill-percent">10</span>%<br/>
        마법 공격력 증가: <span class="skill-percent">3</span>%<br/>
        치명타 증가: <span class="skill-percent">3</span>%</div>
        </div>
      </div>
    </div>
  </div>
</div>




<br>
<br>

