"""
Rate Limit 해결 방안 테스트
"""
import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# 테스트를 위해 현재 디렉토리를 path에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.agent.tools import search_products


class TestRateLimitFix:
    """Rate Limit 해결 방안 테스트 클래스"""
    
    def test_search_products_function_exists(self):
        """search_products 함수가 존재하는지 테스트"""
        assert search_products is not None
        assert callable(search_products)
    
    @patch('app.agent.tools.DDGS')
    @patch('app.agent.tools.time.sleep')
    def test_search_with_delay(self, mock_sleep, mock_ddgs):
        """지연 시간이 적용되는지 테스트"""
        # Mock 설정
        mock_ddgs_instance = MagicMock()
        mock_ddgs.return_value = mock_ddgs_instance
        mock_ddgs_instance.text.return_value = [
            {
                'title': '테스트 상품',
                'href': 'https://test.com',
                'body': '테스트 설명'
            }
        ]
        
        # 함수 호출
        result = search_products.func("테스트")  # .func로 tool 함수 직접 호출
        
        # 검증
        mock_sleep.assert_called_once()  # sleep이 호출되었는지 확인
        assert "상품 검색 결과" in result
    
    @patch('app.agent.tools.DDGS')
    def test_rate_limit_error_handling(self, mock_ddgs):
        """Rate Limit 오류 처리 테스트"""
        # 캐시 초기화
        from app.agent.tools import _search_cache, _cache_expiry
        _search_cache.clear()
        _cache_expiry.clear()
        
        # Mock 에러 설정
        mock_ddgs.side_effect = Exception("202 Ratelimit")
        
        # 함수 호출
        result = search_products.func("rate_limit_test_unique")
        
        # 검증
        assert "일시적으로 제한" in result
        assert "네이버 쇼핑" in result
    
    def test_cache_functionality(self):
        """캐시 기능 테스트"""
        from app.agent.tools import _search_cache, _cache_expiry
        
        # 캐시가 초기화되었는지 확인
        assert isinstance(_search_cache, dict)
        assert isinstance(_cache_expiry, dict)
    
    @patch('app.agent.tools.DDGS')
    def test_korean_region_setting(self, mock_ddgs):
        """한국 지역 설정 테스트"""
        # 캐시 초기화
        from app.agent.tools import _search_cache, _cache_expiry
        _search_cache.clear()
        _cache_expiry.clear()
        
        # Mock 설정
        mock_ddgs_instance = MagicMock()
        mock_ddgs.return_value = mock_ddgs_instance
        mock_ddgs_instance.text.return_value = []
        
        # 함수 호출
        search_products.func("korean_region_test_unique")
        
        # 검증: 한국 지역(kr-kr)으로 설정되었는지 확인
        mock_ddgs_instance.text.assert_called_once()
        args, kwargs = mock_ddgs_instance.text.call_args
        assert kwargs.get('region') == 'kr-kr' 