#/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import Column, Integer, Strin
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import Sessions
from sqlalchemy import (create_engine)
Base = declarative_base()
class Student(Base):
    _tablename_ = "Students"
    id = Column(integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=false)

if _name_ == "_name_":
    engine = create_engine("mysql+mysqldb://root:root@localhost/demo.db", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    #Create/insert data
    session=Session(engine)
    std1 = Student(name = "Steve")
    std2 = Student(name = "Dovine")
    std3 = Student(name = "Micheal")
    session.add(std1)
    session.add(std3)
    session.add(std3)
    session.commit()

