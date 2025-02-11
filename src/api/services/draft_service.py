import uuid
from typing import List
from src.api.schemas.draft import DraftCreate, DraftResponse
from src.core.pyJianYingDraft import JianYingDraft

class DraftService:
    @staticmethod
    async def create_draft(draft_data: DraftCreate) -> DraftResponse:
        draft_id = str(uuid.uuid4())
        
        # 创建剪映草稿实例
        draft = JianYingDraft()
        
        # 添加媒体文件
        for media_file in draft_data.media_files:
            draft.add_media(media_file)
            
        # 导出草稿
        draft.export(draft_data.output_path)
        
        return DraftResponse(
            id=draft_id,
            title=draft_data.title,
            description=draft_data.description,
            status="completed",
            draft_path=draft_data.output_path
        ) 