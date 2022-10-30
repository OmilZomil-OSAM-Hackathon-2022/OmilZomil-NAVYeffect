## :pencil: INDEX
<details open="open">
<ol>
<li><a href="#intro"> ᐅ  Project Omil-Zomil (Intro)</a></li>
<li><a href="#features"> ᐅ  핵심 기능 (Features)</a></li>
<li><a href="#pages"> ᐅ  기타 페이지 (Pages)</a></li>
<li><a href="#links"> ᐅ  함께 보기 (External Links)</a></li>
</ol>
</details>
<!--
핵심 기능이랑 기타 페이지 말고 하나는 보여주고 하나는 인터렉션 하는데, 사용자 기능/관리자 기능이라 할까?
뭔가 '핵심', '기타'하니까 나머지는 쩌리같고 그럼,,,
-->

<h2 id="intro"> :grey_question: Project Omil-Zomil (Intro)</h2>


<img src="https://user-images.githubusercontent.com/59905641/198840302-070fa67e-1fa9-44a3-9970-dcdd4107fc6f.png" align="left" width="300" height="400"/>
사진을 찍고 나서 AI로 판단한 WebRTC 컨테이너가 그 데이터를 DB 컨테이너에 저장하면, 다시 DB 컨테이너에서 데이터를 받아와 Omil-Zomil Backend 컨테이너에서 파싱한다.<br></br>
이를 **웹 서비스에서 대시보드, 통계적 추이 등으로 사용자에게 보여주는 구조**이다. 본 문서에서는 그 페이지들에 대한 설명을 적어두었다.<br></br>

<br clear="left"/><br></br>

<img src="https://user-images.githubusercontent.com/59905641/198857296-d50d29d4-07e2-49b5-a9cc-48a7c7677181.gif" align="right" width="300" height="400"/>


 :robot: *영상 인식 AI* : 카메라로 찍은 영상에서 사람의 유무, 얼굴 인식, 두발 불량 여부, 복장 불량 여부를 판별합니다.<br></br>
 + 자세한 설명은 ‘함께 보기’의 **AI READMD.md**를 참고하여 주시기 바랍니다. <br></br>

<br clear="right"/>

<h2 id="features"> :star2: 핵심 기능 (Features):stars:</h2>

### 대시보드

![대시보드](https://user-images.githubusercontent.com/59905641/198835988-dbbb25c4-9aa0-4412-b985-21f7232fc773.gif)
 + 위병소 실시간 감지현황, 파츠별 불량비율 등 *실시간으로 감지되는 데이터들을 시각화*해서 보여주는 **부대별 대시보드** 페이지입니다.
 + 이번 달 우리 부대 두발/복장 양호 인원, 출입 인원수와 **전월 대비 증감률**을 카드로 보여줍니다.
 + 이번 달 우리 부대 **파츠별 불량 비율**을 원 그래프로 보여줍니다.
 + 위병소(기지 정문) 출입 인원의 **실시간 감지 현황**을 보여줍니다. *실시간 감지 현황 페이지로 넘어갈 수 있습니다.*
 + 지역 내 부대 순위, 부대 내 양호 비율 순위 축하 등의 *이벤트 카드*로 동기부여를 해줍니다.


### 실시간 감지 현황

![실시간 감지 현황](https://user-images.githubusercontent.com/59905641/198836560-3cce9488-ff6e-48e0-a826-6417643aae68.gif)
 + **부대 인원 조회**가 가능하며, 출입자의 기본적인 정보 및 복장의 종류 및 양호/불량 상태를 알 수 있습니다.
 + 자세히 보기 클릭 시 *세부 정보 팝업창*이 뜨며, 실제 찍힌 **사진과 각각의 인식된 불량 요소(파츠. 이름표 등)를 확인**할 수 있습니다.
 + 이를 통해 *AI가 잘못 판단한 부분도 부대 관리자가 수정할 수 있어* **오탐을 방지**합니다.

### 전군 통계

![전군 통계](https://user-images.githubusercontent.com/59905641/198836561-ca162f44-57b3-4be5-8e86-26ad5c8eaeff.gif)
 + DB에서 *데이터를 불러와 파싱*한 것을 각군 및 파츠별, 시간별(월/연 등) 다양한 시각 자료로 확인할 수 있는 **전군 통계 대시보드**입니다.
 + 특히 *월별 불량 파츠 비율, 연간 전군 불량 비율 등의 추이를 볼 수 있어* **부대 관리자**들은 생활관 운영 방침을 정할 때 참고할 수 있습니다.
 + 또한 **사병**들도 자주 불량이 되는 파츠를 의식하는 식으로 **인사이트를 얻을 수 있습니다.**
 + 부대별 대시보드와 함께 외적 군기 확립 고취를 위해 데이터를 활용하는 *핵심 페이지*입니다.

### 랭킹 페이지

![랭킹페이지](https://user-images.githubusercontent.com/59905641/198835555-89334f4e-bdbc-4ac3-8031-d88cafe2ebde.gif)
 + 양호 / 불량 인원 및 비율 등을 통해 부대별 순위를 *리스트업* 했습니다.
 + 이와 더불어 상위 3개 부대는 순위 강조 아이콘을 붙여 **성취감**을 느끼게 해 외적 군기 확립 의식을 복돋아주었습니다.

<h2 id="pages"> :page_with_curl: 기타 페이지 (Pages):star:</h2>

### 휴가 관리 페이지

![휴가 신청](https://user-images.githubusercontent.com/59905641/198836569-ddead0c9-ddf8-4cd6-8f43-ef5725608d5c.gif)
 + 출입 일자를 입력해 휴가를 신청합니다.
 + 그러면 부대 관리자는 본인이 언제 인원 조회 페이지로 어떤 사람들의 상세보기 창을 확인해야 하는지를 알 수 있습니다.

### 로그인 / 회원가입

> 로그인 화면입니다.

![로그인](https://user-images.githubusercontent.com/59905641/198838304-9223f8a0-f04d-4a29-b4e8-8c04a904c4c6.gif)

> 회원 가입 화면입니다.

 + OMIL-ZOMIL을 사용하기 위해 기본적으로 제공하는 로그인, 회원 가입 기능입니다. *회원 가입 신청 시 관리자의 승인이 필요합니다.*
 
### 프로필 수정
 + 일반 사용자, 부대 관리자, 루트 관리자에게 각각 다른 프로필 수정 페이지를 보여줍니다.
> 일반 사용자

![프로필 수정-일반사용자](https://user-images.githubusercontent.com/59905641/198836563-5141ab60-c5df-422c-b1d2-c0e341d440ca.gif)
 + 기본적인 프로필 수정 기능입니다.

> 부대 관리자

![프로필 수정-일반관리자](https://user-images.githubusercontent.com/59905641/198839556-4bad30d2-44f2-48a9-806a-f94c0fc6212f.gif)
 + 프로필 수정 탭 외에도 사용자 관리, 휴가 관리 탭이 추가되었습니다.
 + 사용자 관리에서 본인 부대 인원을 파악, 수정 및 삭제 등의 작업을 수행할 수 있습니다.
 + 휴가 관리에서 본인 부대 인원이 신청한 휴가 내역을 파악, 승인 및 거부할 수 있습니다.

> 루트 관리자

![프로필 수정-최고관리자](https://user-images.githubusercontent.com/59905641/198836566-d2282ad2-f52e-44f3-ad96-93c56d595015.gif)
 + 부대 관리자 페이지의 기능에 부대 관리, 위병소 관리 페이지가 추가되었습니다.
 + **사용자 관리 페이지에**서 회원 가입 신청으르 승인하며, **각 회원의 권한을 부여 및 관리**할 수 있습니다.
 + *위병소 관리 페이지와 부대 관리 페이지*는 각각 추가 및 이름을 수정할 수 있습니다.
 + 부대 관리 페이지에서 각 부대에 위병소를 연결시킵니다.


<h2 id="links"> :grey_question: 함께 보기 (External Links)</h2>

:arrow_down_small: [README.md - Main](https://github.com/osamhack2022-v2/WEB_CLOUD_OmilZomil_NAVYeffect/blob/main/README.md)  
:arrow_down_small: [README.md - WebRTC](https://github.com/osamhack2022-v2/WEB_CLOUD_OmilZomil_NAVYeffect/blob/main/webrtc/Readme.md)  
:arrow_down_small: [README.md - AI](https://github.com/osamhack2022-v2/WEB_CLOUD_OmilZomil_NAVYeffect/blob/main/webrtc/ai/readme.md)
