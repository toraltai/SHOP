def generate_id(ids):
    import random
    id_ = random.randint(100, 1000)
    while id_ in ids:
        id_ = random.randint(100, 1000)
    return str(id_)

def validate_id(ids, u_id):
    if u_id not in ids:
        raise Exception("Такого юзера нет")

def read_db(name):
    import json
    with open(name, "r") as file:
        db = json.load(file)
    return db

def write_to_db(name, data):
    import json
    with open(name, "w", encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False)