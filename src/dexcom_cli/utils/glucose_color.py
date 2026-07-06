def glucose_color(value: float, unit: str) -> str:
    unit_norm = (unit or "").strip().lower()

    low, high = 3.9, 7.8
    if unit_norm in {"mg/dl", "mgdl"}:
        low, high = 70, 140

    if value < low:
        return "red"
    if value > high:
        return "orange1"
    return "green"