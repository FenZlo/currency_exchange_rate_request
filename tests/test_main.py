from datetime import date
from main import get_datime_range


def test_get_datime_range():
    year = 2023
    month = 11
    expected_range = [date(2023, 11, day) for day in range(1, 31)]
    assert get_datime_range(year, month) == expected_range
