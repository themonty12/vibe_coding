"""
Streamlit 프론트엔드 애플리케이션

PR 테스트: GitHub Actions 자동화 확인
- 자동 라벨링 테스트
- 자동 댓글 기능 테스트
- PR 크기 분류 테스트
"""
import streamlit as st
import requests
import json


def call_backend_api(user_message):
    """백엔드 API 호출 함수"""
    try:
        backend_url = "http://localhost:8000/api/chat/"
        payload = {"message": user_message}
        
        response = requests.post(
            backend_url,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"백엔드 서버 오류: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        st.error("백엔드 서버에 연결할 수 없습니다. 서버가 실행 중인지 확인해주세요.")
        return None
    except requests.exceptions.Timeout:
        st.error("요청 시간이 초과되었습니다. 다시 시도해주세요.")
        return None
    except Exception as e:
        st.error(f"예상치 못한 오류가 발생했습니다: {str(e)}")
        return None


def format_response(response_data):
    """응답 데이터 포맷팅 함수"""
    if response_data is None:
        return "서비스 오류가 발생했습니다. 잠시 후 다시 시도해주세요."
    
    if isinstance(response_data, dict) and "response" in response_data:
        return response_data["response"]
    
    return "응답 형식에 오류가 있습니다."


def display_chat_info():
    """채팅 정보 표시 함수"""
    return "💡 상품명을 입력하시면 AI가 관련 상품을 검색해드립니다!"


def clear_chat_history():
    """채팅 히스토리 초기화 함수"""
    if "messages" in st.session_state:
        st.session_state.messages = []
        st.success("채팅 히스토리가 초기화되었습니다!")
        st.rerun()


def main():
    """메인 애플리케이션"""
    st.title("🛍️ 상품 검색 챗봇")
    st.write("Vibe Coding W2-1 프로젝트에 오신 것을 환영합니다!")
    
    # 사이드바에 정보 표시
    with st.sidebar:
        st.header("📋 채팅 정보")
        st.info(display_chat_info())
        
        if st.button("🗑️ 채팅 히스토리 초기화"):
            clear_chat_history()
        
        st.divider()
        st.caption("💻 개발: Vibe Coding W2-1")
    
    # 세션 상태 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # 채팅 히스토리 표시
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # 사용자 입력 처리
    if prompt := st.chat_input("상품을 검색해보세요!"):
        # 사용자 메시지 표시 및 저장
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # AI 응답 처리
        with st.chat_message("assistant"):
            # 로딩 상태 표시
            with st.spinner("상품을 검색하고 있습니다..."):
                # 백엔드 API 호출
                response_data = call_backend_api(prompt)
                
                # 응답 포맷팅 및 표시
                formatted_response = format_response(response_data)
                st.markdown(formatted_response)
                
                # 응답을 세션에 저장
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": formatted_response
                })


if __name__ == "__main__":
    main() 