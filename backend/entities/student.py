from sqlalchemy import Boolean, Column, Integer, String

from config.database import Base



class Student(Base):
    __tablename__ = "studentlist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address= Column(String)
    date = Column(String)
    email = Column(String)
    active = Column(Boolean)