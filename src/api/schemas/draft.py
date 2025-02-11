from pydantic import BaseModel
from typing import List, Optional

class DraftBase(BaseModel):
    title: str
    description: Optional[str] = None

class DraftCreate(DraftBase):
    media_files: List[str]
    output_path: str

class DraftResponse(DraftBase):
    id: str
    status: str
    draft_path: str

    class Config:
        from_attributes = True 