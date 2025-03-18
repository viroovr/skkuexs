# SKKUEXS - 교환학생 지원 플랫폼  

## 프로젝트 소개  
**SKKUEXS**는 성균관대학교(SKKU) 교환학생들을 지원하는 웹 플랫폼입니다.  
교환학생들이 겪는 **언어 장벽, 문화 차이, 정보 부족** 등의 문제를 해결하기 위해,  
**신뢰할 수 있는 정보 제공, 커뮤니티 기능, 멘토링 시스템**을 제공합니다.  

### 1. **주요 기능**  
**정리된 정보 제공** – 교환학생 프로그램 관련 핵심 정보 제공  
**커뮤니티 기능** – 교환학생, 선배, 멘토 간의 네트워크 형성  
**학습 자료 제공** – 교환학생 후기 및 과목 평가 자료 정리  
**비자 & 기숙사 정보** – 비자 신청 및 숙소 선택 가이드 제공  
**게시판 시스템** – 교환학생들이 직접 경험을 공유할 수 있는 공간  


## 2. 기술 스택  
### **프론트엔드 (Frontend)**  
- **HTML, CSS, JavaScript** – 사용자 인터페이스(UI) 개발  
- **Figma** – UI/UX 디자인  

### **백엔드 (Backend)**  
- **Django** – 웹 애플리케이션 프레임워크  
- **SQLite** – 데이터베이스 관리  
- **AWS Lightsail** – 클라우드 호스팅  

### **인공지능 & 데이터 처리**  
- **KoT5** – 한국어 텍스트 요약 모델  
- **GPT-4** – AI 기반 콘텐츠 생성  
- **WordCloud** – 키워드 시각화


## 3. 프로젝트 실행 방법  

### **1️⃣ 설치**  
```bash
https://github.com/viroovr/skkuexs.git
cd SKKUEXS
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 2️⃣ 데이터베이스 설정

```bash
python manage.py migrate
python manage.py createsuperuser  # 관리자 계정 생성
```

### 3️⃣ 서버 실행
```bash
python manage.py runserver
```

🔗 웹사이트 접속: http://127.0.0.1:8000/


## 4. 시스템 구조
SKKUEXS는 클라이언트-서버 아키텍처를 기반으로 하며,
사용자는 웹 UI를 통해 정보를 얻고, Django 백엔드가 데이터 처리를 담당합니다.

![image](https://github.com/user-attachments/assets/60c15206-d255-47d1-9e23-16c0f180f44d)


## 5. 팀원 소개
Team H (성균관대학교 캡스톤 프로젝트)

이하은
한휘근
서현원
김주원



