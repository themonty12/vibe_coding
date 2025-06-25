"""
Gemini LLM 모델 설정
"""
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()


def create_gemini_model():
    """
    Gemini 모델 생성 함수
    
    Returns:
        ChatGoogleGenerativeAI 모델 인스턴스
    """
    # 환경 변수에서 API 키 가져오기
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        raise ValueError("GOOGLE_API_KEY 환경 변수가 설정되지 않았습니다.")
    
    # Gemini 모델 생성
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",  # 최신 Gemini 모델 사용
        google_api_key=api_key,
        temperature=0.7,
        max_tokens=1024,
        convert_system_message_to_human=True
    )
    
    return model 