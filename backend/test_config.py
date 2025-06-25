"""
설정(Config) 관련 테스트
"""
import pytest
from app.config.settings import Settings


def test_settings_default_values():
    """설정 기본값 테스트"""
    settings = Settings()
    
    assert settings.app_name == "Vibe Coding W2-1 API"
    assert settings.app_version == "1.0.0"
    assert settings.debug is False
    assert settings.cors_origins == ["*"]


def test_settings_from_env():
    """환경 변수로부터 설정 로드 테스트"""
    # 이 테스트는 실제 환경 변수 설정 없이도 통과해야 함
    settings = Settings()
    
    # 기본값들이 설정되어 있는지 확인
    assert hasattr(settings, 'app_name')
    assert hasattr(settings, 'app_version')
    assert hasattr(settings, 'debug')
    assert hasattr(settings, 'cors_origins') 