"""
DuckDuckGo 검색 도구 구현
"""
from langchain_core.tools import tool
from duckduckgo_search import DDGS
from typing import List, Dict
import time
import random
import hashlib
from datetime import datetime, timedelta

# 간단한 캐시 (메모리 기반)
_search_cache = {}
_cache_expiry = {}


@tool
def search_products(query: str) -> str:
    """
    상품 정보를 검색하는 도구입니다.
    
    Args:
        query: 검색할 상품 관련 키워드
        
    Returns:
        검색 결과를 문자열로 반환
    """
    try:
        # 캐시 확인
        cache_key = hashlib.md5(query.encode()).hexdigest()
        current_time = datetime.now()
        
        # 캐시된 결과가 있고 만료되지 않았다면 반환
        if (cache_key in _search_cache and 
            cache_key in _cache_expiry and 
            current_time < _cache_expiry[cache_key]):
            return f"[캐시된 결과] {_search_cache[cache_key]}"
        
        # Rate Limit 회피를 위한 랜덤 지연
        delay = random.uniform(1.0, 3.0)
        time.sleep(delay)
        
        # DuckDuckGo 검색 실행 (개선된 설정)
        ddgs = DDGS(
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            },
            timeout=10
        )
        
        results = ddgs.text(
            keywords=f"{query} 가격 구매 쇼핑",
            region='kr-kr',
            safesearch='moderate',
            max_results=3,
            backend='api'
        )
        
        if not results:
            return "검색 결과를 찾을 수 없습니다. 다른 검색어를 시도해보세요."
        
        # 검색 결과를 포맷팅
        formatted_results = []
        for i, result in enumerate(results, 1):
            title = result.get('title', '제목 없음')
            href = result.get('href', '')
            body = result.get('body', '설명 없음')
            
            formatted_result = f"""
{i}. {title}
   URL: {href}
   설명: {body[:200]}{'...' if len(body) > 200 else ''}
"""
            formatted_results.append(formatted_result)
        
        result_text = f"상품 검색 결과:\n{''.join(formatted_results)}"
        
        # 결과를 캐시에 저장 (10분간 유효)
        _search_cache[cache_key] = result_text
        _cache_expiry[cache_key] = current_time + timedelta(minutes=10)
        
        return result_text
        
    except Exception as e:
        error_msg = str(e)
        
        # Rate Limit 오류 처리
        if "202" in error_msg or "Ratelimit" in error_msg:
            return """
⚠️ 현재 검색 서비스가 일시적으로 제한되어 있습니다.

대안 정보를 제공해드리겠습니다:
- 네이버 쇼핑: https://shopping.naver.com
- 쿠팡: https://www.coupang.com  
- 11번가: https://www.11st.co.kr
- G마켓: https://www.gmarket.co.kr

위 쇼핑몰에서 직접 검색해보시거나, 잠시 후 다시 시도해주세요.
"""
        
        return f"검색 중 오류가 발생했습니다: {error_msg}\n잠시 후 다시 시도해주세요."


def create_search_tool():
    """
    검색 도구 생성 함수
    
    Returns:
        search_products 도구
    """
    return search_products 