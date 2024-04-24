from json import JSONDecodeError
from loguru import logger
from datetime import date
from calendar import monthrange

from currency_api import get_exchange_rate
from server import create_database, is_exchange_rate_on_date_exist, create_exchange_rate_on_date

YEAR = 2023
MONTH = 11


def get_datime_range(year: int = YEAR, month: int = MONTH) -> list[date]:
    last_day = monthrange(year, month)[1]
    return [date(year, month, day) for day in range(1, last_day + 1)]


def get_currency_exchange_rate_on_date(base_currency: str = 'eur', target_currency: str = 'rub'):
    range_date = get_datime_range()

    for date_ in range_date:

        if is_exchange_rate_on_date_exist(date_):
            logger.debug(f'Exchange rate for date: {date_} is already exist')
            continue

        try:
            exchange_rate = get_exchange_rate(date_, base_currency, target_currency)

        except JSONDecodeError as e:
            logger.warning(f'Error retrieving data for {date_}: {e}')
            continue

        logger.debug(f'Date: {date_} exchange_rate: {exchange_rate}')

        create_exchange_rate_on_date(date_, exchange_rate)


if __name__ == '__main__':
    create_database()
    get_currency_exchange_rate_on_date()
