from dexcom_cli.models.glucose import GlucoseReading

class GlucoseService:
    def __init__(self, client):
        self.client = client

    def get_current_glucose(self) -> GlucoseReading:
        return self.client.current_glucose()

    def get_history(self, minutes: int) -> list[GlucoseReading]:
        return self.client.get_history(minutes)