from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from PIL import Image
from pdf2image import convert_from_bytes
from fastapi.middleware.cors import CORSMiddleware
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Tool Palette Backend!"}

@app.post("/convert-to-webp")
async def convert_to_webp(file: UploadFile = File(...)):
    data = await file.read()
    name = file.filename.lower()

    if name.endswith(".pdf"):
        images = convert_from_bytes(data)
        img = images[0]
    else:
        img = Image.open(io.BytesIO(data))

    out = io.BytesIO()
    img.save(out, format="WEBP", quality=85)
    out.seek(0)

    return StreamingResponse(
        out,
        media_type="image/webp",
        headers={"Content-Disposition": "attachment; filename=converted.webp"}
    )