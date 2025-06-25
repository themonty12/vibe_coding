"""
Chat API 라우터
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agent.agent import process_search_query

router = APIRouter(
    prefix="/api/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


# 요청/응답 모델 정의
class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    status: str = "success"


@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat API 엔드포인트 - LangGraph Agent 연동"""
    try:
        # Agent를 통한 검색 쿼리 처리
        result = process_search_query(request.message)
        
        return ChatResponse(
            response=result['response'],
            status=result['status']
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"서버 내부 오류: {str(e)}"
        )


@router.post("/search", response_model=ChatResponse)
async def search_products_endpoint(request: ChatRequest):
    """상품 검색 전용 엔드포인트"""
    try:
        # Agent를 통한 상품 검색
        result = process_search_query(request.message)
        
        return ChatResponse(
            response=result['response'],
            status=result['status']
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"검색 처리 오류: {str(e)}"
        ) 