from models import Car
from utils import *

database = read_db("database.json")

def create_product_car():
    Car(input("Введите марку: "),
    input("Введите модель: "),
    input("Введите год:"))
    id_ = generate_id(database.keys())
    for o in Car.objects:
        database[id_] = {
            "Марка:": o.mark,
            "Модель:": o.model,
            "Год:": o.year
        }
    print("Успешно добавлен")
    write_to_db("database.json", database)

def listing(u_id):
    validate_id(database.keys(),u_id)
    mark = database[u_id]["Марка"]
    model = database[u_id]["Модель"]
    year = database[u_id]["Год"]
    print(f"""
    ==========={u_id}============
    Mark: {mark}
    Model: {model}
    Year: {year}
    =============================
    """)


listing(753)