---
title: 교주의 기록
publish: true
icon: material/file-tree
description: Styled record cards for the '교주의 기록' character entries. Scoped CSS with kj- prefix.
tags:
  - HTML
  - CSS
---

<div class="kj-record-wrap">
  <style>
  /* Scoped styles for the 교주의 기록 cards - kj- prefix to avoid collisions */
  .kj-record-wrap { color:#333; }
  .kj-record { max-width:920px; margin:18px auto; background:#dff0b8; border-radius:8px; padding:18px; box-shadow:0 0 0 1px rgba(0,0,0,0.03) inset; border:1px solid rgba(0,0,0,0.06); }
  .kj-record .kj-title { display:inline-block; background:#9fcf55; color:#0b2611; font-weight:800; padding:8px 14px; border-radius:8px; box-shadow:0 2px 0 rgba(0,0,0,0.06); margin-bottom:14px; font-size:1.05rem; }

  .kj-cards { display:flex; flex-direction:column; gap:12px; margin-top:6px; }
  .kj-card { background:#fbf5ea; border-radius:8px; padding:14px; border:2px solid rgba(0,0,0,0.06); box-shadow:0 2px 0 rgba(0,0,0,0.04); }
  .kj-card .kj-level { font-weight:700; color:#5a4b2a; margin-bottom:8px; font-size:0.98rem; }
  .kj-card .kj-text { color:#3b3b3b; line-height:1.6; white-space:pre-wrap; font-size:0.98rem; }

  /* Decorative inner border like the sample */
  .kj-card-inner { border:1px solid rgba(0,0,0,0.04); padding:10px; border-radius:6px; }

  /* Accent left bar on each card */
  .kj-card { position:relative; }
  .kj-card::after { content:""; position:absolute; left:12px; top:12px; bottom:12px; width:4px; background:linear-gradient(#78b33b,#9fd85a); border-radius:3px; opacity:0.98; }
  .kj-card .kj-level, .kj-card .kj-text { margin-left:26px; }

  /* Responsive tweaks */
  @media (max-width:680px) {
    .kj-record { margin:12px; padding:12px; }
    .kj-card { padding:12px; }
    .kj-card::after { left:10px; }
    .kj-card .kj-level, .kj-card .kj-text { margin-left:22px; }
  }
  </style>

  <div class="kj-record">
    <div class="kj-title">교주의 기록</div>
    <div class="kj-cards">
      <div class="kj-card">
        <div class="kj-card-inner">
          <div class="kj-level">[ 친밀 레벨 3 ]</div>
          <div class="kj-text">에슈르는 '자칭' 요정 마법의 최고 권위자다. 그래서 마법학교를 세우고 스스로 학교장이 됐... 지만, 아무래도 학교 운영비를 충당하는 게 여간 힘든 일이 아닌 것 같다.</div>
        </div>
      </div>
      <div class="kj-card">
        <div class="kj-card-inner">
          <div class="kj-level">[ 친밀 레벨 6 ]</div>
          <div class="kj-text">에슈르는 마법에 대한 자부심이 굉장히 강한 것 같다. 다른 요정들은 에슈르가 마법보다 제빵에 재능이 더 많다고 심심찮게 말하는데 에슈르는 그런 말을 들을 때마다 굉장히 걱정적으로 변한다.</div>
        </div>
      </div>
      <div class="kj-card">
        <div class="kj-card-inner">
          <div class="kj-level">[ 친밀 레벨 9 ]</div>
          <div class="kj-text">에슈르가 만들었다는 빵을 먹어봤는데 정말 놀랍다. 내가 평소 먹어보던 그린 빵의 맛이 아니다. 물론 내가 살던 차원이 아니라 당연히 그렇겠지만...</div>
        </div>
      </div>
      <div class="kj-card">
        <div class="kj-card-inner">
          <div class="kj-level">[ 친밀 레벨 12 ]</div>
          <div class="kj-text">에슈르가 마법보다 제빵에 재능이 있다는 말이 한번에 이해되는 맛이었다. 확실히 이것도 재능인데 에슈르가 굳이 그것에 부끄러워할 필요가 있을까 싶기도 하다.</div>
        </div>
      </div>
      <div class="kj-card">
        <div class="kj-card-inner">
          <div class="kj-level">[ 친밀 레벨 15 ]</div>
          <div class="kj-text">에슈르는 '마법의 권위자'가 되고 싶다는 꿈이 있다고 한다. 다만 엘리아스에서 마법은 너무 흔한 공기 같은 것이라 다른 마법을 그렇게 중요하게 생각하지 않는 것 같아 아쉽다.</div>
        </div>
      </div>
      <div class="kj-card">
        <div class="kj-card-inner">
          <div class="kj-level">[ 친밀 레벨 18 ]</div>
          <div class="kj-text">에슈르가 나에게 잘 대해주는 이유는 내가 마법이 생소한 외지인이라서가 아닐까? 나는 아직도 에슈르가 간단한 마법만 보여줘도 신기해한다. 상식적으로 신기해할 수 밖에 없으니...</div>
        </div>
      </div>
      <div class="kj-card">
        <div class="kj-card-inner">
          <div class="kj-level">[ 친밀 레벨 21 ]</div>
          <div class="kj-text">제빵과 마법을 합쳐보면 뭔가 나올 것 같지 않냐고 에슈르에게 제안해본 적이 있다. 에슈르가 주먹을 꽉 쥐었을 때, 섬뜩한 살기가 느껴져 내 말을 취소했다. 그래도 내 말이 신경쓰였는지 그날 밤부터 빵에 대고 무언가 연습을 하는 모습이 종종 보인다. 나중에 어떤 결과가 나올지 궁금하다.</div>
        </div>
      </div>

    </div>
  </div>
</div>

# 아이템
