from .credentials import Credentials
from ..clients.pydexcom_client import PydexcomClient

class Session:

    def create_client(self) -> PydexcomClient:

        credentials = Credentials.load()

        return PydexcomClient(
            username=credentials.username,
            password=credentials.password,
            region=credentials.region,
        )