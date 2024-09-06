from sqlalchemy import Column, Integer, String
from config import Base

class User(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique= True, nullable=False)

    def __repr__(self):
        return f'<User(username = {self.username}, email = {self.email}>'
