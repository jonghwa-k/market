sparta-market
🪷 SpartaMarket_DRF 🪷
⏰ 개발 기간
2024.09.05 ~ 2024.09.10

👩🏻‍💻 프로젝트 소개
이 프로젝트는 Django 기초 과제에서 구현한 것들을 Django Rest Framework로 변환한 것입니다. 제품 등록, 제품 목록 조회, 제품 수정, 제품 삭제, 사용자 등록, 로그인, 프로필 조회 기능을 포함하고 있습니다.

💻 개발 환경
프로그래밍 언어   python 3.10
웹 프레임워크   Django 4.2, Djangorestframework
데이터베이스   SQLite
IDE   PyCharm
버전 관리   Git, Github
백엔드   Python, Django, Djangorestframework
데이터베이스   Django ORM, SQLite
POSTMAN   POSTMAN

💻ERD

![main](https://github.com/user-attachments/assets/878d04c1-a448-4cbb-ad77-ee2cf25171c3)

🧬 디렉터리 구조
구조   기능
accounts   사용자 인증 및 계정 관리 기능
articles   게시글(객체) 생성, 수정, 삭제 및 검색
spartamarket_DRF   프로젝트 설정 및 초기화 파일

📌 프로젝트 기능
1. 계정 [회원가입 기능]
회원가입 (CREATE)
URL: /api/register/
Method: POST
데이터 형식: JSON
필수 입력 값: username, password, email, first_name, last_name
응답: 201 Created (성공), 400 Bad Request (실패)
로그인 (LOGIN)
URL: /api/login/
Method: POST
데이터 형식: JSON
필수 입력 값: username, password
응답: 200 OK (성공, JWT 토큰 포함), 401 Unauthorized (실패)
프로필 조회 (LIST)
URL: /api/users/<username>/
Method: GET
필요한 권한: 인증된 사용자
응답: 200 OK (성공), 404 Not Found (사용자 없음)
  
2. 게시글 [게시 기능]
제품 등록 (CREATE)
URL: /api/products/
Method: POST
데이터 형식: JSON
필수 입력 값: title, content, image
필요한 권한: 인증된 사용자
응답: 201 Created (성공), 400 Bad Request (실패)
제품 목록 조회 (LIST)
URL: /api/products/
Method: GET
응답: 200 OK (성공, 제품 목록 포함)
제품 수정 (UPDATE)
URL: /api/products/<pk>/
Method: PUT
데이터 형식: JSON
필요한 권한: 인증된 사용자, 제품 작성자
응답: 200 OK (성공), 403 Forbidden (권한 없음), 404 Not Found (제품 없음)
제품 삭제 (DELETE)
URL: /api/products/<pk>/
Method: DELETE
필요한 권한: 인증된 사용자, 제품 작성자
응답: 204 No Content (성공), 403 Forbidden (권한 없음), 404 Not Found (제품 없음)
ERD 다이어그램


POSTMAN 테스트
- 회원가입

![회원가입](https://github.com/user-attachments/assets/fdf990e4-af77-433a-b80a-bdc71f5a4b3e)

- 로그인

![로그인](https://github.com/user-attachments/assets/47ad2a21-081b-46a0-9142-4c3f2d587179)

- 프로필 조회
![프로필 조회](https://github.com/user-attachments/assets/35a937a8-9b76-4257-943e-0496fe8c4259)


- 제품 등록

![상품 등록](https://github.com/user-attachments/assets/32201773-6225-40f7-bd47-0f2f4c77451c)

- 제품 목록 조회
![상품 조회](https://github.com/user-attachments/assets/243d3900-6d05-4575-9f14-15f8e07d9fab)


- 제품 수정

![상품 수정](https://github.com/user-attachments/assets/f5426ec1-4085-4a38-8e15-c50fe9fdaa67)

- 제품 삭제
![상품 삭제](https://github.com/user-attachments/assets/8e26bb21-48b9-4c7e-b925-21b5ca4f465f)


개발 및 기여
코드 변경
변경 사항을 커밋하고, 푸시한 후에 Pull Request를 생성해 주세요.
기여
이 프로젝트에 기여하려면 Issues 탭에서 문제를 제기하거나 제안 사항을 남겨 주세요.
