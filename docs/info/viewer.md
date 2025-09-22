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
![Image title](https://vitamink1.github.io/mkdocs-test/assets/ashurdesc_1.png){width="500" height="300"}
/// caption
에슈르 기본 사복 설명
///

=== "스탠딩"
    <script src="https://vitamink1.github.io/mkdocs-test/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/mkdocs-test/css/spine-player.css" />
    <div id="player-container1" style="width: 360px; height: 450px; margin:0 auto;"></div>
    <script>
    new spine.SpinePlayer("player-container1", {
        skelUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/standing/Ashur.skel",
        atlasUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/standing/Ashur.atlas",
        backgroundColor: "#ffffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        showLoading: false,
        animation: "Idle_1",
    });
    </script>

=== "전투"
    <script src="https://vitamink1.github.io/mkdocs-test/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/mkdocs-test/css/spine-player.css" />
    <div id="player-container2" style="width: 360px; height: 450px; margin:0 auto;"></div>
    <script>
    new spine.SpinePlayer("player-container2", {
        skelUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/battle/Ashur.skel",
        atlasUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/battle/Ashur.atlas",
        backgroundColor: "#ffffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        showLoading: false,
        animation: "Idle",
    });
    </script>

<br>
<br>

## 아이스크림 메이커
![Image title](https://vitamink1.github.io/mkdocs-test/assets/ashurdesc_2.png){width="500" height="300"}
/// caption
에슈르 아이스크림 메이커 사복 설명
///

=== "스탠딩"
    <script src="https://vitamink1.github.io/mkdocs-test/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/mkdocs-test/css/spine-player.css" />
    <div id="player-container3" style="width: 360px; height: 450px; margin:0 auto;"></div>
    <script>
    new spine.SpinePlayer("player-container3", {
        skelUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/standingskin1/AshurSkin1.skel",
        atlasUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/standingskin1/AshurSkin1.atlas",
        backgroundColor: "#ffffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        showLoading: false,
        animation: "Idle_1",
    });
    </script>

=== "전투"
    <script src="https://vitamink1.github.io/mkdocs-test/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/mkdocs-test/css/spine-player.css" />
    <div id="player-container4" style="width: 360px; height: 450px; margin:0 auto;"></div>
    <script>
    new spine.SpinePlayer("player-container4", {
        skelUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/battleskin1/AshurSkin1.skel",
        atlasUrl: "https://vitamink1.github.io/mkdocs-test/assets/spine/battleskin1/AshurSkin1.atlas",
        backgroundColor: "#ffffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        showLoading: false,
        animation: "Idle",
    });
    </script>

<br>
<br>