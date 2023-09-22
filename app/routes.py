from app import app, db 
from app.models import Car, Part, does_car_exist

@app.route('/')
def index():
    parts_list = [('pecaA', 100), ('pecaB', 200)]

    cars = does_car_exist(db.session, parts_list)  
    if cars:
        return "Carro com as peças especificadas já existe!"
    else:
        return "Carro com as peças especificadas não existe!"
