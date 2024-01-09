from typing import Optional, Sequence
from sqlmodel import Field, SQLModel, create_engine, select, Session
from datetime import date, datetime


class Curse (SQLModel, table=True):
    id_: Optional[int] = Field(default=None, primary_key=True, alias="id")
    date_: date = Field(alias="date")
    curse_eur: float


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_base():
    SQLModel.metadata.create_all(engine)


def is_course_on_date_exist(date_: datetime.date) -> Sequence[Curse]:
    with Session(engine) as session:
        return session.exec(select(Curse)).all()

