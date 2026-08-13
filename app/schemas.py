from pydantic import BaseModel
from typing import List, Optional

class MarketInfo(BaseModel):
    name: str
    branch: Optional[str] = None

class ReceiptInfo(BaseModel):
    date: str
    time: Optional[str] = None
    receipt_no: Optional[str] = None

class ReceiptItem(BaseModel):
    quantity: float
    description: str
    unit_price: float
    total: float

class Summary(BaseModel):
    subtotal: Optional[float] = None
    grand_total: float
    payment_method: Optional[str] = None

class ReceiptData(BaseModel):
    market_info: MarketInfo
    receipt_info: ReceiptInfo
    items: List[ReceiptItem]
    summary: Summary

class OCRSuccessResponse(BaseModel):
    success: bool = True
    data: ReceiptData