from typing import Optional
from sqlmodel import Field, SQLModel, create_engine


class Curse (SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: str
    curse_eur: float


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)


def create_db_and_base ():
    SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    create_db_and_base()

