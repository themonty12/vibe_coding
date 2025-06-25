"""
Streamlit 앱 통합 테스트
"""
import pytest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import app


class TestStreamlitIntegration:
    """Streamlit 앱 통합 테스트 클래스"""
    
    def test_app_imports_successfully(self):
        """앱이 성공적으로 임포트되는지 테스트"""
        assert app is not None
        
    def test_all_required_functions_exist(self):
        """필요한 모든 함수가 존재하는지 테스트"""
        required_functions = [
            'main',
            'call_backend_api',
            'format_response',
            'display_chat_info',
            'clear_chat_history'
        ]
        
        for func_name in required_functions:
            assert hasattr(app, func_name), f"함수 {func_name}이 존재하지 않습니다"
            assert callable(getattr(app, func_name)), f"함수 {func_name}이 호출 가능하지 않습니다"
    
    @patch('requests.post')
    def test_complete_chat_flow_success(self, mock_post):
        """성공적인 채팅 플로우 전체 테스트"""
        # Mock 응답 설정
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "response": "아이폰 15 Pro 128GB - 가격: 1,350,000원, 색상: 자연 티타늄, 블루 티타늄 등 4가지"
        }
        mock_post.return_value = mock_response
        
        # 1. API 호출 테스트
        api_result = app.call_backend_api("아이폰 15")
        assert api_result is not None
        assert "response" in api_result
        
        # 2. 응답 포맷팅 테스트
        formatted_result = app.format_response(api_result)
        assert isinstance(formatted_result, str)
        assert "아이폰 15" in formatted_result
        
        # 3. 전체 플로우가 에러 없이 실행되는지 확인
        assert len(formatted_result) > 0
    
    @patch('requests.post')  
    def test_complete_chat_flow_failure(self, mock_post):
        """실패하는 채팅 플로우 전체 테스트"""
        # Mock 에러 설정
        mock_post.side_effect = Exception("서버 에러")
        
        # 1. API 호출 실패 테스트
        api_result = app.call_backend_api("테스트 상품")
        assert api_result is None
        
        # 2. 실패 응답 포맷팅 테스트
        formatted_result = app.format_response(api_result)
        assert isinstance(formatted_result, str)
        assert "오류" in formatted_result
        
        # 3. 에러 상황에서도 적절한 메시지가 반환되는지 확인
        assert len(formatted_result) > 0
    
    def test_ui_helper_functions(self):
        """UI 헬퍼 함수들 테스트"""
        # 채팅 정보 표시 함수 테스트
        info_result = app.display_chat_info()
        assert isinstance(info_result, str)
        assert len(info_result) > 0
        assert "상품" in info_result or "검색" in info_result 