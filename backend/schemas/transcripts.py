from pydantic import BaseModel

class PointBase(BaseModel):
    course: str
    a: float
    b: float
    c: float
    d: float
    e: float
    gpa: float
    status: bool

class PointCreate(PointBase):
    pass

class PointUpdate(PointBase):
    pass

class PointDelete(PointBase):
    pass

class Point(PointBase):
    id: int
    class Config:
        orm_mode = True