from calendar import monthrange
from datetime import date


YEAR = 2023
MONTH = 11


def get_datime_range(year: int = YEAR, month: int = MONTH) -> list[date]:
    last_day = monthrange(year, month)[1]
    return [date(year, month, day) for day in range(1, last_day + 1)]
