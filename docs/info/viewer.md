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
=== "기본 사복"
    ![Image title](https://vitamink1.github.io/ashur-note/assets/ashurdesc_2.png){width="500" height="300"}
    /// caption
    에슈르 기본 사복 설명
    ///

=== "아이스크림 메이커"
    ![Image title](https://vitamink1.github.io/ashur-note/assets/ashurdesc_1.png){width="500" height="300"}
    /// caption
    에슈르 아이스크림 메이커 사복 설명
    ///

=== "평온한 온천 여행"
    ![Image title](https://vitamink1.github.io/ashur-note/assets/ashurdesc_3.png){width="500" height="300"}
    /// caption
    에슈르 평온한 온천 여행 사복 설명
    ///

## 스탠딩
=== "기본 사복"
    <script src="https://vitamink1.github.io/ashur-note/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/ashur-note/css/spine-player.css" />
    <div id="player-container1" style="width: 360px; height: 450px; margin:0 auto;"></div>
    <script>
    new spine.SpinePlayer("player-container1", {
    skelUrl: "https://vitamink1.github.io/ashur-note/assets/spine/standing/Ashur.skel",
    atlasUrl: "https://vitamink1.github.io/ashur-note/assets/spine/standing/Ashur.atlas",
        backgroundColor: "#ffffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        showLoading: false,
        animation: "Idle_1",
    });
    </script>

=== "아이스크림 메이커"
    <script src="https://vitamink1.github.io/ashur-note/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/ashur-note/css/spine-player.css" />
    <div id="player-container3" style="width: 360px; height: 450px; margin:0 auto;"></div>
    <script>
    new spine.SpinePlayer("player-container3", {
    skelUrl: "https://vitamink1.github.io/ashur-note/assets/spine/standingskin1/AshurSkin1.skel",
    atlasUrl: "https://vitamink1.github.io/ashur-note/assets/spine/standingskin1/AshurSkin1.atlas",
        backgroundColor: "#ffffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        showLoading: false,
        animation: "Idle_1",
    });
    </script>

=== "평온한 온천 여행"
    <script src="https://vitamink1.github.io/ashur-note/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/ashur-note/css/spine-player.css" />
    <div id="player-container5" style="width: 360px; height: 450px; margin:0 auto;"></div>
    <script>
    new spine.SpinePlayer("player-container5", {
    skelUrl: "https://vitamink1.github.io/ashur-note/assets/spine/standingskin2/AshurSkin2.skel",
    atlasUrl: "https://vitamink1.github.io/ashur-note/assets/spine/standingskin2/AshurSkin2.atlas",
        backgroundColor: "#ffffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        showLoading: false,
        animation: "Idle_1",
    });
    </script>


<br>

## 전투
=== "기본 사복"
    <script src="https://vitamink1.github.io/ashur-note/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/ashur-note/css/spine-player.css" />
    <div id="player-container2" style="width: 360px; height: 450px; margin:0 auto;"></div>
    <script>
    new spine.SpinePlayer("player-container2", {
    skelUrl: "https://vitamink1.github.io/ashur-note/assets/spine/battle/Ashur.skel",
    atlasUrl: "https://vitamink1.github.io/ashur-note/assets/spine/battle/Ashur.atlas",
        backgroundColor: "#ffffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        showLoading: false,
        animation: "Idle",
    });
    </script>

=== "아이스크림 메이커"
    <script src="https://vitamink1.github.io/ashur-note/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/ashur-note/css/spine-player.css" />
    <div id="player-container4" style="width: 360px; height: 450px; margin:0 auto;"></div>
    <script>
    new spine.SpinePlayer("player-container4", {
    skelUrl: "https://vitamink1.github.io/ashur-note/assets/spine/battleskin1/AshurSkin1.skel",
    atlasUrl: "https://vitamink1.github.io/ashur-note/assets/spine/battleskin1/AshurSkin1.atlas",
        backgroundColor: "#ffffffff",
        alpha: false,
        preserveDrawingBuffer:true,
        skin: "Normal",
        showLoading: false,
        animation: "Idle",
    });
    </script>

=== "평온한 온천 여행"
    <script src="https://vitamink1.github.io/ashur-note/javascripts/spine-player.min.js"></script>
    <link rel="stylesheet" href="https://vitamink1.github.io/ashur-note/css/spine-player.css" />
    <div id="player-container6" style="width: 360px; height: 450px; margin:0 auto;"></div>
    <script>
    new spine.SpinePlayer("player-container6", {
    skelUrl: "https://vitamink1.github.io/ashur-note/assets/spine/battleskin2/AshurSkin2.skel",
    atlasUrl: "https://vitamink1.github.io/ashur-note/assets/spine/battleskin2/AshurSkin2.atlas",
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