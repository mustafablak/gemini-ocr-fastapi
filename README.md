# AI-Powered Receipt OCR API 🧾⚡🤖

An automated Document Intelligence & OCR microservice powered by **Google Gemini Vision** and **FastAPI**. This API extracts structured key-value data (store name, items, dates, VAT/tax breakdowns, total amounts) from receipts, invoices, and physical documents, returning clean, production-ready JSON.

---

## 🌟 Key Features

- **Production-Ready Architecture:** Structured using Clean Architecture principles separating routing, schemas, and validation logics.
- **Strict Data Validation (Pydantic):** Ensures that the AI-generated JSON perfectly matches the expected schemas before returning the response.
- **Robust File Validation:** Built-in middleware to block oversized files (max 5MB), unsupported MIME types, and corrupted images.
- **Dockerized:** Fully containerized with `Dockerfile` and `docker-compose` for seamless, one-click deployments to any cloud environment.
- **Multimodal AI Vision:** Leverages Google Gemini's multimodal capability for highly accurate document recognition.
- **Interactive OpenAPI/Swagger Docs:** Native API documentation generated automatically at `/docs`.

---

## 🏗️ Folder Structure

```text
gemini-ocr-fastapi/
│
├── app/
│   ├── main.py          # FastAPI application & route definitions
│   ├── schemas.py       # Pydantic models for type-safe AI responses
│   └── validators.py    # File size, MIME type, and integrity checks
│
├── .env                 # Environment variables (ignored in Git)
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Multi-container orchestration
├── requirements.txt     # Python dependencies
└── README.md
```
## 🛠️ Tech Stack

○ Framework: FastAPI

○ Data Validation: Pydantic

○ AI Model: Google Gemini API (gemini-3.5-flash)

○ Containerization: Docker & Docker Compose

○ Image Handling: Pillow (PIL)

○ ASGI Server: Uvicorn

## 🚀 Getting Started
Prerequisites
Python 3.10+ (If running locally)
Docker Desktop (If running via containers)
Google AI Studio API Key
1. Clone the repository
```text
   git clone [https://github.com/mustafablak/gemini-ocr-fastapi.git](https://github.com/mustafablak/gemini-ocr-fastapi.git)
cd gemini-ocr-fastapi
```
2. Configure environment variables
Create a .env file in the root directory and add your API key:
```text
GEMINI_API_KEY=your_gemini_api_key_here
```
3. Run the Application
Option A: Run with Docker (Recommended)
You can build and start the entire microservice with a single command:
```text
docker compose up --build
```
▻ Option B: Run Locally (Virtual Environment)
```text
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
python -m uvicorn app.main:app --reload
```
4. Access Interactive Docs
Open your browser and navigate to http://localhost:8000/docs to test the API directly using Swagger UI.

## 📡 API Endpoints
POST /scan-receipt
Uploads a receipt image (.png, .jpg, .jpeg, .webp) and returns validated, structured JSON details.

Validation Error Responses:
○ 400 Bad Request: Missing or corrupted file.
○ 413 Payload Too Large: File exceeds the 5MB limit.
○ 415 Unsupported Media Type: File format is not allowed.
○ 500 Internal Server Error: AI Processing or JSON validation failures.

Sample Response Body (200 OK)
```text
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
```
## 🔒 Security Note
Make sure never to commit your .env file containing sensitive API keys to public repositories. Ensure .env is listed inside your .gitignore file.

## 📄 License
Distributed under the MIT License. See LICENSE for more information.
