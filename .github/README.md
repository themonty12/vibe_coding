# GitHub 자동화 설정

이 디렉토리는 프로젝트의 GitHub 자동화 설정을 포함합니다.

## 📁 구조

```
.github/
├── workflows/           # GitHub Actions 워크플로우
│   ├── test.yml        # 테스트 자동 실행
│   ├── pr-automation.yml   # PR 자동화 (댓글, 할당, 라벨링, 리뷰 요청)
│   ├── issue-automation.yml # 이슈 자동화 (댓글, 할당, 라벨링)
│   ├── stale.yml       # 오래된 이슈/PR 관리
│   └── labels.yml      # 라벨 동기화
├── ISSUE_TEMPLATE/     # 이슈 템플릿
│   ├── bug_report.md   # 버그 리포트 템플릿
│   ├── feature_request.md # 기능 요청 템플릿
│   └── question.md     # 질문 템플릿
├── pull_request_template.md # PR 템플릿
├── dependabot.yml      # 의존성 자동 업데이트
└── README.md          # 이 파일
```

## 🤖 자동화 기능

### 1. 테스트 자동 실행 (`test.yml`)
- **트리거**: push, pull_request (main, develop 브랜치)
- **기능**:
  - 백엔드/프론트엔드 테스트 실행
  - 다중 Python 버전 테스트 (3.8, 3.9, 3.10)
  - 코드 커버리지 측정
  - 통합 테스트 실행

### 2. PR 자동화 (`pr-automation.yml`)
- **트리거**: pull_request (opened, synchronize, reopened, edited)
- **기능**:
  - ✅ **자동 댓글**: PR 생성 시 환영 메시지 및 체크리스트
  - 👥 **자동 할당**: 파일 경로에 따른 리뷰어 자동 할당
  - 🏷️ **자동 라벨링**: 제목, 파일 경로, PR 크기에 따른 라벨 자동 추가
  - 🔍 **코드 리뷰 요청**: 자동 리뷰 요청 댓글

### 3. 이슈 자동화 (`issue-automation.yml`)
- **트리거**: issues (opened, edited, labeled, assigned)
- **기능**:
  - ✅ **자동 댓글**: 이슈 생성 시 안내 메시지
  - 👥 **자동 할당**: 이슈 내용에 따른 담당자 자동 할당
  - 🏷️ **자동 라벨링**: 제목, 내용에 따른 라벨 자동 추가
  - 🚨 **긴급 이슈 알림**: critical 라벨 추가 시 특별 댓글

### 4. Stale 관리 (`stale.yml`)
- **트리거**: 매일 자정 (스케줄)
- **기능**:
  - 30일 비활성 이슈/PR stale 표시
  - 7일 후 자동 닫기
  - 특정 라벨 제외 (pinned, security, critical 등)

### 5. 라벨 동기화 (`labels.yml`)
- **트리거**: main 브랜치 push, 수동 실행
- **기능**:
  - 표준화된 라벨 자동 생성
  - 우선순위, 타입, 컴포넌트, 크기별 라벨 관리

## 🏷️ 라벨 체계

### 우선순위
- `priority/critical` - 즉시 처리 필요
- `priority/high` - 높은 우선순위
- `priority/medium` - 보통 우선순위
- `priority/low` - 낮은 우선순위

### 타입
- `bug` - 버그
- `enhancement` - 기능 개선/추가
- `question` - 질문
- `documentation` - 문서

### 컴포넌트
- `backend` - 백엔드 관련
- `frontend` - 프론트엔드 관련
- `database` - 데이터베이스 관련
- `api` - API 관련

### PR 크기
- `size/XS` - 10줄 미만
- `size/S` - 30줄 미만
- `size/M` - 100줄 미만
- `size/L` - 500줄 미만
- `size/XL` - 500줄 이상

## 📝 템플릿

### PR 템플릿
- 변경사항 요약 및 상세 설명
- 테스트 방법 및 결과
- 체크리스트
- 관련 이슈 링크

### 이슈 템플릿
1. **Bug Report**: 버그 리포트용
2. **Feature Request**: 기능 요청용
3. **Question**: 질문용

## 🔧 Dependabot 설정

- **업데이트 주기**: 매주 월요일 09:00
- **대상**: Python 의존성, GitHub Actions
- **브랜치**: develop
- **자동 라벨링**: dependencies, auto-update

## ⚙️ 설정 방법

### 1. 사용자명 변경
다음 파일들에서 `your-github-username`을 실제 GitHub 사용자명으로 변경하세요:
- `dependabot.yml`
- `pr-automation.yml` (리뷰어 설정 부분)
- `issue-automation.yml` (담당자 설정 부분)

### 2. 리뷰어 설정
`pr-automation.yml`과 `issue-automation.yml`에서 주석 처리된 리뷰어/담당자 설정을 활성화하고 실제 사용자명으로 변경하세요.

### 3. 라벨 생성
처음 사용 시 `.github/workflows/labels.yml` 워크플로우를 수동으로 실행하여 라벨을 생성하세요.

## 🚀 사용법

1. **PR 생성**: 자동으로 댓글, 라벨, 리뷰어 할당
2. **이슈 생성**: 자동으로 댓글, 라벨, 담당자 할당
3. **테스트**: push/PR 시 자동 실행
4. **의존성 업데이트**: 매주 자동 PR 생성

## 📋 주의사항

- 첫 사용 시 GitHub repository 설정에서 Actions 권한을 확인하세요
- 브랜치 보호 규칙 설정을 권장합니다
- 팀원들에게 템플릿 사용법을 안내하세요 