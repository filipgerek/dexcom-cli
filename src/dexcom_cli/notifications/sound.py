from subprocess import run

from dexcom_cli.config import SOUND_PATH
from dexcom_cli.models.sound import Sound

def play(sound: Sound) -> None:
    run(["afplay", f"{SOUND_PATH}/{sound.value}.aiff"])