from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float, DateTime, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


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
    

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432") 
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Student(12315, 'John', 'Wall', 12 )
person2 = Student(1111, 'Joe', 'Burrow', 10)
session.add(person)
session.add(person2)
session.commit()