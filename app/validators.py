from fastapi import HTTPException, status, UploadFile
from PIL import Image
import io

# Sadece bu 3 formata izin vereceğiz
ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE_MB = 5

async def validate_image_file(file: UploadFile) -> bytes:
    # Dosya tipi kontrolü
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Sadece JPEG, PNG ve WEBP formatları kabul edilir."
        )

    contents = await file.read()
    
    # Boyut kontrolü
    if len(contents) > (MAX_FILE_SIZE_MB * 1024 * 1024):
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"Dosya boyutu çok büyük. Maksimum {MAX_FILE_SIZE_MB}MB yükleyebilirsiniz."
        )

    # Gerçekten bir görsel mi yoksa bozuk mu kontrolü
    try:
        image = Image.open(io.BytesIO(contents))
        image.verify()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Yüklenen dosya bozuk veya geçerli bir görsel değil."
        )

    return contents