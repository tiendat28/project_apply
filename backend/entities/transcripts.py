from sqlalchemy import Column, Float, String,Integer, Boolean

from config.database import Base



class Point(Base):
    __tablename__ = "transcripts"

    id = Column(Integer, primary_key=True, index=True)
    course = Column(String)
    a= Column(Float)
    b = Column(Float)
    c = Column(Float)
    d = Column(Float)
    e = Column(Float)
    gpa = Column(Float)
    status = Column(Boolean)