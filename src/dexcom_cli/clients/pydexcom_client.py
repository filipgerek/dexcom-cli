from pydexcom import Dexcom

from dexcom_cli.models.glucose import GlucoseReading

class PydexcomClient:
    def __init__(self, username: str, password: str, region: str):
        self.dexcom = Dexcom(username=username, password=password, region=region)

    def current_glucose(self) -> GlucoseReading:

        reading = self.dexcom.get_current_glucose_reading()

        return GlucoseReading(
            value=reading.mmol_l,
            trend=reading.trend_direction,
            unit="mmol/L",
            timestamp=reading.datetime,
        )
    
    def get_history(self, minutes: int) -> list[GlucoseReading]:

        readings = self.dexcom.get_glucose_readings(minutes=minutes)

        return [
            GlucoseReading(
                value=reading.mmol_l,
                trend=reading.trend_direction,
                unit="mmol/L",
                timestamp=reading.datetime,
            )
            for reading in readings
        ]