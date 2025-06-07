# Orderin

카페 현장 및 전화 예약, 주문 관리가 가능한 백오피스 시스템입니다.  
실제 카페 POS와 키오스크 사용 경험을 바탕으로,  
실무에서 필요한 기능을 중심으로 기획하고 개발한 FastAPI 기반 백엔드 프로젝트입니다.

---

## 🔧 기술 스택

- **Language**: Python 3.12
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite (추후 PostgreSQL 가능)
- **Auth**: JWT (Python-Jose, Passlib)
- **Package Management**: Poetry
- **Docs**: Swagger (FastAPI 자동 문서)
- **Version Control**: Git / GitHub

---

## 📌 핵심 기능

- ✅ 관리자 로그인 (JWT 기반)
- ✅ 메뉴 CRUD (등록, 수정, 삭제)
- ✅ 예약 등록 및 조회 (전화/현장 예약 처리)
- ✅ 주문 생성 및 상태 변경 (제조 중 / 완료)
- ✅ 주문 리스트 실시간 조회
- 🔄 확장 예정:
  - 예약 중복 확인
  - 포인트 & 쿠폰 시스템
  - 주문 통계 API
  - 결제 처리 (현금/카드)
  - PDF 주문서 출력

---

## 🧠 프로젝트 목적

> “카페에서 실제로 사용할 수 있을 법한 실용적인 백오피스를 만들어 보자.”

- 카페 POS/Kiosk 실무 경험을 바탕으로 실제 사용 시 불편했던 점들을 개선
- 백엔드 개발자로서 실무형 설계/구현 경험을 쌓는 것에 집중

---

## ⚙️ 폴더 구조 (요약)

```bash
app/
├── api/v1/           # 라우터 (menu, order, auth 등)
├── core/             # 설정, 보안
├── crud/             # DB 연산 로직
├── db/               # 세션 및 초기화
├── models/           # SQLAlchemy 모델
├── schemas/          # Pydantic 스키마
├── deps/             # Depends 관련 유틸
└── main.py           # FastAPI 실행 진입점
```

---

## 🛠️ 개발 현황

- [x] 프로젝트 구조 설계
- [x] 기술 스택 선정
- [x] 핵심 기능 정의
- [x] ERD 초안 설계
- [ ] API 명세서 작성
- [ ] 모델 및 CRUD 작성
- [ ] JWT 로그인 구현
- [ ] 예약 기능 구현
- [ ] 관리자 UI 연동 (선택)

---

## ✍️ 개발자

- 김효영 (hyo00000)  
- 백엔드 개발자 전환 준비 중 / 카페 실무 경험 기반 프로젝트 기획

---

## 🚀 실행 방법 (로컬 개발)

```bash
poetry install
poetry shell
uvicorn main:app --reload
```

---

## 📄 ERD

📌 (ERD 시각화 링크 또는 이미지 삽입 예정)