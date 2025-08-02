
# 🧠 FastAPI × ComfyUI — Image Generator API

This project is a minimal FastAPI wrapper for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), enabling users to generate 512×512 AI images using a text prompt through a simple API endpoint.

---

## 📦 Features

- Accepts a text prompt via `/api/generate`
- Sends it to a local ComfyUI server at `http://127.0.0.1:8188`
- Returns the generated image in base64 format
- Custom ComfyUI flow with minimal nodes for fast image generation

---

## 🛠️ Requirements

- Python 3.9+
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) installed and running locally
- A compatible model checkpoint (e.g., `v1-5-pruned-emaonly.ckpt`) loaded in ComfyUI
- `output/` directory path correctly set in your FastAPI script (e.g., `C:/Users/tarun/diffusion/ComfyUI/output`)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Tarunkumarchelumalla/comfyui-fast-api/tree/main
cd comfyui-fastapi-api
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate       # For Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server

```bash
uvicorn main:app --reload
```

---

## 🎯 Usage

### Endpoint

`POST /api/generate?prompt=<your_prompt>`

#### Example

```bash
curl -X POST "http://127.0.0.1:8000/api/generate?prompt=a futuristic cyberpunk street with dog"
```

#### Response

```json
{
  "base64_image": "iVBORw0KGgoAAAANSUhEUgAA..."
}
```

You can decode this base64 string into an image using any viewer or frontend app.

---

## 🧠 Project Structure

```
.
├── main.py                # FastAPI app with /api/generate route
├── utils/
│   └── comfy.py          # Functions to send and fetch prompt data from ComfyUI
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🧾 .gitignore

```gitignore
venv/
__pycache__/
*.pyc
output/
.env
```

---

## 🧪 TODO

- [ ] Add async polling timeout fallback
- [ ] Improve error messages
- [ ] Add support for output metadata (e.g., seed, time taken)
- [ ] Dockerize the setup

---

## ⚖️ License

MIT License © 2025 Tarun

---

## 🙌 Acknowledgements

- Thanks to [ComfyUI](https://github.com/comfyanonymous/ComfyUI) for the node-based diffusion backend.

