# Vibe Coding Week 2-1 Project

## 🚀 AI Agent Chat Interface

AI 에이전트와 채팅할 수 있는 웹 인터페이스 프로젝트입니다.

## 📋 프로젝트 개요

이 프로젝트는 백엔드 API와 프론트엔드 웹 인터페이스로 구성된 AI 채팅 시스템입니다.

### 주요 기능
- 🤖 AI 에이전트와의 실시간 채팅
- 📱 반응형 웹 인터페이스
- 🔧 RESTful API
- ⚡ 비동기 처리
- 🧪 자동화된 테스트
- 🔄 GitHub 자동화 시스템

## 🏗️ 프로젝트 구조

```
vibe_coding_w2-1/
├── backend/                 # 백엔드 API 서버
│   ├── app/
│   │   ├── agent/          # AI 에이전트 모듈
│   │   ├── config/         # 설정 파일
│   │   ├── routers/        # API 라우터
│   │   └── main.py         # 메인 애플리케이션
│   ├── requirements.txt
│   └── run_server.py       # 서버 실행 스크립트
├── frontend/               # 프론트엔드 웹 인터페이스
│   ├── components/         # UI 컴포넌트
│   ├── utils/             # 유틸리티 함수
│   ├── app.py             # 메인 애플리케이션
│   └── requirements.txt
├── docs/                  # 프로젝트 문서
├── .github/               # GitHub 자동화 설정
└── .cursor/               # 개발 규칙 및 가이드라인
```

## 🛠️ 기술 스택

### 백엔드
- **Framework**: FastAPI
- **Language**: Python 3.8+
- **Features**: 
  - 비동기 API
  - AI 에이전트 통합
  - CORS 지원
  - 자동 API 문서화

### 프론트엔드
- **Framework**: Streamlit
- **Language**: Python
- **Features**:
  - 실시간 채팅 인터페이스
  - 반응형 디자인
  - 사용자 친화적 UI

### DevOps & 자동화
- **CI/CD**: GitHub Actions
- **의존성 관리**: Dependabot
- **코드 품질**: 자동 테스트, 코드 리뷰
- **프로젝트 관리**: 자동 이슈/PR 관리

## 🚀 빠른 시작

### 전체 시스템 실행

```bash
# 1. 저장소 클론
git clone https://github.com/themonty12/vibe_coding.git
cd vibe_coding

# 2. 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 환경변수 설정
cp .env.example .env
# .env 파일에서 필요한 값들을 설정하세요

# 5. 백엔드 서버 실행
cd backend
python run_server.py

# 6. 새 터미널에서 프론트엔드 실행
cd frontend
python run_app.py
```

### 개별 서비스 실행

#### 백엔드만 실행
```bash
cd backend
pip install -r requirements.txt
python run_server.py
```

#### 프론트엔드만 실행
```bash
cd frontend
pip install -r requirements.txt
python run_app.py
```

## 🧪 테스트

```bash
# 전체 테스트 실행
python -m pytest

# 백엔드 테스트
cd backend
python -m pytest

# 프론트엔드 테스트
cd frontend
python -m pytest

# 프로젝트 구조 테스트
python test_project_structure.py
```

## 📖 API 문서

백엔드 서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🤝 기여하기

1. 이 저장소를 Fork 합니다
2. 새 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋합니다 (`git commit -m 'feat: Add amazing feature'`)
4. 브랜치에 Push 합니다 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성합니다

### 커밋 메시지 규칙

- `feat`: 새로운 기능 추가
- `fix`: 버그 수정
- `docs`: 문서 수정
- `style`: 코드 포맷팅
- `refactor`: 코드 리팩토링
- `test`: 테스트 코드 추가/수정
- `chore`: 빌드 업무 수정

## 📋 개발 가이드라인

- [개발 원칙](.cursor/rules/development-policy.mdc)
- [프로젝트 구조](.cursor/rules/project-structure.mdc)
- [기술 스택](.cursor/rules/tech-stack.mdc)
- [GitHub 관리 룰](.cursor/rules/github-management.mdc)

## 🔧 환경 설정

### 필수 환경변수

```env
# AI 에이전트 설정
OPENAI_API_KEY=your_openai_api_key_here

# 서버 설정
BACKEND_HOST=localhost
BACKEND_PORT=8000
FRONTEND_PORT=8501

# 개발 모드
DEBUG=True
```

## 📊 GitHub Actions 자동화

- ✅ **자동 테스트**: 모든 push와 PR에서 테스트 실행
- 🏷️ **자동 라벨링**: PR/이슈 자동 분류
- 👥 **자동 할당**: 파일 경로에 따른 리뷰어 할당
- 📝 **자동 댓글**: PR/이슈 생성 시 안내 메시지
- 🔄 **의존성 업데이트**: 매주 자동 업데이트 PR 생성
- 📋 **Stale 관리**: 비활성 이슈/PR 자동 관리

## 📞 문의

프로젝트에 대한 질문이나 제안사항이 있으시면 [Issues](https://github.com/themonty12/vibe_coding/issues)를 통해 연락해주세요.

## 📄 라이센스

이 프로젝트는 MIT 라이센스 하에 제공됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

⭐ 이 프로젝트가 유용하다면 별표를 눌러주세요! 