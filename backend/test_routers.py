"""
라우터 관련 테스트
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_chat_router_exists():
    """Chat 라우터가 존재하는지 테스트"""
    response = client.post("/api/chat", json={"message": "테스트"})
    assert response.status_code == 200


def test_chat_router_response_structure():
    """Chat 라우터 응답 구조 테스트"""
    test_message = {"message": "상품 검색 테스트"}
    response = client.post("/api/chat", json=test_message)
    
    assert response.status_code == 200
    response_data = response.json()
    assert "response" in response_data
    assert isinstance(response_data["response"], str)


def test_api_routes_prefix():
    """API 라우트 프리픽스 테스트"""
    # /api/info 엔드포인트가 작동하는지 확인
    response = client.get("/api/info")
    assert response.status_code == 200
    
    # /api/chat 엔드포인트가 작동하는지 확인
    response = client.post("/api/chat", json={"message": "테스트"})
    assert response.status_code == 200 