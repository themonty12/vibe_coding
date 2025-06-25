"""
LangGraph React Agent 구현
"""
import os
from typing import Dict, Any
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

from .model import create_gemini_model
from .tools import create_search_tool

# 환경 변수 로드
load_dotenv()


def create_product_search_agent():
    """
    상품 검색을 위한 React Agent 생성
    
    Returns:
        LangGraph React Agent
    """
    # LangSmith 설정 (선택사항)
    langsmith_api_key = os.getenv('LANGSMITH_API_KEY')
    if langsmith_api_key:
        os.environ['LANGSMITH_TRACING'] = 'true'
        os.environ['LANGSMITH_PROJECT'] = 'vibe-coding-w2-1'
    
    # Gemini 모델 생성
    model = create_gemini_model()
    
    # 검색 도구 생성
    search_tool = create_search_tool()
    tools = [search_tool]
    
    # 시스템 프롬프트 정의
    system_prompt = """
당신은 상품 검색 전문 AI 어시스턴트입니다.

역할:
- 사용자가 원하는 상품의 최저가격을 찾기 위해 웹 검색을 수행합니다
- 각 쇼핑몰에서 검색한 결과를 가지고 최저가격을 찾아서 알려줍니다
- 가격, 구매처 등을 요약해서 알려줍니다

지침:
1. 사용자의 질문을 분석하여 적절한 검색 키워드를 생성하세요
2. search_products 도구를 사용하여 상품 정보를 검색하세요
3. 검색 결과를 바탕으로 유용하고 정확한 정보를 제공하세요
4. 한국어로 친근하게 응답하세요
5. 검색 결과가 없거나 부족한 경우 다른 키워드로 재검색을 시도하세요

응답 형식:
- 가격 정보와 구매 사이트 링크를 포함

"""
    
    # React Agent 생성
    agent = create_react_agent(
        model=model,
        tools=tools,
        prompt=system_prompt
    )
    
    return agent


def process_search_query(query: str) -> Dict[str, Any]:
    """
    검색 쿼리 처리 함수
    
    Args:
        query: 사용자 검색 쿼리
        
    Returns:
        처리 결과 딕셔너리
    """
    try:
        # Agent 생성
        agent = create_product_search_agent()
        
        # 메시지 생성
        messages = [HumanMessage(content=query)]
        
        # Agent 실행 (단일 턴)
        response = agent.invoke({"messages": messages})
        
        # 응답 추출
        if response and 'messages' in response:
            last_message = response['messages'][-1]
            if hasattr(last_message, 'content'):
                return {
                    'response': last_message.content,
                    'status': 'success'
                }
        
        return {
            'response': '응답을 생성할 수 없습니다.',
            'status': 'error'
        }
        
    except Exception as e:
        return {
            'response': f'처리 중 오류가 발생했습니다: {str(e)}',
            'status': 'error'
        } 