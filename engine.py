from sqlalchemy import create_engine
from sqlalchemy import text, Column, Integer
from sqlalchemy.orm import Session
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )
    conn.commit()

with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
    )
    conn.commit()

stmt = text("SELECT x from some_table where y> :y").bindparams(y=6)

#id = Column(Integer, primary_key=True, nullable=False, name='x')
with engine.connect() as conn:
    result = conn.execute(stmt)

    for row in result:
        print(f'x is {row} ')
