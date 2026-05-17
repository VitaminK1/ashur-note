---
title: 캐릭터 정보 - 기록
publish: true
icon: fontawesome/solid/shirt
subtitle: 모션, 뽑기연출, 대사
tags:
  - 캐릭터정보
---

# 캐릭터 정보 - 기록
{{ section_nav() }}
## 사복 설명
{{ tabs([
    ['기본 사복', image('ashurdesc_2.png', height=300, caption='에슈르 기본 사복 설명')],
    ['아이스크림 메이커', image('ashurdesc_1.png', height=300, caption='에슈르 아이스크림 메이커 사복 설명')],
    ['평온한 온천 여행', image('ashurdesc_3.png', height=300, caption='에슈르 평온한 온천 여행 사복 설명')],
]) }}
## 스탠딩 모션
{{ tabs([
    ['기본 사복', spine_viewer('player-container1', 'spine/standing/Ashur.skel', 'spine/standing/Ashur.atlas', width=360, height=450, background='#ffffffff', animation='Idle_1', show_controls=True, style='margin:0 auto')],
    ['아이스크림 메이커', spine_viewer('player-container3', 'spine/standingskin1/AshurSkin1.skel', 'spine/standingskin1/AshurSkin1.atlas', width=360, height=450, background='#ffffffff', animation='Idle_1', show_controls=True, style='margin:0 auto')],
    ['평온한 온천 여행', spine_viewer('player-container5', 'spine/standingskin2/AshurSkin2.skel', 'spine/standingskin2/AshurSkin2.atlas', width=360, height=450, background='#ffffffff', animation='Idle_1', show_controls=True, style='margin:0 auto')],
]) }}
## 전투 모션
{{ tabs([
    ['기본 사복', spine_viewer('player-container2', 'spine/battle/Ashur.skel', 'spine/battle/Ashur.atlas', width=360, height=450, background='#ffffffff', animation='Idle', show_controls=True, style='margin:0 auto')],
    ['아이스크림 메이커', spine_viewer('player-container4', 'spine/battleskin1/AshurSkin1.skel', 'spine/battleskin1/AshurSkin1.atlas', width=360, height=450, background='#ffffffff', animation='Idle', show_controls=True, style='margin:0 auto')],
    ['평온한 온천 여행', spine_viewer('player-container6', 'spine/battleskin2/AshurSkin2.skel', 'spine/battleskin2/AshurSkin2.atlas', width=360, height=450, background='#ffffffff', animation='Idle', show_controls=True, style='margin:0 auto')],
]) }}
## 뽑기 연출
=== "오픈 당시"
    {{ video('others/gacha1.mp4', caption='에슈르 뽑기 연출 (오픈 당시)', width=500, height=300) }}
=== "개편 후"
    {{ video('others/gacha2.mp4', caption='에슈르 뽑기 연출 (개편 후)', width=500, height=300) }}
## 대사 (한국어)
{{ intimacy_table('친밀도', [
    ['레벨 1', [
        ("빵집 아줌마가 아니라 '마법사님'이라고 부르라고!", 'voice_kr/Voice_Ashur_Affinity1_1.mp3'),
        ('마법의 체계 논문도 읽어보지 않고 나랑 말을 섞겠다는 거야?', 'voice_kr/Voice_Ashur_Affinity1_2.mp3'),
        ('식사 시간에만 찾지 말고 모험할 때도 좀 불러달란 말이야!', 'voice_kr/Voice_Ashur_Affinity1_3.mp3'),
    ]],
    ['레벨 2', ('뭐? 물빵을 달라고? 그런건 다른데 가서 찾아!', 'voice_kr/Voice_Ashur_Affinity2.mp3')],
    ['레벨 3', ('흐흑⋯ 또 여왕님이 케잌 300개를 주문하셨어⋯', 'voice_kr/Voice_Ashur_Affinity3.mp3')],
    ['레벨 4', ('내 마법 강의실은 조리대 앞이야! 언제든 찾아와!', 'voice_kr/Voice_Ashur_Affinity4.mp3')],
    ['레벨 5', ('마법의 기본은 중력분이나 강력분이나…가 아니잖아!', 'voice_kr/Voice_Ashur_Affinity5.mp3')],
    ['레벨 6', ('제빵의 기본은 중력술이냐 강령술이냐…가 아니잖아!', 'voice_kr/Voice_Ashur_Affinity6.mp3')],
    ['레벨 7', ('아무도 내 마법 이론서를 읽어주지 않아… 교주님이라도 읽을래요?', 'voice_kr/Voice_Ashur_Affinity7.mp3')],
]) }}
{{ intimacy_tabs([
    ['기본 사복', '상호작용', [
        ['볼 당기기 1', ('앗! 아프잖아욧!!', 'voice_kr/Voice_Ashur_Touch1.mp3')],
        ['볼 당기기 2', ('안 그래도 힘든 일 많아요!', 'voice_kr/Voice_Ashur_Touch1_1.mp3')],
        ['볼 당기기 3', ('으아아.. 결국 이 고통에도 익숙해져 버렸어...', 'voice_kr/Voice_Ashur_Touch1_2.mp3')],
        ['간지럽히기 1', ('으히~ 흐흐흐⋯', 'voice_kr/Voice_Ashur_TickleStart1.mp3')],
        ['간지럽히기 2', ('악 간지럿, 간지러잇! 흐흐흐⋯', 'voice_kr/Voice_Ashur_TickleDuring1.mp3')],
        ['꿀밤 때리기', ('어쭈! / 으악, 이제 빵 안 나눠 드릴 거에요!', 'voice_kr/Voice_Ashur_DutchRubEnd1.mp3', 'voice_kr/Voice_Ashur_DutchRubEnd2.mp3')],
        ['쓰다듬기 1', ('살기 힘들어요⋯', 'voice_kr/Voice_Ashur_Touch2.mp3')],
        ['쓰다듬기 2', ('교주님은⋯ 흑, 제 맘 아시죠?', 'voice_kr/Voice_Ashur_Touch2_1.mp3')],
        ['쓰다듬기 3', ('그래도⋯ 조금 편해졌어요.', 'voice_kr/Voice_Ashur_Touch2_2.mp3')],
    ], [
        '꿀밤 때리기 상호작용 해금 조건 : 친밀레벨 5 이상',
        '쓰다듬기 2 대사 해금 조건 : 친밀레벨 10 이상',
        '쓰다듬기 3 대사 해금 조건 : 친밀레벨 20 이상',
    ]],
    ['아이스크림 메이커', '상호작용', [
        ['볼 당기기 1', ('물장구로 복수할거에요⋯!', 'voice_kr/Voice_Ashur_Touch1_Skin1.mp3')],
        ['볼 당기기 2', ('썬크림 다 지워져요!', 'voice_kr/Voice_Ashur_Touch1_1_Skin1.mp3')],
        ['볼 당기기 3', ('기분 좋으니까.. 봐드리는 거에요!', 'voice_kr/Voice_Ashur_Touch1_2_Skin1.mp3')],
        ['간지럽히기 1', ('으히~ 흐흐흐⋯', 'voice_kr/Voice_Ashur_TickleStart1.mp3')],
        ['간지럽히기 2', ('악 간지럿, 간지러잇! 흐흐흐⋯', 'voice_kr/Voice_Ashur_TickleDuring1.mp3')],
        ['꿀밤 때리기', ('어쭈! / 아이스크림 떨어트릴뻔 했잖아요⋯', 'voice_kr/Voice_Ashur_DutchRubEnd1.mp3', 'voice_kr/Voice_Ashur_DutchRubEnd2_Skin1.mp3')],
        ['쓰다듬기 1', ('음⋯ 선글라스는 건들지 말아주세요⋯ ', 'voice_kr/Voice_Ashur_Touch2_Skin1.mp3')],
        ['쓰다듬기 2', ('이게 바로, 진정한 휴가구나~', 'voice_kr/Voice_Ashur_Touch2_1_Skin1.mp3')],
        ['쓰다듬기 3', ('제가 수영 가르쳐 드릴까요?', 'voice_kr/Voice_Ashur_Touch2_2_Skin1.mp3')],
    ], [
        '꿀밤 때리기 상호작용 해금 조건 : 친밀레벨 5 이상',
        '쓰다듬기 2 대사 해금 조건 : 친밀레벨 10 이상',
        '쓰다듬기 3 대사 해금 조건 : 친밀레벨 20 이상',
    ]],
    ['평온한 온천 여행', '상호작용', [
        ['볼 당기기 1', ('잘 쉬고 있는데 갑자기요?!', 'voice_kr/Voice_Ashur_Touch1_Skin2.mp3')],
        ['볼 당기기 2', ('간식 먹는 중이었는데!', 'voice_kr/Voice_Ashur_Touch1_1_Skin2.mp3')],
        ['볼 당기기 3', ('따끈하니 말랑하다구요? 어쩌라구요!', 'voice_kr/Voice_Ashur_Touch1_2_Skin2.mp3')],
        ['간지럽히기 1', ('으히~ 흐흐흐⋯', 'voice_kr/Voice_Ashur_TickleStart1.mp3')],
        ['간지럽히기 2', ('악 간지럿, 간지러잇! 흐흐흐⋯', 'voice_kr/Voice_Ashur_TickleDuring1.mp3')],
        ['꿀밤 때리기', ('어쭈! / 따뜻한 물벼락 맞아 보실래요?!', 'voice_kr/Voice_Ashur_DutchRubEnd1.mp3', 'voice_kr/Voice_Ashur_DutchRubEnd2_Skin2.mp3')],
        ['쓰다듬기 1', ('히히⋯ 나른해져요.', 'voice_kr/Voice_Ashur_Touch2_Skin2.mp3')],
        ['쓰다듬기 2', ('조, 조금은 좋을지도⋯ 흥!', 'voice_kr/Voice_Ashur_Touch2_1_Skin2.mp3')],
        ['쓰다듬기 3', ('으음~ 더 하셔도 괜찮을 것 같기도 하고⋯', 'voice_kr/Voice_Ashur_Touch2_2_Skin2.mp3')],
    ], [
        '꿀밤 때리기 상호작용 해금 조건 : 친밀레벨 5 이상',
        '쓰다듬기 2 대사 해금 조건 : 친밀레벨 10 이상',
        '쓰다듬기 3 대사 해금 조건 : 친밀레벨 20 이상',
    ]],
]) }}
{{ intimacy_tabs([
    ['기본 사복', '육성', [
        ['레벨 업', ('새 학위를 땄어요!', 'voice_kr/Voice_Ashur_LevelUp.mp3')],
        ['장비 장착', ('마법사에겐, 좋은 도구가 필수지!', 'voice_kr/Voice_Ashur_Equipment.mp3')],
        ['스킬 강화', ('마법 논문 연구를 마쳤어요~!', 'voice_kr/Voice_Ashur_HeroSkill.mp3')],
        ['보드 색칠', ('마법을 위한 전진!', 'voice_kr/Voice_Ashur_Board.mp3')],
        ['뽑기 등장', ('빵집 주인이라고 부르지 말라구요!! / 제 이름이요? / 에슈르!<br>/ 요정최고 대마법사, 에슈르가 간다!', 'voice_kr/Voice_Ashur_Gacha3.mp3', 'voice_kr/Voice_Ashur_Gacha4.mp3', 'voice_kr/Voice_Ashur_Gacha1.mp3', 'voice_kr/Voice_Ashur_Gacha2.mp3')],
        ['승급', ('교장 다음엔 총장인가?', 'voice_kr/Voice_Ashur_HeroUpgrade.mp3')],
        ['어사이드 발현', ('끝내주는 마법 이론이 마구 떠오르는 것 같아요!<br>내 모든 지식을 담은 궁극의 마법서⋯ 를 만들어볼까?', 'voice_kr/Voice_Ashur_AsideGet.mp3')],
        ['어사이드 승급', ('마법서에 채워 넣을 증명식이 뭐가 있을까⋯ 오! 좀 더 쓰다듬어 주세요! 방금 좋은 방정식이 떠올랐어요!', 'voice_kr/Voice_Ashur_AsideUpgrade.mp3')],
    ]],
    ['아이스크림 메이커', '육성', [
        ['레벨 업', ('학위나 자격증은 많을수록 좋지!', 'voice_kr/Voice_Ashur_LevelUp_Skin1.mp3')],
        ['장비 장착', ('전문가용 수영도구요? 잘쓸게요⋯!', 'voice_kr/Voice_Ashur_Equipment_Skin1.mp3')],
        ['스킬 강화', ('역시 수영도 이론이 중요하다니까.', 'voice_kr/Voice_Ashur_HeroSkill_Skin1.mp3')],
        ['보드 색칠', ('누구보다 빠르게 헤엄칠거에요⋯! ', 'voice_kr/Voice_Ashur_Board_Skin1.mp3')],
        ['뽑기 등장', ('빵집 주인이라고 부르지 말라구요!! / 제 이름이요? / 에슈르!<br>/ 요정최고 대마법사, 에슈르가 간다!', 'voice_kr/Voice_Ashur_Gacha3.mp3', 'voice_kr/Voice_Ashur_Gacha4.mp3', 'voice_kr/Voice_Ashur_Gacha1.mp3', 'voice_kr/Voice_Ashur_Gacha2.mp3')],
        ['승급', ('수영학원 차려도 되겠는데?', 'voice_kr/Voice_Ashur_HeroUpgrade_Skin1.mp3')],
        ['어사이드 발현', ('끝내주는 마법 이론이 마구 떠오르는 것 같아요!<br>내 모든 지식을 담은 궁극의 마법서⋯ 를 만들어볼까?', 'voice_kr/Voice_Ashur_AsideGet.mp3')],
        ['어사이드 승급', ('마법서에 채워 넣을 증명식이 뭐가 있을까⋯ 오! 좀 더 쓰다듬어 주세요! 방금 좋은 방정식이 떠올랐어요!', 'voice_kr/Voice_Ashur_AsideUpgrade.mp3')],
    ]],
    ['평온한 온천 여행', '육성', [
        ['레벨 업', ('온천학을 연구하고 있어요.', 'voice_kr/Voice_Ashur_LevelUp_Skin2.mp3')],
        ['장비 장착', ('온천을 즐기는데 필요한 건가요?', 'voice_kr/Voice_Ashur_Equipment_Skin2.mp3')],
        ['스킬 강화', ('쉬니까.. 연구의 실마리가 잡히는 것 같기도 하구~', 'voice_kr/Voice_Ashur_HeroSkill_Skin2.mp3')],
        ['보드 색칠', ('저 쪽으로 산책 가실래요? ', 'voice_kr/Voice_Ashur_Board_Skin2.mp3')],
        ['뽑기 등장', ('빵집 주인이라고 부르지 말라구요!! / 제 이름이요? / 에슈르!<br>/ 요정최고 대마법사, 에슈르가 간다!', 'voice_kr/Voice_Ashur_Gacha3.mp3', 'voice_kr/Voice_Ashur_Gacha4.mp3', 'voice_kr/Voice_Ashur_Gacha1.mp3', 'voice_kr/Voice_Ashur_Gacha2.mp3')],
        ['승급', ('푹~ 쉬었더니, 기운이 나요!', 'voice_kr/Voice_Ashur_HeroUpgrade_Skin2.mp3')],
        ['어사이드 발현', ('끝내주는 마법 이론이 마구 떠오르는 것 같아요!<br>내 모든 지식을 담은 궁극의 마법서⋯ 를 만들어볼까?', 'voice_kr/Voice_Ashur_AsideGet.mp3')],
        ['어사이드 승급', ('마법서에 채워 넣을 증명식이 뭐가 있을까⋯ 오! 좀 더 쓰다듬어 주세요! 방금 좋은 방정식이 떠올랐어요!', 'voice_kr/Voice_Ashur_AsideUpgrade.mp3')],
    ]],
]) }}
{{ intimacy_table('전투', [
    ['덱 편성', [
        ('나 정도면 이 자리에 충분하지!', 'voice_kr/Voice_Ashur_DeckSetting1.mp3'),
        ('아주 좋은 배치예요!', 'voice_kr/Voice_Ashur_DeckSetting2.mp3'),
    ]],
    ['스테이지 진입', ('실전 경험을 쌓을 기회야!', 'voice_kr/Voice_Ashur_Stage.mp3')],
    ['등장', [
        ('요정 최고, 대마법사 에슈르가 간다!', 'voice_kr/Voice_Ashur_Spawn1.mp3'),
        ('누가 자꾸 빵순이라고 부르는 거야!', 'voice_kr/Voice_Ashur_Spawn2.mp3'),
    ]],
    ['일반 공격', ('불공!','voice_kr/Voice_Ashur_BasicAttack1.mp3','voice_kr/Voice_Ashur_BasicAttack1-01.mp3','voice_kr/Voice_Ashur_BasicAttack1-02.mp3')],
    ['강화 공격', ('불뭉치!','voice_kr/Voice_Ashur_PowerAttack1.mp3','voice_kr/Voice_Ashur_PowerAttack1-01.mp3','voice_kr/Voice_Ashur_PowerAttack1-02.mp3')],
    ['저학년 스킬', ('빵들아, 가자! / 으라차! / 빵템피드!','voice_kr/Voice_Ashur_SPSkill1.mp3','voice_kr/Voice_Ashur_SPSkill1-01.mp3','voice_kr/Voice_Ashur_SPSkill2.mp3','voice_kr/Voice_Ashur_SPSkill2-01.mp3','voice_kr/Voice_Ashur_SPSkill3.mp3','voice_kr/Voice_Ashur_SPSkill3-01.mp3','voice_kr/Voice_Ashur_SPSkill3-02.mp3')],
    ['고학년 스킬', ('빵은! 이정도 온도에서 만들어진다!! / 이야 하! / 빵테오~!','voice_kr/Voice_Ashur_Ultimate1.mp3','voice_kr/Voice_Ashur_Ultimate1-01.mp3','voice_kr/Voice_Ashur_Ultimate2.mp3','voice_kr/Voice_Ashur_Ultimate2-01.mp3','voice_kr/Voice_Ashur_Ultimate3.mp3','voice_kr/Voice_Ashur_Ultimate3-01.mp3')],
    ['쓰러짐', [
        ('아직 월세도 다 못 냈는데⋯', 'voice_kr/Voice_Ashur_Die1.mp3'),
        ('이번 마법은 실패였다⋯.', 'voice_kr/Voice_Ashur_Die2.mp3'),
    ]],
    ['승리 대사', [
        ('하하! 그럼 그렇지~', 'voice_kr/Voice_Ashur_Victory1.mp3'),
        ('학위를 딴 보람이 있구만!', 'voice_kr/Voice_Ashur_Victory2.mp3'),
    ]],
    ['패배 대사', [
        ('빵 장사나 하러 가야겠어요⋯', 'voice_kr/Voice_Ashur_Defeat1.mp3'),
        ('적자⋯ 메꿀 수 있었는데⋯!', 'voice_kr/Voice_Ashur_Defeat2.mp3'),
    ]],
    ['PVP 패배<br>반성문', '으으, 지다니⋯ 마법 학교장으로서 면목이 없네요.&nbsp;세상에는 정말 다양한 강자가 있군요⋯!&nbsp;그러고보니 오븐을 켜놓고 나온 것 같은데⋯&nbsp;이만 가볼게요!&nbsp; 죄송해요!!'],
]) }}
{{ intimacy_table('모험회', [
    ['선택', ('교주님~', 'voice_kr/Voice_Ashur_CallPlayer1.mp3')],
    ['시작', '빵 만들다 잡혀왔네⋯'],
    ['성공률 높음', '마법 안 쓰고도 되겠는데?'],
    ['성공률 보통', '할 수 있을지도?'],
    ['성공률 낮음', '저 빵 만들러 가도 되나요⋯?'],
    ['성공', '힘으로도 가뿐해요~'],
    ['대성공', '마법의 기본, 물리력!'],
    ['실패', '앗! 빵 다 구워졌다!'],
    ['추가 보상', '(극장 세트 제작) 다음 공연도 기대하세요!'],
]) }}
{{ intimacy_table('기타', [
    ['교단', [
        '에슈르: 휘핑 손으로 쳐 볼래?',
        '에슈르: 사카린 말고 설탕!<br>에르핀: 둘이 다른 거야?<br>에슈르: 사카린은 빵 못 만들어요.',
        '에르핀: 마법으로 빵 두 배!<br>에슈르: 배는 한 개 어치만 불러요.<br>에르핀: 뭐야~ 에슈르 능력없어!',
        '빅우드: 열매 뜯겼다⋯ 좋다⋯<br>에슈르: 응? 방금 뭐라고 했어?<br>빅우드: 아니다! 말 안 했다!',
        '미로: 에, 에슈르! 드디어 제대로 인사하네, 안녕⋯!<br>에슈르: 으, 으악! 거울의 정령이다!!!<br>미로: 오해가 풀린 건지, 아닌 건지 모르겠어~!',
    ]],
    ['교주의 방 초대', '이것이 교주의 집⋯!'],
    ['연회장 초대', '안녕?'],
    ['관심 사도 지정', '빵 먹고 싶어서 저한테 이러는 거 아니죠?'],
    ['관심 사도 해제', '슬프지만 이제 마법학교 일에 더 집중할 수 있겠어요.'],
    ['로딩 화면', '(엘리아스 제빵왕) 가스 켜놓고 나온 것 같은데?'],
    ['로딩 화면<br>(만우절)', '(빵집 주인) 우리 빵을 만들어요. 밤 하늘의 별만큼!'],
    ['생일', ('교주님, 생일이죠~ 케이크 하나 만들어 드릴까요?', 'voice_kr/Voice_Ashur_Birthday.mp3')],
    ['응원사도 배치','제가 또 이런거엔 일가견이 있죠. 빵가루를 솔솔 뿌리면 식물들이 춤을 춘다니까요?'],
]) }}
{{ intimacy_table('대화', [
    ['CallHero', [
        ['여왕님~ / 여왕님! / 여왕님.','voice_kr/Voice_Ashur_CallHero1.mp3','voice_kr/Voice_Ashur_CallHero2.mp3','voice_kr/Voice_Ashur_CallHero3.mp3']]
    ],
    ['CallPlayer', [
        ['교주님~ / 교주님? / 교주님. / 교주님! / 교주님..!','voice_kr/Voice_Ashur_CallPlayer1.mp3','voice_kr/Voice_Ashur_CallPlayer2.mp3','voice_kr/Voice_Ashur_CallPlayer3.mp3','voice_kr/Voice_Ashur_CallPlayer4.mp3','voice_kr/Voice_Ashur_CallPlayer5.mp3']]
    ],
    ['Anger', [
        ['으으으! / 으휴! / 끄으응! / 쳇! / 아오오!', 'voice_kr/Voice_Ashur_Anger1.mp3','voice_kr/Voice_Ashur_Anger2.mp3','voice_kr/Voice_Ashur_Anger3.mp3','voice_kr/Voice_Ashur_Anger4.mp3','voice_kr/Voice_Ashur_Anger5.mp3']
    ]],
    ['Joy', [
        ['하하핫! / 음후훗! / 에헤! / 으흠! / 크으~','voice_kr/Voice_Ashur_Joy1.mp3','voice_kr/Voice_Ashur_Joy2.mp3','voice_kr/Voice_Ashur_Joy3.mp3','voice_kr/Voice_Ashur_Joy4.mp3','voice_kr/Voice_Ashur_Joy5.mp3']]
    ],
    ['Pleasure', [
        ['으흐 흐흐흐~ / 라라라~ / 흐음? / 음후후훗! / 어머~ ','voice_kr/Voice_Ashur_Pleasure1.mp3','voice_kr/Voice_Ashur_Pleasure2.mp3','voice_kr/Voice_Ashur_Pleasure3.mp3','voice_kr/Voice_Ashur_Pleasure4.mp3','voice_kr/Voice_Ashur_Pleasure5.mp3']]
    ],
    ['Sorrow', [
        ['흐으.. / 히잉.. / 크흑.. / 흐흐흑.. / 으아앙!','voice_kr/Voice_Ashur_Sorrow1.mp3','voice_kr/Voice_Ashur_Sorrow2.mp3','voice_kr/Voice_Ashur_Sorrow3.mp3','voice_kr/Voice_Ashur_Sorrow4.mp3','voice_kr/Voice_Ashur_Sorrow5.mp3']]
    ],
    ['Sorry', [
        ['죄송합니다.. / 죄송해요..','voice_kr/Voice_Ashur_Sorry1.mp3','voice_kr/Voice_Ashur_Sorry2.mp3']]
    ],
    ['Surprise', [
        ['으앗! / 흐어억!','voice_kr/Voice_Ashur_Surprise1.mp3','voice_kr/Voice_Ashur_Surprise2.mp3']]
    ],    
    ['Hit', [
        ['윽! / 으으윽! / 끄악! / 으아악! / 으아앙!', 'voice_kr/Voice_Ashur_Hit1.mp3','voice_kr/Voice_Ashur_Hit2.mp3','voice_kr/Voice_Ashur_Hit3.mp3','voice_kr/Voice_Ashur_Hit4.mp3','voice_kr/Voice_Ashur_Hit5.mp3']]
    ],
    ['Hmm', [
        ['음. / 으음? / 흠~','voice_kr/Voice_Ashur_Hmm1.mp3','voice_kr/Voice_Ashur_Hmm2.mp3','voice_kr/Voice_Ashur_Hmm3.mp3']]
    ],
    ['Shout', [
        ['얏! / 흣! / 챠! / 흡!','voice_kr/Voice_Ashur_Shout1.mp3','voice_kr/Voice_Ashur_Shout1-01.mp3','voice_kr/Voice_Ashur_Shout1-02.mp3','voice_kr/Voice_Ashur_Shout1-03.mp3'],
        ['이얏! / 핫! / 탓! / 흠!','voice_kr/Voice_Ashur_Shout2.mp3', 'voice_kr/Voice_Ashur_Shout2-01.mp3', 'voice_kr/Voice_Ashur_Shout2-02.mp3', 'voice_kr/Voice_Ashur_Shout2-03.mp3'],
        ['야앗! / 챠! / 흐읍! / 야앗! / 헛!','voice_kr/Voice_Ashur_Shout3.mp3', 'voice_kr/Voice_Ashur_Shout3-01.mp3', 'voice_kr/Voice_Ashur_Shout3-02.mp3', 'voice_kr/Voice_Ashur_Shout3-03.mp3','voice_kr/Voice_Ashur_Shout3-04.mp3'],
        ['이야앗! / 으랴! / 하! / 흐으읍! / 챠아~','voice_kr/Voice_Ashur_Shout4.mp3', 'voice_kr/Voice_Ashur_Shout4-01.mp3', 'voice_kr/Voice_Ashur_Shout4-02.mp3', 'voice_kr/Voice_Ashur_Shout4-03.mp3', 'voice_kr/Voice_Ashur_Shout4-04.mp3'],
        ['빵빵빵! / 빵빵! / 으아흥~ / 갸앗! / 빵!!','voice_kr/Voice_Ashur_Shout5.mp3', 'voice_kr/Voice_Ashur_Shout5-01.mp3', 'voice_kr/Voice_Ashur_Shout5-02.mp3', 'voice_kr/Voice_Ashur_Shout5-03.mp3', 'voice_kr/Voice_Ashur_Shout5-04.mp3']]
    ],
    ['Yes', [
        ['맞아요! / 좋아요~ / 좋아요!','voice_kr/Voice_Ashur_Yes1.mp3','voice_kr/Voice_Ashur_Yes2.mp3','voice_kr/Voice_Ashur_Yes3.mp3']]
    ],
    ['No', [
        ['아니에요! / 아니에요. / 아.니.에.요.','voice_kr/Voice_Ashur_No1.mp3','voice_kr/Voice_Ashur_No2.mp3','voice_kr/Voice_Ashur_No3.mp3']]
    ],
    ['Eat', '우물우물..','voice_kr/Voice_Ashur_Eat1.mp3'],
    ['Greeting', '안녕?','voice_kr/Voice_Ashur_Greeting.mp3'],
    ['Trickcal', [
        ['트릭컬 리바이브~ / 트릭컬!','voice_kr/Voice_Ashur_Trickcal1.mp3','voice_kr/Voice_Ashur_Trickcal2.mp3']]
    ],
]) }}
{{ intimacy_table('불명', [
    ['Growth', [
        ['더 큰 힘에는 더 큰... 뭐더라?','voice_kr/Voice_Ashur_Growth1.mp3'],
        ['수영 원리 이론 학위나 따볼까?','voice_kr/Voice_Ashur_Growth1_Skin1.mp3'],
        ['휴식도 성장의 밑거름이라구요?','voice_kr/Voice_Ashur_Growth1_Skin2.mp3'],
        ['내가 더 크면 학생이 더 생기겠지?','voice_kr/Voice_Ashur_Growth2.mp3'],
        ['수영과 마법, 둘 다 놓칠 수 없어요!','voice_kr/Voice_Ashur_Growth2_Skin1.mp3'],
        ['피로회복마법이라도, 연구해볼까요?','voice_kr/Voice_Ashur_Growth2_Skin2.mp3']]
    ],
    ['Line', [
        ['왜 다들 내 수업을 안 들으려고 하는거야..','voice_kr/Voice_Ashur_Line1.mp3'],
        ['이번 달 월세는 어떻게 메꾸지?', 'voice_kr/Voice_Ashur_Line2.mp3'],
        ['이번 논문 주제는.. 뭘로 할까?', 'voice_kr/Voice_Ashur_Line3.mp3']]
    ],
    ['Lobby', '학생 모집 합니다~ 첫 수강료는, 무료~','voice_kr/Voice_Ashur_Lobby.mp3'],
]) }}


## 대사 (일본어)
글로벌 버전에는 아직 '평온한 온천 여행' 스킨이 출시되지 않았으므로, 해당 스킨의 대사는 재생되지 않습니다.
{{ intimacy_table('친밀도', [
    ['레벨 1', [
        ("빵집 아줌마가 아니라 '마법사님'이라고 부르라고!", 'voice_jp/Voice_Ashur_Affinity1_1.mp3'),
        ('마법의 체계 논문도 읽어보지 않고 나랑 말을 섞겠다는 거야?', 'voice_jp/Voice_Ashur_Affinity1_2.mp3'),
        ('식사 시간에만 찾지 말고 모험할 때도 좀 불러달란 말이야!', 'voice_jp/Voice_Ashur_Affinity1_3.mp3'),
    ]],
    ['레벨 2', ('뭐? 물빵을 달라고? 그런건 다른데 가서 찾아!', 'voice_jp/Voice_Ashur_Affinity2.mp3')],
    ['레벨 3', ('흐흑⋯ 또 여왕님이 케잌 300개를 주문하셨어⋯', 'voice_jp/Voice_Ashur_Affinity3.mp3')],
    ['레벨 4', ('내 마법 강의실은 조리대 앞이야! 언제든 찾아와!', 'voice_jp/Voice_Ashur_Affinity4.mp3')],
    ['레벨 5', ('마법의 기본은 중력분이나 강력분이나…가 아니잖아!', 'voice_jp/Voice_Ashur_Affinity5.mp3')],
    ['레벨 6', ('제빵의 기본은 중력술이냐 강령술이냐…가 아니잖아!', 'voice_jp/Voice_Ashur_Affinity6.mp3')],
    ['레벨 7', ('아무도 내 마법 이론서를 읽어주지 않아… 교주님이라도 읽을래요?', 'voice_jp/Voice_Ashur_Affinity7.mp3')],
]) }}
{{ intimacy_tabs([
    ['기본 사복', '상호작용', [
        ['볼 당기기 1', ('앗! 아프잖아욧!!', 'voice_jp/Voice_Ashur_Touch1.mp3')],
        ['볼 당기기 2', ('안 그래도 힘든 일 많아요!', 'voice_jp/Voice_Ashur_Touch1_1.mp3')],
        ['볼 당기기 3', ('으아아.. 결국 이 고통에도 익숙해져 버렸어...', 'voice_jp/Voice_Ashur_Touch1_2.mp3')],
        ['간지럽히기 1', ('으히~ 흐흐흐⋯', 'voice_jp/Voice_Ashur_TickleStart1.mp3')],
        ['간지럽히기 2', ('악 간지럿, 간지러잇! 흐흐흐⋯', 'voice_jp/Voice_Ashur_TickleDuring1.mp3')],
        ['꿀밤 때리기', ('어쭈! / 으악, 이제 빵 안 나눠 드릴 거에요!', 'voice_jp/Voice_Ashur_DutchRubEnd1.mp3', 'voice_jp/Voice_Ashur_DutchRubEnd2.mp3')],
        ['쓰다듬기 1', ('살기 힘들어요⋯', 'voice_jp/Voice_Ashur_Touch2.mp3')],
        ['쓰다듬기 2', ('교주님은⋯ 흑, 제 맘 아시죠?', 'voice_jp/Voice_Ashur_Touch2_1.mp3')],
        ['쓰다듬기 3', ('그래도⋯ 조금 편해졌어요.', 'voice_jp/Voice_Ashur_Touch2_2.mp3')],
    ], [
        '꿀밤 때리기 상호작용 해금 조건 : 친밀레벨 5 이상',
        '쓰다듬기 2 대사 해금 조건 : 친밀레벨 10 이상',
        '쓰다듬기 3 대사 해금 조건 : 친밀레벨 20 이상',
    ]],
    ['아이스크림 메이커', '상호작용', [
        ['볼 당기기 1', ('물장구로 복수할거에요⋯!', 'voice_jp/Voice_Ashur_Touch1_Skin1.mp3')],
        ['볼 당기기 2', ('썬크림 다 지워져요!', 'voice_jp/Voice_Ashur_Touch1_1_Skin1.mp3')],
        ['볼 당기기 3', ('기분 좋으니까.. 봐드리는 거에요!', 'voice_jp/Voice_Ashur_Touch1_2_Skin1.mp3')],
        ['간지럽히기 1', ('으히~ 흐흐흐⋯', 'voice_jp/Voice_Ashur_TickleStart1.mp3')],
        ['간지럽히기 2', ('악 간지럿, 간지러잇! 흐흐흐⋯', 'voice_jp/Voice_Ashur_TickleDuring1.mp3')],
        ['꿀밤 때리기', ('어쭈! / 아이스크림 떨어트릴뻔 했잖아요⋯', 'voice_jp/Voice_Ashur_DutchRubEnd1.mp3', 'voice_jp/Voice_Ashur_DutchRubEnd2_Skin1.mp3')],
        ['쓰다듬기 1', ('음⋯ 선글라스는 건들지 말아주세요⋯ ', 'voice_jp/Voice_Ashur_Touch2_Skin1.mp3')],
        ['쓰다듬기 2', ('이게 바로, 진정한 휴가구나~', 'voice_jp/Voice_Ashur_Touch2_1_Skin1.mp3')],
        ['쓰다듬기 3', ('제가 수영 가르쳐 드릴까요?', 'voice_jp/Voice_Ashur_Touch2_2_Skin1.mp3')],
    ], [
        '꿀밤 때리기 상호작용 해금 조건 : 친밀레벨 5 이상',
        '쓰다듬기 2 대사 해금 조건 : 친밀레벨 10 이상',
        '쓰다듬기 3 대사 해금 조건 : 친밀레벨 20 이상',
    ]],
    ['평온한 온천 여행', '상호작용', [
        ['볼 당기기 1', ('잘 쉬고 있는데 갑자기요?!', 'voice_jp/Voice_Ashur_Touch1_Skin2.mp3')],
        ['볼 당기기 2', ('간식 먹는 중이었는데!', 'voice_jp/Voice_Ashur_Touch1_1_Skin2.mp3')],
        ['볼 당기기 3', ('따끈하니 말랑하다구요? 어쩌라구요!', 'voice_jp/Voice_Ashur_Touch1_2_Skin2.mp3')],
        ['간지럽히기 1', ('으히~ 흐흐흐⋯', 'voice_jp/Voice_Ashur_TickleStart1.mp3')],
        ['간지럽히기 2', ('악 간지럿, 간지러잇! 흐흐흐⋯', 'voice_jp/Voice_Ashur_TickleDuring1.mp3')],
        ['꿀밤 때리기', ('어쭈! / 따뜻한 물벼락 맞아 보실래요?!', 'voice_jp/Voice_Ashur_DutchRubEnd1.mp3', 'voice_jp/Voice_Ashur_DutchRubEnd2_Skin2.mp3')],
        ['쓰다듬기 1', ('히히⋯ 나른해져요.', 'voice_jp/Voice_Ashur_Touch2_Skin2.mp3')],
        ['쓰다듬기 2', ('조, 조금은 좋을지도⋯ 흥!', 'voice_jp/Voice_Ashur_Touch2_1_Skin2.mp3')],
        ['쓰다듬기 3', ('으음~ 더 하셔도 괜찮을 것 같기도 하고⋯', 'voice_jp/Voice_Ashur_Touch2_2_Skin2.mp3')],
    ], [
        '꿀밤 때리기 상호작용 해금 조건 : 친밀레벨 5 이상',
        '쓰다듬기 2 대사 해금 조건 : 친밀레벨 10 이상',
        '쓰다듬기 3 대사 해금 조건 : 친밀레벨 20 이상',
    ]],
]) }}
{{ intimacy_tabs([
    ['기본 사복', '육성', [
        ['레벨 업', ('새 학위를 땄어요!', 'voice_jp/Voice_Ashur_LevelUp.mp3')],
        ['장비 장착', ('마법사에겐, 좋은 도구가 필수지!', 'voice_jp/Voice_Ashur_Equipment.mp3')],
        ['스킬 강화', ('마법 논문 연구를 마쳤어요~!', 'voice_jp/Voice_Ashur_HeroSkill.mp3')],
        ['보드 색칠', ('마법을 위한 전진!', 'voice_jp/Voice_Ashur_Board.mp3')],
        ['뽑기 등장', ('빵집 주인이라고 부르지 말라구요!! / 제 이름이요? / 에슈르!<br>/ 요정최고 대마법사, 에슈르가 간다!', 'voice_jp/Voice_Ashur_Gacha3.mp3', 'voice_jp/Voice_Ashur_Gacha4.mp3', 'voice_jp/Voice_Ashur_Gacha1.mp3', 'voice_jp/Voice_Ashur_Gacha2.mp3')],
        ['승급', ('교장 다음엔 총장인가?', 'voice_jp/Voice_Ashur_HeroUpgrade.mp3')],
        ['어사이드 발현', ('끝내주는 마법 이론이 마구 떠오르는 것 같아요!<br>내 모든 지식을 담은 궁극의 마법서⋯ 를 만들어볼까?', 'voice_jp/Voice_Ashur_AsideGet.mp3')],
        ['어사이드 승급', ('마법서에 채워 넣을 증명식이 뭐가 있을까⋯ 오! 좀 더 쓰다듬어 주세요! 방금 좋은 방정식이 떠올랐어요!', 'voice_jp/Voice_Ashur_AsideUpgrade.mp3')],
    ]],
    ['아이스크림 메이커', '육성', [
        ['레벨 업', ('학위나 자격증은 많을수록 좋지!', 'voice_jp/Voice_Ashur_LevelUp_Skin1.mp3')],
        ['장비 장착', ('전문가용 수영도구요? 잘쓸게요⋯!', 'voice_jp/Voice_Ashur_Equipment_Skin1.mp3')],
        ['스킬 강화', ('역시 수영도 이론이 중요하다니까.', 'voice_jp/Voice_Ashur_HeroSkill_Skin1.mp3')],
        ['보드 색칠', ('누구보다 빠르게 헤엄칠거에요⋯! ', 'voice_jp/Voice_Ashur_Board_Skin1.mp3')],
        ['뽑기 등장', ('빵집 주인이라고 부르지 말라구요!! / 제 이름이요? / 에슈르!<br>/ 요정최고 대마법사, 에슈르가 간다!', 'voice_jp/Voice_Ashur_Gacha3.mp3', 'voice_jp/Voice_Ashur_Gacha4.mp3', 'voice_jp/Voice_Ashur_Gacha1.mp3', 'voice_jp/Voice_Ashur_Gacha2.mp3')],
        ['승급', ('수영학원 차려도 되겠는데?', 'voice_jp/Voice_Ashur_HeroUpgrade_Skin1.mp3')],
        ['어사이드 발현', ('끝내주는 마법 이론이 마구 떠오르는 것 같아요!<br>내 모든 지식을 담은 궁극의 마법서⋯ 를 만들어볼까?', 'voice_jp/Voice_Ashur_AsideGet.mp3')],
        ['어사이드 승급', ('마법서에 채워 넣을 증명식이 뭐가 있을까⋯ 오! 좀 더 쓰다듬어 주세요! 방금 좋은 방정식이 떠올랐어요!', 'voice_jp/Voice_Ashur_AsideUpgrade.mp3')],
    ]],
    ['평온한 온천 여행', '육성', [
        ['레벨 업', ('온천학을 연구하고 있어요.', 'voice_jp/Voice_Ashur_LevelUp_Skin2.mp3')],
        ['장비 장착', ('온천을 즐기는데 필요한 건가요?', 'voice_jp/Voice_Ashur_Equipment_Skin2.mp3')],
        ['스킬 강화', ('쉬니까.. 연구의 실마리가 잡히는 것 같기도 하구~', 'voice_jp/Voice_Ashur_HeroSkill_Skin2.mp3')],
        ['보드 색칠', ('저 쪽으로 산책 가실래요? ', 'voice_jp/Voice_Ashur_Board_Skin2.mp3')],
        ['뽑기 등장', ('빵집 주인이라고 부르지 말라구요!! / 제 이름이요? / 에슈르!<br>/ 요정최고 대마법사, 에슈르가 간다!', 'voice_jp/Voice_Ashur_Gacha3.mp3', 'voice_jp/Voice_Ashur_Gacha4.mp3', 'voice_jp/Voice_Ashur_Gacha1.mp3', 'voice_jp/Voice_Ashur_Gacha2.mp3')],
        ['승급', ('푹~ 쉬었더니, 기운이 나요!', 'voice_jp/Voice_Ashur_HeroUpgrade_Skin2.mp3')],
        ['어사이드 발현', ('끝내주는 마법 이론이 마구 떠오르는 것 같아요!<br>내 모든 지식을 담은 궁극의 마법서⋯ 를 만들어볼까?', 'voice_jp/Voice_Ashur_AsideGet.mp3')],
        ['어사이드 승급', ('마법서에 채워 넣을 증명식이 뭐가 있을까⋯ 오! 좀 더 쓰다듬어 주세요! 방금 좋은 방정식이 떠올랐어요!', 'voice_jp/Voice_Ashur_AsideUpgrade.mp3')],
    ]],
]) }}
{{ intimacy_table('전투', [
    ['덱 편성', [
        ('나 정도면 이 자리에 충분하지!', 'voice_jp/Voice_Ashur_DeckSetting1.mp3'),
        ('아주 좋은 배치예요!', 'voice_jp/Voice_Ashur_DeckSetting2.mp3'),
    ]],
    ['스테이지 진입', ('실전 경험을 쌓을 기회야!', 'voice_jp/Voice_Ashur_Stage.mp3')],
    ['등장', [
        ('요정 최고, 대마법사 에슈르가 간다!', 'voice_jp/Voice_Ashur_Spawn1.mp3'),
        ('누가 자꾸 빵순이라고 부르는 거야!', 'voice_jp/Voice_Ashur_Spawn2.mp3'),
    ]],
    ['일반 공격', ('불공!','voice_jp/Voice_Ashur_BasicAttack1.mp3','voice_jp/Voice_Ashur_BasicAttack2.mp3')],
    ['강화 공격', ('불뭉치!','voice_jp/Voice_Ashur_PowerAttack1.mp3','voice_jp/Voice_Ashur_PowerAttack2.mp3')],
    ['저학년 스킬', ('빵들아, 가자! / 으라차! / 빵템피드!','voice_jp/Voice_Ashur_SPSkill1.mp3','voice_jp/Voice_Ashur_SPSkill2.mp3','voice_jp/Voice_Ashur_SPSkill3.mp3')],
    ['고학년 스킬', ('빵은! 이정도 온도에서 만들어진다!! / 이야 하! / 빵테오~!','voice_jp/Voice_Ashur_Ultimate1.mp3','voice_jp/Voice_Ashur_Ultimate2.mp3','voice_jp/Voice_Ashur_Ultimate3.mp3')],
    ['쓰러짐', [
        ('아직 월세도 다 못 냈는데⋯', 'voice_jp/Voice_Ashur_Die1.mp3'),
        ('이번 마법은 실패였다⋯.', 'voice_jp/Voice_Ashur_Die2.mp3'),
    ]],
    ['승리 대사', [
        ('하하! 그럼 그렇지~', 'voice_jp/Voice_Ashur_Victory1.mp3'),
        ('학위를 딴 보람이 있구만!', 'voice_jp/Voice_Ashur_Victory2.mp3'),
    ]],
    ['패배 대사', [
        ('빵 장사나 하러 가야겠어요⋯', 'voice_jp/Voice_Ashur_Defeat1.mp3'),
        ('적자⋯ 메꿀 수 있었는데⋯!', 'voice_jp/Voice_Ashur_Defeat2.mp3'),
    ]],
    ['PVP 패배<br>반성문', '으으, 지다니⋯ 마법 학교장으로서 면목이 없네요.&nbsp;세상에는 정말 다양한 강자가 있군요⋯!&nbsp;그러고보니 오븐을 켜놓고 나온 것 같은데⋯&nbsp;이만 가볼게요!&nbsp; 죄송해요!!'],
]) }}
{{ intimacy_table('모험회', [
    ['선택', ('교주님~', 'voice_jp/Voice_Ashur_CallPlayer1.mp3')],
    ['시작', '빵 만들다 잡혀왔네⋯'],
    ['성공률 높음', '마법 안 쓰고도 되겠는데?'],
    ['성공률 보통', '할 수 있을지도?'],
    ['성공률 낮음', '저 빵 만들러 가도 되나요⋯?'],
    ['성공', '힘으로도 가뿐해요~'],
    ['대성공', '마법의 기본, 물리력!'],
    ['실패', '앗! 빵 다 구워졌다!'],
    ['추가 보상', '(극장 세트 제작) 다음 공연도 기대하세요!'],
]) }}
{{ intimacy_table('기타', [
    ['교단', [
        '에슈르: 휘핑 손으로 쳐 볼래?',
        '에슈르: 사카린 말고 설탕!<br>에르핀: 둘이 다른 거야?<br>에슈르: 사카린은 빵 못 만들어요.',
        '에르핀: 마법으로 빵 두 배!<br>에슈르: 배는 한 개 어치만 불러요.<br>에르핀: 뭐야~ 에슈르 능력없어!',
        '빅우드: 열매 뜯겼다⋯ 좋다⋯<br>에슈르: 응? 방금 뭐라고 했어?<br>빅우드: 아니다! 말 안 했다!',
        '미로: 에, 에슈르! 드디어 제대로 인사하네, 안녕⋯!<br>에슈르: 으, 으악! 거울의 정령이다!!!<br>미로: 오해가 풀린 건지, 아닌 건지 모르겠어~!',
    ]],
    ['교주의 방 초대', '이것이 교주의 집⋯!'],
    ['연회장 초대', '안녕?'],
    ['관심 사도 지정', '빵 먹고 싶어서 저한테 이러는 거 아니죠?'],
    ['관심 사도 해제', '슬프지만 이제 마법학교 일에 더 집중할 수 있겠어요.'],
    ['로딩 화면', '(엘리아스 제빵왕) 가스 켜놓고 나온 것 같은데?'],
    ['로딩 화면<br>(만우절)', '(빵집 주인) 우리 빵을 만들어요. 밤 하늘의 별만큼!'],
    ['생일', ('교주님, 생일이죠~ 케이크 하나 만들어 드릴까요?', 'voice_jp/Voice_Ashur_Birthday.mp3')],
    ['응원사도 배치','제가 또 이런거엔 일가견이 있죠. 빵가루를 솔솔 뿌리면 식물들이 춤을 춘다니까요?'],
]) }}
{{ intimacy_table('대화', [
    ['CallHero', [
        ['여왕님~ / 여왕님! / 여왕님.','voice_jp/Voice_Ashur_CallHero1.mp3','voice_jp/Voice_Ashur_CallHero2.mp3','voice_jp/Voice_Ashur_CallHero3.mp3']]
    ],
    ['CallPlayer', [
        ['교주님~ / 교주님? / 교주님. / 교주님! / 교주님..!','voice_jp/Voice_Ashur_CallPlayer1.mp3','voice_jp/Voice_Ashur_CallPlayer2.mp3','voice_jp/Voice_Ashur_CallPlayer3.mp3','voice_jp/Voice_Ashur_CallPlayer4.mp3','voice_jp/Voice_Ashur_CallPlayer5.mp3']]
    ],
    ['Anger', [
        ['으으으! / 으휴! / 끄으응! / 쳇! / 아오오!', 'voice_jp/Voice_Ashur_Anger1.mp3','voice_jp/Voice_Ashur_Anger2.mp3','voice_jp/Voice_Ashur_Anger3.mp3','voice_jp/Voice_Ashur_Anger4.mp3','voice_jp/Voice_Ashur_Anger5.mp3']
    ]],
    ['Joy', [
        ['하하핫! / 음후훗! / 에헤! / 으흠! / 크으~','voice_jp/Voice_Ashur_Joy1.mp3','voice_jp/Voice_Ashur_Joy2.mp3','voice_jp/Voice_Ashur_Joy3.mp3','voice_jp/Voice_Ashur_Joy4.mp3','voice_jp/Voice_Ashur_Joy5.mp3']]
    ],
    ['Pleasure', [
        ['으흐 흐흐흐~ / 라라라~ / 흐음? / 음후후훗! / 어머~ ','voice_jp/Voice_Ashur_Pleasure1.mp3','voice_jp/Voice_Ashur_Pleasure2.mp3','voice_jp/Voice_Ashur_Pleasure3.mp3','voice_jp/Voice_Ashur_Pleasure4.mp3','voice_jp/Voice_Ashur_Pleasure5.mp3']]
    ],
    ['Sorrow', [
        ['흐으.. / 히잉.. / 크흑.. / 흐흐흑.. / 으아앙!','voice_jp/Voice_Ashur_Sorrow1.mp3','voice_jp/Voice_Ashur_Sorrow2.mp3','voice_jp/Voice_Ashur_Sorrow3.mp3','voice_jp/Voice_Ashur_Sorrow4.mp3','voice_jp/Voice_Ashur_Sorrow5.mp3']]
    ],
    ['Sorry', [
        ['죄송합니다.. / 죄송해요..','voice_jp/Voice_Ashur_Sorry1.mp3','voice_jp/Voice_Ashur_Sorry2.mp3']]
    ],
    ['Surprise', [
        ['으앗! / 흐어억!','voice_jp/Voice_Ashur_Surprise1.mp3','voice_jp/Voice_Ashur_Surprise2.mp3']]
    ],    
    ['Hit', [
        ['윽! / 으으윽! / 끄악! / 으아악! / 으아앙!', 'voice_jp/Voice_Ashur_Hit1.mp3','voice_jp/Voice_Ashur_Hit2.mp3','voice_jp/Voice_Ashur_Hit3.mp3','voice_jp/Voice_Ashur_Hit4.mp3','voice_jp/Voice_Ashur_Hit5.mp3']]
    ],
    ['Hmm', [
        ['음. / 으음? / 흠~','voice_jp/Voice_Ashur_Hmm1.mp3','voice_jp/Voice_Ashur_Hmm2.mp3','voice_jp/Voice_Ashur_Hmm3.mp3']]
    ],
    ['Shout', [
        ['얏! / 이얏! / 이랴앗! / 오랴앗! / 우오오!','voice_jp/Voice_Ashur_Shout1.mp3','voice_jp/Voice_Ashur_Shout2.mp3','voice_jp/Voice_Ashur_Shout3.mp3','voice_jp/Voice_Ashur_Shout4.mp3', 'voice_jp/Voice_Ashur_Shout5.mp3']]
    ],
    ['Yes', [
        ['맞아요! / 좋아요~ / 좋아요!','voice_jp/Voice_Ashur_Yes1.mp3','voice_jp/Voice_Ashur_Yes2.mp3','voice_jp/Voice_Ashur_Yes3.mp3']]
    ],
    ['No', [
        ['아니에요! / 아니에요. / 아.니.에.요.','voice_jp/Voice_Ashur_No1.mp3','voice_jp/Voice_Ashur_No2.mp3','voice_jp/Voice_Ashur_No3.mp3']]
    ],
    ['Eat', '우물우물..','voice_jp/Voice_Ashur_Eat1.mp3'],
    ['Greeting', '안녕?','voice_jp/Voice_Ashur_Greeting.mp3'],
    ['Trickcal', [
        ['트릭컬! / 트릭컬!','voice_jp/Voice_Ashur_Trickcal1.mp3','voice_jp/Voice_Ashur_Trickcal2.mp3']]
    ],
]) }}
{{ intimacy_table('불명', [
    ['Growth', [
        ['더 큰 힘에는 더 큰... 뭐더라?','voice_jp/Voice_Ashur_Growth1.mp3'],
        ['수영 원리 이론 학위나 따볼까?','voice_jp/Voice_Ashur_Growth1_Skin1.mp3'],
        ['<s>휴식도 성장의 밑거름이라구요?</s>','voice_jp/Voice_Ashur_Growth1_Skin2.mp3'],
        ['내가 더 크면 학생이 더 생기겠지?','voice_jp/Voice_Ashur_Growth2.mp3'],
        ['수영과 마법, 둘 다 놓칠 수 없어요!','voice_jp/Voice_Ashur_Growth2_Skin1.mp3'],
        ['<s>피로회복마법이라도, 연구해볼까요?</s>','voice_jp/Voice_Ashur_Growth2_Skin2.mp3']]
    ],
    ['Line', [
        ['왜 다들 내 수업을 안 들으려고 하는거야..','voice_jp/Voice_Ashur_Line1.mp3'],
        ['이번 달 월세는 어떻게 메꾸지?', 'voice_jp/Voice_Ashur_Line2.mp3'],
        ['이번 논문 주제는.. 뭘로 할까?', 'voice_jp/Voice_Ashur_Line3.mp3']]
    ],
    ['Lobby', '학생 모집 합니다~ 첫 수강료는, 무료~','voice_jp/Voice_Ashur_Lobby.mp3'],
]) }}

