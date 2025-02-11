from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routers import draft

app = FastAPI(
    title="pyJianYingDraft API",
    description="剪映草稿文件生成和管理 API",
    version="1.0.0"
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 添加路由
app.include_router(draft.router)

@app.get("/")
async def root():
    return {"message": "欢迎使用 pyJianYingDraft API"} 