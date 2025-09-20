from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

class Paintings(Base):
    __table__ = 'paintings'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    caption: Mapped[str] = mapped_column(String(200))
    #img: Mapped[bin] = mapped_column(LargeBinary)

    def __repr__(self):
        return  "hello"#f'id: {self.id} title:{self.title}, caption:{self.caption}'


def _main():
    load_dotenv()
    print("main")
    db_host=os.getenv("POSTGRES_HOST")
    db_username=os.getenv("POSTGRES_USER")
    db_password=os.getenv("POSTGRES_PASSWORD")
    db_dbname=os.getenv("POSTGRES_DATABASE")
    db_url = f'postgresql://{db_dbname}:{db_password}@{db_host}/{db_dbname}'
    print(db_url)
    conn = create_engine(db_url)
    conn.connect()

    Base.metadata.create_all(conn)

if __name__ =="__main__":
    #print("main")
    _main()