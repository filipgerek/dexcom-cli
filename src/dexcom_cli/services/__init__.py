#services/__init__.py

from dexcom_cli.auth import Session
from dexcom_cli.services.glucose import GlucoseService

def glucose_service() -> GlucoseService:
    client = Session().create_client()
    return GlucoseService(client)