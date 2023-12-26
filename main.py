from json import JSONDecodeError
from httpx import request
from loguru import logger
from datetime import date
from calendar import monthrange


def get_datime_range(year: int, month: int) -> list[date]:
    last_day = monthrange(year, month)[1]
    return [date(year, month, day) for day in range(1, last_day+1)]


def get_curse(date_: date, base_currency: str = 'eur', target_currency: str = 'rub') -> float:              #сигнатура функции
    url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{date_.strftime("%Y-%m-%d")}/currencies/{base_currency}.json'
    response = request(method='get', url=url)
    json = response.json()
    curse = json[base_currency][target_currency]
    return curse


def get_currency_curse_on_date(base_currency='eur', target_currency='rub'):
    year, month = 2023, 11
    range_date = get_datime_range(year, month)

    for date_ in range_date:

        try:
            curse = get_curse(date_, base_currency, target_currency)

        except JSONDecodeError as e:
            logger.error(f'Error retrieving data for {date_}: {e}')
            continue

        logger.debug(f'Date: {date_} curse: {curse}')


if __name__ == '__main__':
    get_currency_curse_on_date()
