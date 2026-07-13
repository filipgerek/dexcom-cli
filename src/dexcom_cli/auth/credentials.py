from __future__ import annotations

import json
import keyring
from dexcom_cli.models.credentials import Credentials as CredentialsModel

SYSTEM_NAME = "dexcom_cli"
SESSION_KEY = "session"


class Credentials(CredentialsModel):
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
        return cls(
            username=data["username"],
            password=data["password"],
            region=data["region"],
        )

    @classmethod
    def delete(cls) -> None:
        keyring.delete_password(SYSTEM_NAME, SESSION_KEY)