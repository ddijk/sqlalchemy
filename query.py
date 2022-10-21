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


unread_notifications = []
columns = [User.id, User.name, User.fullname]
with Session() as session:
# main_db_metadata = MetaData()

    result = session.query(*columns).all()

    print(f'type van res is: {type(result)}')
    num = len(result)
    print(f'Aantal rows is {num}')
    if num:
        print(f'type van res item is: {type(result[0])}')

    for row in result:
        print(row)

    unread_notifications.extend(result)
    print('unread: ', unread_notifications)
