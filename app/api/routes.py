from fastapi import APIRouter, Query, HTTPException
from app.utils.comfy import send_prompt_to_comfy
from app.utils.logger import debug
router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

@router.post("/generate")
async def generate(prompt: str = Query(..., description="Text prompt for image generation")):
    """
    Send a prompt to ComfyUI and return generated image path
    """
    try:
        image_info = await send_prompt_to_comfy(prompt)
        debug(image_info)
        return {
            "message": "Image generated",
            "output_file": image_info["base64_image"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))