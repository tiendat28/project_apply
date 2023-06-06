from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from config.database import Base, engine, SessionLocal
from models.student import StudentModel
from schemas.student import StudentCreate, StudentUpdate, StudentDelete
from fastapi.middleware.cors import CORSMiddleware
from models.transcripts import PointModel
# from schemas.transcripts import PointCreate, PointUpdate



app = FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/students/{students_id}")
def read_students(students_id:str,db: Session = Depends(get_db)):
    students = StudentModel.get_students(db,students_id)
    return students

@app.get("/students/")
def read_students2(db: Session = Depends(get_db)):
    students = StudentModel.get_students2(db=db)
    return students

@app.post("/students/")
def create_student(create:StudentCreate, db: Session = Depends(get_db)):
    cre_Student = StudentModel.create_Student1(db=db, create=create)
    return cre_Student

@app.patch("/students/{student_id}")
def update_student(update:StudentUpdate, student_id: str, db: Session = Depends(get_db)):
    update_Student = StudentModel.update_Student1(db=db, update=update, student_id=student_id)
    return update_Student

@app.delete("/students/{student_id}")
def delete_student(student_id: str, db: Session = Depends(get_db)):
    student_model = StudentModel()
    deleted_student = student_model.delete_Student1( student_id=student_id,db=db)
    return deleted_student

@app.get("/transcripts/")
def read_point(db: Session = Depends(get_db)):
    point = PointModel.get_Points2(db=db)
    return point