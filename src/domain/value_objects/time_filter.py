from enum import Enum

class TimeFilter(str, Enum):
    """Supported search time filters mapped to search engine parameters"""
    PAST_24H = "d"
    PAST_WEEK = "w"
    PAST_MONTH = "m"
