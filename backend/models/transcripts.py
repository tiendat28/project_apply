from entities.transcripts import Point
from sqlalchemy.orm import Session
from schemas.transcripts import PointCreate, PointUpdate, PointDelete

class PointModel:
    _entity = Point
    @classmethod
    def get_Points(cls, db: Session, Point_id: int):

        return db.query(Point).filter(Point.id == Point_id).first()
    
    def get_Points2(db: Session):

        return db.query(Point).all() 
    
    def create_Point1(db: Session, create:PointCreate):
        db_create = Point(course = create.course, a = create.a, b = create.b, c = create.c, d = create.d, e = create.e, gpa = create.gpa  )
        db.add(db_create)
        db.commit()
        db.refresh(db_create)
        return db_create

    def update_Point1(db: Session, Point_id: int, update:PointUpdate):
        db_query = db.query(Point).filter(Point.id == Point_id)
        db_update = db_query.first()
        update_data = update.dict(exclude_unset=True)
        db_query.filter(Point.id == Point_id).update(update_data, synchronize_session=False)
        db.commit()
        db.refresh(db_update)
        return db_update
    
    def delete_Point1(self,Point_id: str, db: Session ):
        db_query = db.query(Point).filter(Point.id == Point_id)
        db_delete = db_query.first()
        delete_data = {'active': False}
        db_query.update(delete_data, synchronize_session=False)
        db.commit()
        db.refresh(db_delete)
        return db_delete