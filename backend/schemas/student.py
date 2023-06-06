from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    address: str
    date: str
    email: str

class StudentCreate(StudentBase):
    active: bool

class StudentUpdate(StudentBase):
    pass

class StudentDelete(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        orm_mode = True