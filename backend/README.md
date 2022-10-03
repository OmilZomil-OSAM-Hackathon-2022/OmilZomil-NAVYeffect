## 구조 설명

### app

api 기능을 담당하는 코드
각 폴더별로 서비스를 분리

model : db orm 객체
crud : 데이터 crud 를 담당
schema : pydantic 객체
router : api endpoint 를 담당

### static

템플릿 모음

### core

공통적으로 사용하는 코드들을 모아놓음

### docker

개발때 사용하는 코드들 모음
dockerfile 이나 기타 웹서비스에 포함되지 않는 코드들을 모음
