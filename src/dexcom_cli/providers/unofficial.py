from pydexcom import Dexcom

from dexcom_cli.models.glucose import GlucoseReading

class PydexcomClient:
    def __init__(self, username: str, password: str, region: str):
        self.dexcom = Dexcom(username=username, password=password, region=region)

    def current_glucose(self) -> GlucoseReading:

        reading = self.dexcom.get_current_glucose_reading()

        print(vars(reading))

        print(reading.mmol_l)
        print(reading.trend)
        print(reading.trend_direction)
        print(reading.datetime)
        print(reading.trend_arrow)

        return GlucoseReading(
            value=reading.mmol_l,
            trend=reading.trend_direction,
            unit="mmol/L",
            timestamp=reading.datetime,
        )