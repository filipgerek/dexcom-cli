from enum import Enum
from pydexcom.const import DEXCOM_TREND_DIRECTIONS, TREND_ARROWS

class Trend(str, Enum):
    DOUBLE_UP = "DoubleUp"
    SINGLE_UP = "SingleUp"
    FORTY_FIVE_UP = "FortyFiveUp"
    FLAT = "Flat"
    FORTY_FIVE_DOWN = "FortyFiveDown"
    SINGLE_DOWN = "SingleDown"
    DOUBLE_DOWN = "DoubleDown"
    NOT_COMPUTABLE = "NotComputable"
    RATE_OUT_OF_RANGE = "RateOutOfRange"
    NONE = "None"

    @property
    def arrow(self) -> str:
        return TREND_ARROWS[DEXCOM_TREND_DIRECTIONS[self.value]]