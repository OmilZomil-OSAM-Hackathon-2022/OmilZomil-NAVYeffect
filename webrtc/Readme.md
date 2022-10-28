## :pencil: INDEX
<details open="open">
<ol>
<li><a href="#intro"> ᐅ  프로젝트 오밀조밀 - WebRTC (Intro)</a></li>
<li><a href="#mechanism"> ᐅ  동작 과정 (How it works)</a></li>
<li><a href="#features"> ᐅ  핵심 기능 (Features)</a></li>
<li><a href="#image-processing"> ᐅ  이미지 처리 과정 (Image Processing)</a></li>
<li><a href="#links"> ᐅ  함께 보기 (External Links)</a></li>
</ol>
</details>

<h2 id="intro"> :grey_question: 프로젝트 오밀조밀 - WebRTC (Intro)</h2>
기지 정문과 같은 출입 관리 장소, 즉 각각의 이하 ‘위병소’마다 카메라를 설치해 서버로 이미지를 전송합니다. 이때, 특정 프로그램 설치 없이 사용하기 위해 WebRTC, WebSocket을 이용해 구현했습니다.

### WebRTC란?
Web Real-Time Communications의 약어. 별도의 플러그인 없이 음성, 화상 채팅 및 데이터 공유 등이 가능한 API.

이를 통해 우리 프로젝트에서는 모든 PC마다 설치되어있는 웹 브라우저와 카메라로 촬영을 할 것입니다.

  
<h2 id="mechanism"> :gear: 동작 과정(How it works)</h2>
<img src="https://user-images.githubusercontent.com/59905641/198444532-6a9e04ca-22d7-4344-93df-5f3118bef4c1.png" align="left" width="300px" height="300px"/>
1. <i>WebRTC</i>를 사용, 웹 브라우저와 카메라가 있는 pc면 <b>특별한 프로그램 설치 없이</b> 해당 카메라로 촬영한다.<br></br>
2. 촬영한 이미지는 <i>WebSocket</i>을 통해 서버로 전달한다.<br><br/>
3. 이미지 1차 분석, 사람이 나온 경우만 파일로 저장 후 해당 경로를 AI 처리 프로세서에 전달한다.<br></br>
4. AI 프로세서는 그 경로를 queue 형식으로 저장, 선입선출 방식으로 하나씩 이미지를 분석한다.<br><br/>
5. 이후 분석 완료된 이미지는 <i>WebSocket</i>을 통해 빠르게 프론트 엔드(클라이언트)에 전달하고, DB에 저장한다.<br></br>

<br clear="left"/>

  
<h2 id="features"> :gem: 핵심 기능 (Features)</h2>

이러한 일련의 동작 과정에서 주목할 만한 부분이 몇 개 있습니다.

### 빠른 속도와 편의성 추구

- webrtc를 사용한 촬영으로 추가 프로그램 없이 동작한다.
- 클라이언트에게 websocket으로 이미지를 전달한다. 아래의 처리 이슈(프로세스 분리)는 서버 보호를 위한 결정이나, 비동기 방식을 포기하게 만들었기에 웹소켓으로 속도적인 면을 보완한다.

 
### 이미지 수신 프로세스와 AI 처리 프로세스의 분리

- webrtc 프론트에서 송신하는 사진들을 백엔드에서 다 받지 못하면 서버 다운되고, 그 데이터도 버려지게 된다.

 - 방지 위해 백엔드가 버퍼처럼 파일 시스템에 우선 이미지를 저장함. 중간에 queue 이벤트 문을 두어, 선입선출 식으로 AI 처리 프로세스가 파일을 읽은 후 이미지 한 장씩 처리하고(판단 후 송신) 지우기를 반복한다.

  
<h2 id="image-processing"> :movie_camera: 이미지 처리 과정 (Image Processing)</h2>

>구간별로 AI 처리 결과에 따라 이미지 처리.
  

1. 수신한 이미지가 사람인지 아닌지 파악합니다.
   1.1. 사람이 아닌 경우 더 이상 진행하지 않습니다.


2. 사람인 경우 해당 이미지를 파일로 저장합니다.
   2.1. 저장한 이미지 경로를 socket을 사용하여 ai 프로세서에게 전달합니다.
  
  
3. 받은 경로를 queue 형식으로 저장하고, 이미지를 처리할 worker 프로세스를 생성합니다.
   3.1 각 카메라별로 최대 1개의 프로세서가 실행됩니다.
   3.2 처리할 이미지가 많을 때 서버의 메모리 캐퍼시티를 넘지 않게 하기 위해, 이미지를 파일로 저장하고 queue형식으로 관리했습니다.
  

4. worker 프로세스에서 queue에 저장된 경로를 참조하여 이미지를 하나씩 분석합니다.


5. 분석이 완료된 경우 해당 결과에 따라 처리합니다.
   5.1. 분석결과를 WebSocket을 통해 실시간으로 처리결과를 화면에 띄워줍니다.
   5.2. 분석결과를 DB에 저장합니다.


6. 연속적인 이미지인 경우 이전 이미지를 참조하여 데이터를 갱신합니다.
   6.1. 데이터가 갱신된 경우만 DB를 접근합니다.
   6.2. 일정 시간 이상 AI 처리결과가 동일한 경우 해당 사람에 대해 더이상 AI가 처리하지 않습니다.

<h2 id="links"> :arrows_counterclockwise: 함께 보기 (External Links)</h2>
Main README.md

Project Omil-Zomil README.md

