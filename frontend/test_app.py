"""
Streamlit 프론트엔드 테스트
"""
import pytest
import requests
from unittest.mock import patch, MagicMock
import sys
import os

# 테스트를 위해 현재 디렉토리를 path에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import app


class TestStreamlitApp:
    """Streamlit 앱 테스트 클래스"""
    
    def test_main_function_exists(self):
        """main 함수가 존재하는지 테스트"""
        assert hasattr(app, 'main')
        assert callable(app.main)
    
    def test_backend_api_call_function_exists(self):
        """백엔드 API 호출 함수가 존재하는지 테스트"""
        assert hasattr(app, 'call_backend_api')
        assert callable(app.call_backend_api)
    
    def test_format_response_function_exists(self):
        """응답 포맷팅 함수가 존재하는지 테스트"""
        assert hasattr(app, 'format_response')
        assert callable(app.format_response)
    
    @patch('requests.post')
    def test_backend_api_call_success(self, mock_post):
        """백엔드 API 호출 성공 테스트"""
        # Mock 응답 설정
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "response": "테스트 상품 검색 결과입니다."
        }
        mock_post.return_value = mock_response
        
        # 함수 호출
        result = app.call_backend_api("테스트 상품")
        
        # 검증
        assert result is not None
        assert "response" in result
        mock_post.assert_called_once()
    
    @patch('requests.post')
    def test_backend_api_call_failure(self, mock_post):
        """백엔드 API 호출 실패 테스트"""
        # Mock 에러 설정
        mock_post.side_effect = requests.exceptions.ConnectionError("Connection failed")
        
        # 함수 호출
        result = app.call_backend_api("테스트 상품")
        
        # 검증
        assert result is None
    
    def test_format_response_with_valid_data(self):
        """유효한 데이터로 응답 포맷팅 테스트"""
        test_data = {
            "response": "상품 검색 결과입니다."
        }
        
        result = app.format_response(test_data)
        
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_format_response_with_invalid_data(self):
        """잘못된 데이터로 응답 포맷팅 테스트"""
        result = app.format_response(None)
        
        assert isinstance(result, str)
        assert "오류" in result or "에러" in result 