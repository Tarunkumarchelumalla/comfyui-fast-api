from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="ComfyUI Image Generator")

app.include_router(router, prefix="/api")