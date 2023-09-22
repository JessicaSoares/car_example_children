from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, and_, tuple_, func
from sqlalchemy.orm import relationship, aliased
from app import db
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

Base = db.Model

class Car(Base):
    __tablename__ = 'car'

    idcar = Column(Integer, primary_key=True)  
    parts = relationship("Part", backref="car")


class Part(Base):
    __tablename__ = 'part'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    idcar = Column(Integer, ForeignKey('car.idcar')) 


def does_car_exist(session, parts_list):

    target_count = len(parts_list)


    subquery = (
        session.query(Part.idcar)
        .filter(tuple_(Part.name, Part.price).in_(parts_list))
        .group_by(Part.idcar)
        .having(func.count(Part.id) == target_count)
    ).subquery()

    
    cars = (
        session.query(Car)
        .join(subquery, Car.idcar == subquery.c.idcar)
        .all()
    )
    
    return cars
