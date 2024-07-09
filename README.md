# 2024-Herethon-2
2024 여기톤 : HERETHON 2조 <br><br>

<img width="400px" src="./StuckProject/Static/img/LOGO.png">

👉🏻 서비스 바로가기

<br><br>
### 📙 프로젝트 소개
STUCK은 자기주도학습을 위한 AI 문제생성 및 질의응답 서비스입니다. 
학생들의 자기주도적 학습 태도 정립을 목표로 만들어진 STUCK은 다음과 같이 소비자들의 painpoint를 해결합니다.
#### 1. 문제 생성
* 문제 생성 탭으로 이동하여 저장하고자 하는 폴더를 생성하거나, 선택한 후 문제를 생성할 수 있습니다.
* 문제의 이름, 생성할 문제의 개수, 문제의 유형(객관식, 주관식), 생성하고자 하는 교재의 pdf나 이미지를 업로드할 수 있습니다.
![img_1.png](img_1.png)
![img.png](img.png)
* 이미지를 업로드한 후 문제 생성 버튼을 클릭했다면 업로드한 이미지의 텍스트를 google cloud vision API를 통해 추출합니다.
* 추출한 텍스트를 기반으로 프롬프팅을 통해 chatGPT에게 문제 생성을 요청합니다.
* chatGPT의 응답을 기반으로 문제를 생성합니다.
![img_2.png](img_2.png)
![img_3.png](img_3.png)
![img_4.png](img_4.png)
![img_5.png](img_5.png)

<br><br>
### 🦁 STUCK 개발 팀원 소개
#### Plan & Design
| <center> 박우현  </center>                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------|
| <center> <img width="150px" src="https://ipainting.co.kr/wp-content/uploads/2019/02/%EB%8F%99%EB%AC%BC%EB%8F%84%EC%95%88_46.jpg"></center> | 
| <center> 기획, 디자인 </center>                                                                                                                 |
####  ️Front-end
| <center> 최수진 </center>                                                                            | <center> 송유선 </center>                                                                         | 
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <center> <img width="150px" src="https://avatars.githubusercontent.com/u/134383155?v=4"></center> | <center> <img width="150px" src="https://avatars.githubusercontent.com/u/164325907?v=4"></center> | 
| <center> 역할1 </center>                                                                            | <center> 역할2 </center>                                                                           | 
| <center>  [@jinsujini](https://github.com/jinsujini) </center>                                    | <center> [@s-uxun](https://github.com/s-uxun) </center>                                           | 

#### Back-end
| <center> 김가현 </center>                                                                         | <center> 김은서 </center>                                                                            | 
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <center> <img width="150px" src="https://avatars.githubusercontent.com/u/115142931?v=4"></center> | <center> <img width="150px" src="https://avatars.githubusercontent.com/u/128278212?v=4" /> </center> | 
| <center> 로그인 회원가입<br>아이디 비밀번호 찾기<br>목표 설정</center>                               | <center> 문제 & 질문 관련 기능<br>MyStuck 폴더 구조</center>                                           | 
| <center>  [@Kimgah](https://github.com/Kimgah) </center>                                          | <center> [@7beunseo](https://github.com/7beunseo) </center>                                           | 

<br><br>
### 🔥 기술 스택

####  ️Front-end
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">

#### Back-end
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

#### ETC
<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white"> <img src="https://img.shields.io/badge/Google Cloud Vision-4285F4?style=for-the-badge&logo=Google Cloud&logoColor=white"> <img src="https://img.shields.io/badge/amazonec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white">

<br><br>
### 📁 폴더 구조
```plain text
📂 2024-Herethon-2
└─ StuckProject
 ├─ accounts/
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ models.py
 │  ├─ tests.py
 │  └─ views.py
 ├─ media/
 ├─ qna/
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ models.py
 │  ├─ tests.py
 │  └─ views.py
 ├─ quiz/
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ models.py
 │  ├─ tests.py
 │  └─ views.py
 ├─ static
 │  ├─ css/
 │  ├─ fonts/
 │  ├─ img/
 │  └─ js/
 ├─ StuckProject
 │  ├─ __init__.py
 │  ├─ asgi.py
 │  ├─ settings.py
 │  ├─ urls.py
 │  └─ wsgi.py
 ├─ templates
 │  ├─ base.html
 ├─ todo/
 │  ├─ __init__.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ models.py
 │  ├─ tests.py
 │  └─ views.py
 ├─ .env
 ├─ db.sqlite3
 ├─ manage.py
 ├─ requirements.txt
 ├─ service_account.json
 └─ manage.py
```

<br><br>
### 🖥️ 개발환경에서의 실행 방법
```shell
cd 2024-Herethon-2
python -m venv venv
source venv/Scripts/activate
cd StuckProject
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py runserer
```
* google cloud vision에서 api 발급 후 service_account.json 파일 다운로드
* openAI API 토큰 발급하여 .env 파일에 저장
```.env
OPENAI_API_KEY="발급받은 토큰"
```
