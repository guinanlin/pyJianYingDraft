from fastapi import APIRouter, HTTPException
from src.api.schemas.draft import DraftCreate, DraftResponse
from src.api.services.draft_service import DraftService

router = APIRouter(
    prefix="/drafts",
    tags=["drafts"],
    responses={404: {"description": "未找到"}},
)

@router.post("/", response_model=DraftResponse)
async def create_draft(draft_data: DraftCreate):
    try:
        return await DraftService.create_draft(draft_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 