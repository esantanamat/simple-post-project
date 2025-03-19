from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float, DateTime, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()



class Student(Base):
    __tablename__ = "Students"

    id = Column("id", Integer, primary_key = True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    grade = Column("grade", Integer)

    def __init__(self, id, firstname, lastname, grade):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.grade = grade
    def __repr__(self):
        return f"({self.id} {self.firstname} {self.lastname}, {self.grade})"
    
    engine = create_engine('postgresql://username:password@localhost:5432/dbname')
    