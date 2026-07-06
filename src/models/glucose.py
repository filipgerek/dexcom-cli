from pydantic import BaseModel
from datetime import datetime

class Glucose(BaseModel):
    value: float
    unit: str
    timestamp: datetime