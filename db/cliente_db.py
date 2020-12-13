from typing import Dict
from pydantic import BaseModel
class clienteInDB(BaseModel):
    username: str
    password: str
    totalproductos: float

database_cliente = Dict[str, clienteInDB]
database_cliente = {
    "adrian15": clienteInDB(**{"username":"adrian15",
                            "password":"12345",
                            "totalproductos":12000}),
    "maria16": clienteInDB(**{"username":"maria16",
                            "password":"mar123",
                             "totalproductos":34000}),
}

def get_cliente(username: str):
    if username in database_cliente.keys():
        return database_cliente[username]
    else:
        return None
def update_cliente(cliente_in_db: clienteInDB):
    database_cliente[cliente_in_db.username] = cliente_in_db
    return cliente_in_db