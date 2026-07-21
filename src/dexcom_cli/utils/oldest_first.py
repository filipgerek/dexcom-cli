from dexcom_cli.models.glucose import GlucoseReading


def oldest_first(readings: list[GlucoseReading]) -> list[GlucoseReading]:
    return list(reversed(readings))
