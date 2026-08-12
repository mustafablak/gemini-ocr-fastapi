# AI-Powered Receipt OCR API 🧾⚡

An automated Document Intelligence & OCR service powered by **Google Gemini Vision** and **FastAPI**. This API extracts structured key-value data (store name, items, dates, VAT/tax breakdowns, total amounts) from receipts, invoices, and physical documents, returning clean, production-ready JSON.

---

## 🌟 Key Features

- **Multimodal AI Vision:** Leverages Google Gemini's multimodal capability for accurate document recognition.
- **Strict JSON Output:** Prompt-engineered to produce pure, validated JSON without unnecessary Markdown wrappers or preamble text—ideal for direct database ingestion.
- **Fast & Lightweight:** Built on top of **FastAPI** and **Uvicorn** for asynchronous processing and quick response times.
- **Interactive OpenAPI/Swagger Docs:** Native API documentation generated automatically at `/docs`.
- **Secure Configuration:** Environment variables (`.env`) for safe API key management.

---

## 🏗️ Architecture & Workflow

```text
[ Client / App / Frontend ]
          │
          │  POST /scan-receipt (image file)
          ▼
    ┌───────────┐
    │  FastAPI  │ ──► Load & Process Image (PIL/io)
    └─────┬─────┘
          │
          │  Prompt & Image Bytes
          ▼
  ┌───────────────┐
  │ Gemini Vision │ ──► Deep Multimodal Analysis
  └───────┬───────┘
          │
          │  Structured JSON Response
          ▼
[ Clean JSON Data Delivered ]

🛠️ Tech Stack
Framework: FastAPI

ASGI Server: Uvicorn

AI Model: Google Gemini API

Image Handling: Pillow (PIL)

Environment Management: python-dotenv

🚀 Getting Started
Prerequisites
Python 3.10+ installed

Google AI Studio API Key (Get one here)

Installation
1. Clone the repository:
git clone https://github.com/mustafablak/gemini-ocr-fastapi.git
cd gemini-ocr-fastapi
2.Create a virtual environment (optional but recommended):
python -m venv venv
3.Activate virtual environment:
-On Windows:
venv\Scripts\activate
-On macOS/Linux:
source venv/bin/activate
4.Install dependencies:
pip install -r requirements.txt
5.Configure environment variables:
Create a .env file in the root directory:
GEMINI_API_KEY=your_gemini_api_key_here
6.Run the API server:
python -m uvicorn main:app --reload
7.Access Interactive Docs:
Open your browser and navigate to http://localhost:8000/docs to test the API directly using Swagger UI.

📡 API Endpoints
POST /scan-receipt
Uploads a receipt image (.png, .jpg, .jpeg) and returns structured JSON details.

Sample Response Body (200 OK)
{
  "success": true,
  "data": {
    "market_info": {
      "name": "ÖZDEMİR SÜPERMARKET",
      "branch": "Antalya Şubesi"
    },
    "receipt_info": {
      "date": "13.08.2026",
      "time": "15:30",
      "receipt_no": "0021"
    },
    "items": [
      {
        "quantity": 1,
        "description": "SÜT (1L)",
        "unit_price": 35.00,
        "total": 35.00
      },
      {
        "quantity": 2,
        "description": "YUMURTA (30'lu)",
        "unit_price": 120.00,
        "total": 120.00
      }
    ],
    "summary": {
      "subtotal": 405.00,
      "grand_total": 405.00,
      "payment_method": "CASH"
    }
  }
}

🔒 Security Note
Make sure never to commit your .env file containing sensitive API keys to public repositories. Ensure .env is listed inside your .gitignore file.

📄 License
Distributed under the MIT License. See LICENSE for more information.