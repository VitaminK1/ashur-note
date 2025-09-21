---
title: 캐릭터 정보 - 옷장
publish: true
icon: fontawesome/solid/shirt
subtitle: 스파인 뷰어
tags:
  - 캐릭터정보
---

# 캐릭터 정보 - 옷장

## 기본 사복

=== "스탠딩"
    <script src="https://vitamink1.github.io/mkdocs-test/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/mkdocs-test/css/spine-player.css" />
    <div id="player-container" style="width: 240px; height: 300px;"></div>
    <script>
    new spine.SpinePlayer("player-container", {
        skelUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/standing/Ashur.skel",
        atlasUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/standing/Ashur.atlas",
        backgroundColor: "#ffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        animation: "Idle_1",
        showLoading: false
    });
    </script>

=== "전투"
    <script src="https://vitamink1.github.io/mkdocs-test/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/mkdocs-test/css/spine-player.css" />
    <div id="player-container1" style="width: 240px; height: 300px;"></div>
    <script>
    // Load Spine data from the assets folder (docs/assets/spine/standing)
    new spine.SpinePlayer("player-container1", {
        skelUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/battle/Ashur.skel",
        atlasUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/battle/Ashur.atlas",
        backgroundColor: "#ffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        animation: "Idle",
        showLoading: false
    });
    </script>

<br>
<br>

## 아이스크림 메이커