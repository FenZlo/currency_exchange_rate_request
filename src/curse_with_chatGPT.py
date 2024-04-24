from __main__ import g
from httpx import request
from loguru import logger
from datetime import date
from calendar import monthrange

def get_datime_range(year, month):
    last_day = monthrange(year, month)[1]
    return [date(year, month, day).strftime('%Y-%m-%d') for day in range(1, last_day + 1)]

def get_currency_curse_on_date(base_currency='eur', target_currency='rub'):
    year, month = 2023, 11  # Замените этими значениями на нужные вам
    date_range = get_datime_range(year, month)

    for date_str in date_range:
        url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{date_str}/currencies/{base_currency}.json'
        response = request(method='get', url=url)

        try:
            response.raise_for_status()
            json_data = response.json()
            curse = json_data[base_currency][target_currency]
            logger.debug(f'Date: {date_str} curse: {curse}')
        except Exception as e:
            logger.error(f'Error retrieving data for {date_str}: {e}')

if __name__ == '__main__':
    get_currency_curse_on_date()