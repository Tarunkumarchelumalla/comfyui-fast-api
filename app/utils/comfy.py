import httpx
import asyncio
import os
import base64

COMFY_API = "http://127.0.0.1:8188"
COMFY_OUTPUT_DIR = r"C:\Users\tarun\diffusion\ComfyUI\output"

def build_flow(prompt: str):
    return {
  "prompt": {
    "1": {
      "class_type": "CheckpointLoaderSimple",
      "inputs": {
        "ckpt_name": "SD1.5\\v1-5-pruned-emaonly.ckpt"
      }
    },
    "2": {
      "class_type": "CLIPTextEncode",
      "inputs": {
        "text": prompt,
        "clip": ["1", 1]
      }
    },
    "3": {
      "class_type": "EmptyLatentImage",
      "inputs": {
        "width": 512,
        "height": 512,
        "batch_size": 1
      }
    },
    "4": {
      "class_type": "KSampler",
      "inputs": {
        "model": ["1", 0],
        "positive": ["2", 0],
        "negative": ["2", 0],
        "latent_image": ["3", 0],
        "seed": 42,
        "steps": 40,
        "cfg": 7,
        "sampler_name": "euler",
        "scheduler": "normal",
        "denoise": 1.0
      }
    },
    "5": {
      "class_type": "VAEDecode",
      "inputs": {
        "samples": ["4", 0],
        "vae": ["1", 2]
      }
    },
    "6": {
      "class_type": "SaveImage",
      "inputs": {
        "images": ["5", 0],
        "filename_prefix": "generated"
      }
    }
  }
}


async def get_output(prompt_id: str, timeout=30):
    for _ in range(timeout):
        async with httpx.AsyncClient() as client:
            res = await client.get(f"{COMFY_API}/history/{prompt_id}")
            if res.status_code == 200:
                data = res.json()
                if prompt_id in data and data[prompt_id]["outputs"]:
                    return data[prompt_id]
        await asyncio.sleep(1)
    raise TimeoutError("Timed out waiting for image from ComfyUI")

async def send_prompt_to_comfy(prompt: str):
    flow = build_flow(prompt)

    async with httpx.AsyncClient() as client:
        res = await client.post(f"{COMFY_API}/prompt", json=flow)
        res.raise_for_status()
        res_data = res.json()
        prompt_id = res_data.get("prompt_id")

        if not prompt_id:
            raise ValueError("ComfyUI did not return prompt_id")

        output = await get_output(prompt_id)
        filename = output["outputs"]["6"]["images"][0]["filename"]
        image_path = os.path.join(COMFY_OUTPUT_DIR, filename)

        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        return {
            "base64_image": f"data:image/png;base64,{encoded_string}"
        }
