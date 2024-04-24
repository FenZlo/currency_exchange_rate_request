from datetime import date
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class CurrencyRate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: date
    exchange_rate_eur: float


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})

