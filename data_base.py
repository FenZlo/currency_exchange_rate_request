from typing import Optional, Sequence
from sqlmodel import Field, SQLModel, create_engine, select, Session
from datetime import date, datetime


class Curse (SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: date
    curse_eur: float


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})


def create_db_and_base():
    SQLModel.metadata.create_all(engine)


def is_course_on_date_exist(date_: datetime.date) -> Sequence[Curse]:
    with Session(engine) as session:
        return session.exec(select(Curse).where(Curse.date == date_)).all()


def create_curse_on_date(date_: str, curse: float):
    curse_on_date = Curse(date=date_, curse_eur=curse)

    with Session(engine) as session:
        session.add(curse_on_date)

        session.commit()

