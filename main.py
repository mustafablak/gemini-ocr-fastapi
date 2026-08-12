from fastapi import FastAPI, UploadFile, File
from fastapi.responses import RedirectResponse
from google import genai
from PIL import Image
from dotenv import load_dotenv
import os
import io

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

# Ana sayfaya girince direkt /docs adresine yönlendirsin
@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

@app.post("/scan-receipt")
async def scan_receipt(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=[image, "Bu faturadaki tüm metinleri ve bilgileri JSON olarak çıkar."]
        )
        
        return {"success": True, "data": response.text}
    except Exception as e:
        return {"success": False, "error": str(e)}