

## install ssh server

github action시 빌드를 위한 ssh server를 vscode server에서 빌드

### 설치
sudo apt-get install openssh-server
service ssh start

/etc/ssh/sshd_config 파일 수정
service ssh restart

### 옵션 추가

### 사용자 설정

useradd omil
passwd omil

