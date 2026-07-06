import keyring

SYSTEM_NAME = "dexcom_cli"

class Credentials:
    def __init__(self, username: str, password: str, region: str):
        self.username = username
        self.password = password
        self.region = region
    
    def save(self, username: str, password: str, region: str):
        keyring.set_password(SYSTEM_NAME, username, password, region)

    def load(self):
        return keyring.get_password(SYSTEM_NAME, self.username)

    def delete(self):
        keyring.delete_password(SYSTEM_NAME, self.username)