"""
UI 개선사항 테스트
"""
import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import app


class TestUIEnhancements:
    """UI 개선사항 테스트 클래스"""
    
    def test_display_chat_info_function_exists(self):
        """채팅 정보 표시 함수가 존재하는지 테스트"""
        assert hasattr(app, 'display_chat_info')
        assert callable(app.display_chat_info)
    
    def test_clear_chat_function_exists(self):
        """채팅 히스토리 초기화 함수가 존재하는지 테스트"""
        assert hasattr(app, 'clear_chat_history')
        assert callable(app.clear_chat_history)
    
    def test_display_chat_info_returns_string(self):
        """채팅 정보 표시 함수가 문자열을 반환하는지 테스트"""
        result = app.display_chat_info()
        assert isinstance(result, str)
        assert len(result) > 0 