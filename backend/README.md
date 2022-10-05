## 개발환경 설정 

### vscode

```

{
    "python.pythonPath": "/usr/bin/",
    "python.defaultInterpreterPath": "/usr/bin/python3",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": ["--max-line-length=120"],
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "/usr/bin/black",
    "python.formatting.blackArgs": ["--line-length=160"],
    "[python]": {
        "editor.formatOnSave": true,
        "editor.defaultFormatter": null,
        "editor.tabSize": 4
    }
}
```


설치 목록
apt-get install flake8
apt-get install black

작성해야 하는 파일
vscode에서 여는 프로젝트 폴더의 최상단에
.vscode/settings.json 파일을 제작
그리고 위 코드를 복붙

python, flake8, black의 경로는 각자 환경에 맞춰서 변경
vscode 확장 프로그램
vscode에서 python 이라고 적혀있는 확장 프로그램을 설치




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
