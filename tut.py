from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy.engine.url import URL

MAIN_DB_URL = URL("mysql+mysqldb",
                  username='root',
                  password='my-secret-pw',
                  host='127.0.0.1',
                  database='sqlalchemy',
                  query=None)

engine = create_engine(MAIN_DB_URL)

Base = declarative_base()

from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(100))
    addresses = relationship("Address", back_populates="user")
    def __repr__(self):
       return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

Base.metadata.create_all(engine)
