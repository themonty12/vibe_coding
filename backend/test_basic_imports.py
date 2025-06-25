#!/usr/bin/env python3
"""
기본 임포트 테스트 스크립트
"""
import sys
import os

# 환경 변수 모킹
os.environ['GOOGLE_API_KEY'] = 'test_key'
os.environ['LANGSMITH_API_KEY'] = 'test_langsmith_key'

def test_imports():
    """기본 임포트 테스트"""
    try:
        # Tools 모듈 테스트
        from app.agent.tools import create_search_tool, search_products
        print('✓ Tools 모듈 임포트 성공')
        
        # Model 모듈 테스트
        from app.agent.model import create_gemini_model
        print('✓ Model 모듈 임포트 성공')
        
        # Agent 모듈 테스트
        from app.agent.agent import create_product_search_agent, process_search_query
        print('✓ Agent 모듈 임포트 성공')
        
        # 도구 생성 테스트
        tool = create_search_tool()
        print(f'✓ 검색 도구 생성 성공: {tool.name}')
        print(f'✓ 검색 도구 설명: {tool.description[:50]}...')
        
        print('\n✅ 모든 기본 테스트 통과!')
        return True
        
    except Exception as e:
        print(f'❌ 테스트 실패: {e}')
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_imports() 