from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy.engine.url import URL
from tut import User, Address

MAIN_DB_URL = URL("mysql+mysqldb",
                  username='root',
                  password='my-secret-pw',
                  host='127.0.0.1',
                  database='sqlalchemy',
                  query=None)

engine = create_engine(MAIN_DB_URL)

Session = sessionmaker(bind=engine)


with Session() as session:
# main_db_metadata = MetaData()

    result = session.query(User.fullname).all()

    for row in result:
        print(row)
