import json
import keyring
from dexcom_cli.models.credentials import Credentials

SYSTEM_NAME = "dexcom_cli"
SESSION_KEY = "session"


class Credentials:
    def save(self) -> None:
        payload = json.dumps(
            {
                "username": self.username,
                "password": self.password,
                "region": self.region,
            }
        )
        keyring.set_password(SYSTEM_NAME, SESSION_KEY, payload)

    @classmethod
    def load(cls) -> Credentials | None:
        payload = keyring.get_password(SYSTEM_NAME, SESSION_KEY)
        
        if not payload:
            return None
        
        data = json.loads(payload)
        return Credentials(
            username=data["username"],
            password=data["password"],
            region=data["region"],
        )

    @classmethod
    def delete(cls) -> None:
        keyring.delete_password(SYSTEM_NAME, SESSION_KEY)