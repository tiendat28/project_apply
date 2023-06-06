from entities.student import Student
from sqlalchemy.orm import Session
from schemas.student import StudentCreate, StudentUpdate, StudentDelete
# from fastapi import HTTPException

class StudentModel:
    _entity = Student
    @classmethod
    def get_students(cls, db: Session, student_id: int):

        return db.query(Student).filter(Student.id == student_id).first()
    
    def get_students2(db: Session):

        return db.query(Student).all() 
    
    def create_Student1(db: Session, create:StudentCreate):
        db_create = Student(name = create.name, address = create.address, date = create.date, email = create.email, active = create.active  )
        db.add(db_create)
        db.commit()
        db.refresh(db_create)
        return db_create

    def update_Student1(db: Session, student_id: int, update:StudentUpdate):
        db_query = db.query(Student).filter(Student.id == student_id)
        db_update = db_query.first()
        update_data = update.dict(exclude_unset=True)
        db_query.filter(Student.id == student_id).update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(db_update)
        return db_update
    
    def delete_Student1(self,student_id: str, db: Session ):
        db_query = db.query(Student).filter(Student.id == student_id)
        db_delete = db_query.first()
        delete_data = {'active': False}
        db_query.update(delete_data, synchronize_session=False)
        db.commit()
        db.refresh(db_delete)
        return db_delete
        # if db_delete:
        #     db.refresh(db_delete)
        #     db.delete(db_delete)
        #     db.commit()
        #     return db_delete
        # else:
        #     raise HTTPException(status_code=404, detail="Student not found.")
        