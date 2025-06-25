"""
개발용 FastAPI 서버 실행 스크립트
"""
import uvicorn
from app.config.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True,  # 개발 환경에서는 자동 재시작 활성화
        log_level="info"
    ) 