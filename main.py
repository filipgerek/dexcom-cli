from pydexcom import Dexcom
import os
from dotenv import load_dotenv

load_dotenv()

dexcom = Dexcom(username=os.getenv("username"), password=os.getenv("password"), region=os.getenv("region"))

def main():
    print("Hello from dexcom-cli!")
    print("Current glucose reading: ", dexcom.get_current_glucose_reading().mmol_l, "mmol/L")


if __name__ == "__main__":
    main()
