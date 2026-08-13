import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, status, HTTPException
from fastapi.responses import RedirectResponse
from google import genai
from PIL import Image
import io

from app.schemas import OCRSuccessResponse, ReceiptData
from app.validators import validate_image_file

load_dotenv()

app = FastAPI(title="Gemini OCR API")

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")

@app.post("/scan-receipt", response_model=OCRSuccessResponse)
async def scan_receipt(file: UploadFile = File(...)):
    try:
        image_bytes = await validate_image_file(file)
        
        image = Image.open(io.BytesIO(image_bytes))
        
        prompt = (
            "Bu faturayı analiz et ve bilgileri şu JSON formatında dön:\n"
            "{\n"
            '  "market_info": {"name": "string", "branch": "string"},\n'
            '  "receipt_info": {"date": "string", "time": "string", "receipt_no": "string"},\n'
            '  "items": [{"quantity": 1.0, "description": "string", "unit_price": 0.0, "total": 0.0}],\n'
            '  "summary": {"subtotal": 0.0, "grand_total": 0.0, "payment_method": "string"}\n'
            "}\n"
            "Sadece geçerli bir JSON objesi döndür. Markdown etiketi (```json) veya açıklama KESİNLİKLE ekleme."
        )
        
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=[image, prompt]
        )
        
        cleaned_text = response.text.strip().removeprefix("```json").removesuffix("```").strip()
        raw_json = json.loads(cleaned_text)
        
        validated_data = ReceiptData(**raw_json)
        
        return OCRSuccessResponse(success=True, data=validated_data)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"İşlem sırasında bir hata oluştu: {str(e)}")