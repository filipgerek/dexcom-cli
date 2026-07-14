from enum import Enum

class Region(str, Enum):
    US = ("us", "United States")
    JP = ("jp", "Japan")
    OUS = ("ous", "Outside United States")

    def __new__(cls, value: str, label: str):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.label = label
        return obj