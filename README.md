# WEB_CLOUD_OmilJomil_NAVYeffect
외적 군기 디텍팅 솔루션. 사진 넣을 것 gif.
# :sunglasses: 오밀조밀 : 외적 군기 디텍팅 솔루션 :whale:

### 기지 정문에 카메라를 설치, 외적 군기 불량 여부를 판단해 부대 관리자 및 병들이 볼 수 있는 체계에 제공한다.


## :pencil: INDEX
<details open="open">
  <ol>
    <li><a href="#intro"> ᐅ 프로젝트 소개 (Intro)</a></li>
    <li><a href="#features"> ᐅ 기능 설명 (Features)</a></li>
    <li><a href="#pre-required"> ᐅ 컴퓨터 구성 / 필수 조건 안내 (Pre-required)</a></li>
    <li><a href="#technique"> ᐅ 기술 스택 (Technique used)</a></li>
    <li><a href="#install"> ᐅ 설치 안내 (How to download)</a></li>
    <li><a href="#usage"> ᐅ 프로젝트 사용법 (How to use)</a></li>
    <li><a href="#team"> ᐅ 팀원 정보 (Meet the team)</a></li>
    <li><a href="#copyright"> ᐅ 저작권 및 사용권 정보 (Copyright and License)</a></li>
    <li><a href="#appendex"> ᐅ 부록 (Appendex)</a></li>
  </ol>
</details>

# sections

<h2 id="intro"> :grey_question: 프로젝트 소개 (Intro)</h2>

> + 카메라를 설치해, AI가 군 기지 출입시 두발 및 복장 불량 여부를 인식한다.
>    + 대시보드에 부대별, 전군 실시간 데이터를 올려 통계직인 여러 인사이트를 게재한다.
>    + 각 부대 담당 간부는 접근 가능한 계정을 부여받아 이를 통해 확인할 수 있다.
>    + 기지 내 사병들 또한 외적 군기 위반 요소들을 확인해 스스로 점검할 수 있다.

### 개요
군기는 군대의 기율이며 생명과 같기에 항상 엄정한 군기를 세워야 합니다. 또한 군기는 곧 사기이며, 이를 가장 잘 나타내는 부분이 외적 군기와 제식 훈련입니다. 다만 제식은 특별한 상황이 아니면 평상시에 보여줄 수 있는 부분이 아니기 때문에 평시에 외적 군기 확립을 중시 여길 수밖에 없습니다.

그러나 두발 상태 불량부터 시작해 명찰, 계급장, 모자까지,,, 

 *외적 군기 위반 요소는 매우 다양합니다.*

우리 **NAVY효과의 "오밀조밀"은 이러한 사례들을 수집해 관리자, 일반 사병, 군사 경찰 할 것 없이 기지 내 장병들에게 편의와 인사이트를 제공하는 솔루션**이 될 것입니다.

<h2 id="features"> :mag: 기능 설명 및 프로젝트 사용법 (Features)</h2>

### :computer: UX/UI
> 이미지를 기능 설명하며 보여주기
 + 로그인 및 회원가입 기능입니다. 각 부대 담당자들은 부여받은 계정으로 접근 가능합니다.
 + 부대별 대시보드입니다. 실시간으로 출입자 정보가 리스트업되며, 각 요소 별 불량 비율이나 월간 양호 빈도 등을 제공합니다.
 + 부대 인원 조회 페이지입니다. 실시간 감지되는 리스트 중 한 컴포넌트 클릭 시 상세보기 창이 팝업됩니다.
 + 랭킹페이지입니다. 위반 비율을 따져 1순위부터 전 부대를 확인할 수 있습니다.

 + 전군 통계 대시보드입니다. 부대별 현황과 다르게 훨씬 넓은 범위에서의 추이를 보여줍니다.
 + 인공지능이 외적 군기 위반 여부를 판별하는 모습입니다.


<h2 id="pre-required"> :dash: 컴퓨터 구성 / 필수 조건 안내 (Pre-required)</h2>

 + ECMAScript 6 지원 브라우저 사용
 + 권장: Google Chrome 버전 77 이상
 + Internet Explorer 미사용 추천 등

<h2 id="technique"> :technologist: 기술 스택 (Technique used)</h>

### Back end
 + python 3.8
 + fastapi

### DB(back-end)
 + postgresql

### AI(back-end)
 + lib : tensorflow, OpenCV
 + model : swit-transformer, YOLO v4, HED(Holistically-Nested Edge Dataset), MobileNet
 + dataset : MS-COCO, Pascal VOC Dataset Mirror, CelebAMask-HQ, Figaro-1k, Lft

### Front end
 + vue.js
 + node.js

<h2 id="install"> :arrow_down: 설치 안내 (How to download)</h2>

**어느 것 다운받아서 어느 주소로 들어가야 사용 가능한지 설명. 추후 공지 예정**

<h2 id="team"> :kissing_heart: 팀원 정보 (Meet the team)</h2>

> 팀 NAVY효과

| Name | Role | Contect |   
|:---:|:---:|:---:| 
|조남훈| 팀장, 기획자 | lovin6109@gmail.com |   
|조준영| AI 개발자, 웹디자이너 | joon0zo1022@gmail.com |
|정의철| 백엔드 개발자 | com.dos.m0nk3y@gmail.com |
|김대원| 백엔드 개발자 | kdwkd0078@gmail.com |   
|허태량| 프론트 엔드 개발자 | cake0702@naver.com |   
|김민섭| 프론트 엔드 개발자 | tjqtjq0516@gmail.com |

<h2 id="copyright"> :books: 저작권 및 사용권 정보 (Copyright & License)</h2>

 + MIT
This project is licensed under the terms of the MIT license.


<h2 id="appendex"> :card_index: 부록 (Appendex)</h2>

> 개발 문서 
