"""
FastAPI 메인 애플리케이션

GitHub Actions 자동화 테스트를 위한 간단한 수정
이 수정으로 PR 자동화 기능들을 테스트합니다.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.routers import chat

app = FastAPI(
    title=settings.app_name,
    description="LangGraph Agent와 연동된 상품 검색 API",
    version=settings.app_version,
    debug=settings.debug
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(chat.router)


@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {"message": "Vibe Coding W2-1 API가 실행 중입니다!"}


@app.get("/health")
async def health_check():
    """Health check 엔드포인트"""
    return {"status": "healthy", "version": settings.app_version}


@app.get("/api/info")
async def api_info():
    """API 정보 엔드포인트"""
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "description": "LangGraph Agent와 연동된 상품 검색 API"
    } 