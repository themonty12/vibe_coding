#!/usr/bin/env python3
"""
API 테스트 스크립트
"""
import requests
import json
import time

def test_api():
    """API 엔드포인트 테스트"""
    base_url = "http://localhost:8000"
    
    # 서버 대기
    print("서버 시작 대기 중...")
    time.sleep(3)
    
    try:
        # Health check
        print("1. Health check 테스트...")
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✓ Health check 성공")
        else:
            print(f"❌ Health check 실패: {response.status_code}")
            return False
        
        # Root endpoint
        print("2. Root 엔드포인트 테스트...")
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✓ Root 엔드포인트 성공")
        else:
            print(f"❌ Root 엔드포인트 실패: {response.status_code}")
            
        # API Info
        print("3. API Info 테스트...")
        response = requests.get(f"{base_url}/api/info")
        if response.status_code == 200:
            print("✓ API Info 성공")
            print(f"   응답: {response.json()}")
        else:
            print(f"❌ API Info 실패: {response.status_code}")
        
        # Chat 엔드포인트 테스트 (간단한 메시지)
        print("4. Chat 엔드포인트 기본 테스트...")
        chat_data = {
            "message": "안녕하세요"
        }
        
        response = requests.post(
            f"{base_url}/api/chat/",
            json=chat_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✓ Chat 엔드포인트 성공")
            print(f"   응답 길이: {len(result.get('response', ''))}")
            print(f"   상태: {result.get('status', 'unknown')}")
        else:
            print(f"❌ Chat 엔드포인트 실패: {response.status_code}")
            print(f"   에러: {response.text}")
        
        print("\n✅ API 테스트 완료!")
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인하세요.")
        return False
    except Exception as e:
        print(f"❌ 테스트 실패: {e}")
        return False

if __name__ == "__main__":
    test_api() 