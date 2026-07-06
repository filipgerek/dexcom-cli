import json
import keyring

SYSTEM_NAME = "dexcom_cli"
SESSION_KEY = "session"


class Credentials:
    def __init__(self, username: str, password: str, region: str):
        self.username = username
        self.password = password
        self.region = region

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
    def load(cls) -> "Credentials":
        payload = keyring.get_password(SYSTEM_NAME, SESSION_KEY)
        if not payload:
            raise RuntimeError(
                "No saved Dexcom session found. Run `dexcom login` first."
            )

        data = json.loads(payload)
        return cls(
            username=data["username"],
            password=data["password"],
            region=data["region"],
        )

    @classmethod
    def delete(cls) -> None:
        keyring.delete_password(SYSTEM_NAME, SESSION_KEY)