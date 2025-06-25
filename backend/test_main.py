"""
FastAPI 애플리케이션 테스트
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    """루트 엔드포인트 테스트"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Vibe Coding W2-1 API가 실행 중입니다!"}


def test_health_check():
    """Health check 엔드포인트 테스트"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "version": "1.0.0"}


def test_api_info():
    """API 정보 엔드포인트 테스트"""
    response = client.get("/api/info")
    assert response.status_code == 200
    assert "name" in response.json()
    assert "version" in response.json()


def test_chat_endpoint():
    """Chat API 엔드포인트 테스트"""
    test_message = {"message": "테스트 상품을 찾아주세요"}
    response = client.post("/api/chat", json=test_message)
    assert response.status_code == 200
    assert "response" in response.json()
    assert isinstance(response.json()["response"], str)


def test_chat_endpoint_invalid_data():
    """Chat API 잘못된 데이터 테스트"""
    response = client.post("/api/chat", json={})
    assert response.status_code == 422  # Unprocessable Entity 