from pydexcom import Dexcom

from dexcom_cli.models.glucose import GlucoseReading

class PydexcomClient:
    def __init__(self, username: str, password: str, region: str):
        self.dexcom = Dexcom(username=username, password=password, region=region)

    def current_glucose(self) -> GlucoseReading:

        reading = self.dexcom.get_current_glucose_reading()
        return GlucoseReading(
            value=reading.mmol_l,
            trend=reading.trend,
            unit="mmol/L",
            timestamp=reading.timestamp,
        )