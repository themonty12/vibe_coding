"""
프로젝트 구조 검증 테스트
"""
import os
import pytest


class TestProjectStructure:
    """프로젝트 폴더 구조 테스트"""
    
    def test_backend_folder_exists(self):
        """backend 폴더가 존재하는지 확인"""
        assert os.path.exists("backend"), "backend 폴더가 존재하지 않습니다"
        assert os.path.isdir("backend"), "backend는 폴더여야 합니다"
    
    def test_frontend_folder_exists(self):
        """frontend 폴더가 존재하는지 확인"""
        assert os.path.exists("frontend"), "frontend 폴더가 존재하지 않습니다"
        assert os.path.isdir("frontend"), "frontend는 폴더여야 합니다"
    
    def test_docs_folder_exists(self):
        """docs 폴더가 존재하는지 확인"""
        assert os.path.exists("docs"), "docs 폴더가 존재하지 않습니다"
        assert os.path.isdir("docs"), "docs는 폴더여야 합니다"
    
    def test_backend_app_folder_exists(self):
        """backend/app 폴더가 존재하는지 확인"""
        assert os.path.exists("backend/app"), "backend/app 폴더가 존재하지 않습니다"
        assert os.path.isdir("backend/app"), "backend/app는 폴더여야 합니다"
    
    def test_backend_app_init_file_exists(self):
        """backend/app/__init__.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/__init__.py"), "backend/app/__init__.py 파일이 존재하지 않습니다"
        assert os.path.isfile("backend/app/__init__.py"), "backend/app/__init__.py는 파일이어야 합니다"
    
    def test_backend_main_file_exists(self):
        """backend/app/main.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/main.py"), "backend/app/main.py 파일이 존재하지 않습니다"
        assert os.path.isfile("backend/app/main.py"), "backend/app/main.py는 파일이어야 합니다"
    
    def test_backend_routers_folder_exists(self):
        """backend/app/routers 폴더가 존재하는지 확인"""
        assert os.path.exists("backend/app/routers"), "backend/app/routers 폴더가 존재하지 않습니다"
        assert os.path.isdir("backend/app/routers"), "backend/app/routers는 폴더여야 합니다"
    
    def test_backend_config_folder_exists(self):
        """backend/app/config 폴더가 존재하는지 확인"""
        assert os.path.exists("backend/app/config"), "backend/app/config 폴더가 존재하지 않습니다"
        assert os.path.isdir("backend/app/config"), "backend/app/config는 폴더여야 합니다"
    
    def test_frontend_app_file_exists(self):
        """frontend/app.py 파일이 존재하는지 확인"""
        assert os.path.exists("frontend/app.py"), "frontend/app.py 파일이 존재하지 않습니다"
        assert os.path.isfile("frontend/app.py"), "frontend/app.py는 파일이어야 합니다"
    
    def test_frontend_components_folder_exists(self):
        """frontend/components 폴더가 존재하는지 확인"""
        assert os.path.exists("frontend/components"), "frontend/components 폴더가 존재하지 않습니다"
        assert os.path.isdir("frontend/components"), "frontend/components는 폴더여야 합니다"
    
    def test_frontend_utils_folder_exists(self):
        """frontend/utils 폴더가 존재하는지 확인"""
        assert os.path.exists("frontend/utils"), "frontend/utils 폴더가 존재하지 않습니다"
        assert os.path.isdir("frontend/utils"), "frontend/utils는 폴더여야 합니다"


class TestRequirementsFiles:
    """requirements.txt 파일 테스트"""
    
    def test_backend_requirements_exists(self):
        """backend/requirements.txt 파일이 존재하는지 확인"""
        assert os.path.exists("backend/requirements.txt"), "backend/requirements.txt 파일이 존재하지 않습니다"
    
    def test_frontend_requirements_exists(self):
        """frontend/requirements.txt 파일이 존재하는지 확인"""
        assert os.path.exists("frontend/requirements.txt"), "frontend/requirements.txt 파일이 존재하지 않습니다"
    
    def test_root_requirements_exists(self):
        """requirements.txt 파일이 존재하는지 확인"""
        assert os.path.exists("requirements.txt"), "requirements.txt 파일이 존재하지 않습니다"


class TestEnvironmentFiles:
    """환경 설정 파일 테스트"""
    
    def test_env_example_exists(self):
        """.env.example 파일이 존재하는지 확인"""
        assert os.path.exists(".env.example"), ".env.example 파일이 존재하지 않습니다"
    
    def test_gitignore_exists(self):
        """.gitignore 파일이 존재하는지 확인"""
        assert os.path.exists(".gitignore"), ".gitignore 파일이 존재하지 않습니다"
    
    def test_backend_config_settings_exists(self):
        """backend/app/config/settings.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/config/settings.py"), "backend/app/config/settings.py 파일이 존재하지 않습니다"
    
    def test_backend_config_init_exists(self):
        """backend/app/config/__init__.py 파일이 존재하는지 확인"""
        assert os.path.exists("backend/app/config/__init__.py"), "backend/app/config/__init__.py 파일이 존재하지 않습니다" 