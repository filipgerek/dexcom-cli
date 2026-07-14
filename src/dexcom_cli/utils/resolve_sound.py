from dexcom_cli.models.sound import Sound
from dexcom_cli.models.glucose import GlucoseReading

HYPO_SOUND = Sound.SUBMARINE
HYPER_SOUND = Sound.GLASS

def resolve_sound(reading: GlucoseReading) -> Sound | None:
    if reading.value < 3.9:
        return HYPO_SOUND

    elif reading.value > 7.8 :
        return HYPER_SOUND

    return None