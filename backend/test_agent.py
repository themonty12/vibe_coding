"""
LangGraph Agent 테스트
"""
import pytest
from unittest.mock import Mock, patch
import os


class TestAgentEnvironment:
    """Agent 환경 설정 테스트"""
    
    def test_environment_variables_loaded(self):
        """환경 변수가 올바르게 로드되는지 테스트"""
        # Given: 환경 변수가 설정되어 있을 때
        with patch.dict(os.environ, {
            'GOOGLE_API_KEY': 'test_api_key',
            'LANGSMITH_API_KEY': 'test_langsmith_key'
        }):
            # When: 환경 변수를 확인할 때
            google_key = os.getenv('GOOGLE_API_KEY')
            langsmith_key = os.getenv('LANGSMITH_API_KEY')
            
            # Then: 올바른 값이 반환되어야 함
            assert google_key == 'test_api_key'
            assert langsmith_key == 'test_langsmith_key'


class TestDuckDuckGoTool:
    """DuckDuckGo 검색 도구 테스트"""
    
    def test_search_tool_creation(self):
        """검색 도구가 올바르게 생성되는지 테스트"""
        # Given: DuckDuckGo 검색 도구를 생성할 때
        from app.agent.tools import create_search_tool
        
        # When: 도구를 생성하면
        tool = create_search_tool()
        
        # Then: 도구가 올바르게 생성되어야 함
        assert tool is not None
        assert hasattr(tool, 'name')
        assert hasattr(tool, 'description')
    
    @patch('duckduckgo_search.DDGS')
    def test_search_execution(self, mock_ddgs):
        """검색이 올바르게 실행되는지 테스트"""
        # Given: 모킹된 검색 결과
        mock_ddgs.return_value.text.return_value = [
            {
                'title': '테스트 상품',
                'href': 'https://example.com',
                'body': '테스트 상품 설명'
            }
        ]
        
        from app.agent.tools import search_products
        
        # When: 상품을 검색하면
        result = search_products("테스트 쿼리")
        
        # Then: 검색 결과가 반환되어야 함
        assert result is not None
        assert isinstance(result, str)


class TestGeminiModel:
    """Gemini LLM 모델 테스트"""
    
    def test_model_initialization(self):
        """Gemini 모델이 올바르게 초기화되는지 테스트"""
        # Given: 환경 변수가 설정되어 있을 때
        with patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_key'}):
            from app.agent.model import create_gemini_model
            
            # When: 모델을 생성하면
            model = create_gemini_model()
            
            # Then: 모델이 올바르게 생성되어야 함
            assert model is not None


class TestReactAgent:
    """React Agent 테스트"""
    
    @patch('app.agent.model.create_gemini_model')
    @patch('app.agent.tools.create_search_tool')
    def test_agent_creation(self, mock_tool, mock_model):
        """React Agent가 올바르게 생성되는지 테스트"""
        # Given: 모킹된 모델과 도구
        mock_model.return_value = Mock()
        mock_tool.return_value = Mock()
        
        from app.agent.agent import create_product_search_agent
        
        # When: Agent를 생성하면
        agent = create_product_search_agent()
        
        # Then: Agent가 올바르게 생성되어야 함
        assert agent is not None
    
    @patch('app.agent.agent.create_product_search_agent')
    def test_agent_invoke(self, mock_agent):
        """Agent 호출이 올바르게 작동하는지 테스트"""
        # Given: 모킹된 Agent와 응답
        mock_response = {
            'messages': [
                Mock(content='테스트 응답', type='ai')
            ]
        }
        mock_agent.return_value.invoke.return_value = mock_response
        
        from app.agent.agent import process_search_query
        
        # When: 검색 쿼리를 처리하면
        result = process_search_query("테스트 쿼리")
        
        # Then: 결과가 반환되어야 함
        assert result is not None
        assert 'response' in result


class TestChatRouter:
    """Chat 라우터 테스트"""
    
    @patch('app.agent.agent.process_search_query')
    def test_chat_endpoint(self, mock_process):
        """Chat 엔드포인트가 올바르게 작동하는지 테스트"""
        # Given: 모킹된 처리 함수
        mock_process.return_value = {
            'response': '테스트 응답',
            'status': 'success'
        }
        
        from fastapi.testclient import TestClient
        from app.main import app
        
        client = TestClient(app)
        
        # When: Chat 엔드포인트를 호출하면
        response = client.post("/chat/search", json={
            "message": "테스트 쿼리"
        })
        
        # Then: 성공 응답이 반환되어야 함
        assert response.status_code == 200
        data = response.json()
        assert 'response' in data 