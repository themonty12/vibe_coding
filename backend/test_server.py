#!/usr/bin/env python3
"""
테스트용 서버 실행 스크립트
"""
import os
import uvicorn

# 필수 환경 변수 설정 (테스트용)
os.environ['GOOGLE_API_KEY'] = 'test_key_for_demo'
os.environ['LANGSMITH_API_KEY'] = 'test_langsmith_key'

def run_test_server():
    """테스트 서버 실행"""
    print("테스트 서버를 시작합니다...")
    print("주의: 실제 API 키 없이 데모 모드로 실행됩니다.")
    
    try:
        uvicorn.run(
            "app.main:app",
            host="localhost",
            port=8000,
            reload=False,  # 테스트용이므로 reload 비활성화
            log_level="info"
        )
    except Exception as e:
        print(f"서버 실행 오류: {e}")

if __name__ == "__main__":
    run_test_server() 