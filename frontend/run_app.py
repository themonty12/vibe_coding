"""
Streamlit 앱 실행 스크립트
"""
import subprocess
import sys
import os

def run_streamlit_app():
    """Streamlit 앱 실행"""
    try:
        # 현재 디렉토리에서 app.py 실행
        cmd = [sys.executable, "-m", "streamlit", "run", "app.py"]
        
        print("🚀 Streamlit 앱을 시작합니다...")
        print("📱 브라우저에서 http://localhost:8501 에 접속하세요")
        print("⏹️  종료하려면 Ctrl+C를 누르세요")
        
        subprocess.run(cmd)
        
    except KeyboardInterrupt:
        print("\n✅ Streamlit 앱이 정상적으로 종료되었습니다.")
    except Exception as e:
        print(f"❌ 앱 실행 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    run_streamlit_app() 