from src.models.glucose import GlucoseReading
from src.providers.unofficial import PydexcomClient

import os
from dotenv import load_dotenv

load_dotenv()

class GlucoseService:
    def __init__(self):
        self.client = PydexcomClient(username=os.getenv("username"), password=os.getenv("password"), region=os.getenv("region"))

    def get_current_glucose(self) -> GlucoseReading:
        return self.client.current_glucose()