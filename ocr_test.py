from google import genai
from PIL import Image

# Google AI Studio'dan aldığın API Anahtarı
API_KEY = "GEMINI_API_KEY"

client = genai.Client(api_key=API_KEY)
resim_yolu = "image.png"

try:
    resim = Image.open(resim_yolu)
    print("Gemini belgeyi analiz ediyor, lütfen bekleyin...")
    
    # API tarafında en güncel resmi flash modeli
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=[
            resim, 
            "Bu belgedeki veya faturadaki tüm metinleri çıkar. Kurum adı, tarih, toplam tutar gibi bilgileri düzenli bir liste halinde ver."
        ]
    )
    
    print("\n--- ANALİZ SONUCU ---")
    print(response.text)

except Exception as e:
    print(f"Bir hata oluştu: {e}")