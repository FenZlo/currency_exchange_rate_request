from datetime import date
from json import JSONDecodeError
from typing import Sequence

from fastapi import FastAPI, HTTPException
from sqlmodel import Session, SQLModel, select

from src.currency_api import get_exchange_rate
from src.data_base import CurrencyRate, engine


app = FastAPI()


@app.get("/fetch_rate")
def fetch_rate(date_: date) -> dict:
    try:
        return get_exchange_rate(date_)

    except JSONDecodeError as e:
        raise HTTPException(404, {"Error": str(e)})


@app.on_event("startup")
def create_database():
    SQLModel.metadata.create_all(engine)


def is_exchange_rate_on_date_exist(date_: date) -> Sequence[CurrencyRate]:
    with Session(engine) as session:
        return session.exec(select(CurrencyRate).where(CurrencyRate.date == date_)).all()


@app.post("/exchange_rate")
def create_exchange_rate_on_date(date_: date, exchange_rate: float):
    exchange_rate_on_date = CurrencyRate(date=date_, exchange_rate_eur=exchange_rate)

    with Session(engine) as session:
        session.add(exchange_rate_on_date)

        session.commit()
