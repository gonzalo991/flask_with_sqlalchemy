from sqlalchemy import Column, Integer, String
from config import Base

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __repr__(self):
        return (f'<Person(Name = {self.name}, Surname = {self.surname} ,\n'
                f'Age = {self.age} , Gender = {self.gender})>')