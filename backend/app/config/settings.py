"""
애플리케이션 설정
"""
import os
from typing import Optional, List
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()


class Settings:
    """애플리케이션 설정 클래스"""
    
    def __init__(self):
        """환경 변수를 동적으로 로드하는 초기화 메서드"""
        # 앱 기본 정보
        self.app_name: str = os.getenv("APP_NAME", "Vibe Coding W2-1 API")
        self.app_version: str = os.getenv("APP_VERSION", "1.0.0")
        self.debug: bool = os.getenv("DEBUG", "false").lower() == "true"
        
        # CORS 설정
        cors_origins_str = os.getenv("CORS_ORIGINS", "*")
        self.cors_origins: List[str] = [cors_origins_str] if cors_origins_str == "*" else cors_origins_str.split(",")
        
        # Gemini API 설정
        self.GOOGLE_API_KEY: Optional[str] = os.getenv("GOOGLE_API_KEY")
        
        # LangSmith 설정
        self.LANGCHAIN_TRACING_V2: str = os.getenv("LANGCHAIN_TRACING_V2", "false")
        self.LANGCHAIN_API_KEY: Optional[str] = os.getenv("LANGCHAIN_API_KEY")
        self.LANGCHAIN_PROJECT: str = os.getenv("LANGCHAIN_PROJECT", "vibe-coding-w2-1")
        
        # FastAPI 설정
        self.API_HOST: str = os.getenv("API_HOST", "localhost")
        self.API_PORT: int = int(os.getenv("API_PORT", "8000"))
        
        # Streamlit 설정
        self.FRONTEND_HOST: str = os.getenv("FRONTEND_HOST", "localhost")
        self.FRONTEND_PORT: int = int(os.getenv("FRONTEND_PORT", "8501"))
    
    def validate_required_settings(self) -> bool:
        """필수 설정값 검증"""
        if not self.GOOGLE_API_KEY:
            return False
        return True


# 전역 설정 인스턴스
settings = Settings() 