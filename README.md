# empty_pi_server

주차장 이미지를 촬영하고, main 서버로 이미지를 보내주는 라즈베리파이 서버

### run
```
sudo python3 main.py
```

### 환경 설정

1. sd카드 포맷

    FAT32, 기본 할당 크기
  
2. OS 설치 [[참고]](https://www.codesarang.com/2?category=1115206)

    ```
    id : pi
    passwd raspberry
    #변경 passwd
    ```
  
3. 고정 IP 할당

    * [참고 1](https://bebutae.tistory.com/58)
    * [참고 2](https://blog.naver.com/whdakf123/221772267288)
    * [참고 3](https://constructionsite.tistory.com/37?category=818393)

4. WiFi 연결
    * [참고 1](https://webnautes.tistory.com/903)
    * [참고 2](https://blog.dalso.org/raspberry-pi/raspberry-pi-4/7496)


5. 리눅스 기본 설정

    ```
    sudo apt-get update
    sudo apt install vim-gui-common
    
    sudo apt-get python-flask
    sudo apt-get install python-picamera python3-picamera
    ```
    
