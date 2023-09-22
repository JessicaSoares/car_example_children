from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

Base = db.Model

class Car(Base):
    __tablename__ = 'car'
    idcar = Column(Integer, primary_key=True)
    car_name = Column(String(100), nullable=False)
    parts = relationship("Part", backref="car")

class Part(Base):
    __tablename__ = 'part'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    car_id = Column(Integer, ForeignKey('car.idcar'))

def does_car_exist(session, car_name, parts_list):
    car = session.query(Car).filter_by(car_name=car_name).first()
    if car:
        if len(car.parts) == len(parts_list):
            existing_parts = {(part.name, part.price) for part in car.parts}
            if existing_parts == set(parts_list):
                return True
    return False

def add_or_check_car(session, car_name, parts_list):
    car_exists = does_car_exist(session, car_name, parts_list)
    if car_exists:
        return f"Carro com nome {car_name} e as peças especificadas já existe!"
    new_car = Car(car_name=car_name)
    session.add(new_car)
    session.flush()  # Get new car's id
    for part_name, part_price in parts_list:
        new_part = Part(name=part_name, price=part_price, car_id=new_car.idcar)
        session.add(new_part)
    session.commit()
    return f"Carro {car_name} adicionado com sucesso!"
