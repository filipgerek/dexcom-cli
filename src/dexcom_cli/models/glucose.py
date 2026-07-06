from pydantic import BaseModel
from datetime import datetime
from .trend import Trend

class GlucoseReading(BaseModel):
    value: float
    trend: Trend
    unit: str
    timestamp: datetime