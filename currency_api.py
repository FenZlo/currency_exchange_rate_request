from datetime import date

from httpx import request


def get_exchange_rate(date_: date, base_currency: str = 'eur', target_currency: str = 'rub') -> dict:  # сигнатура функции
    url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date_.strftime("%Y-%m-%d")}/v1/currencies/{base_currency}.json'
    response = request(method='get', url=url)
    return response.json()

