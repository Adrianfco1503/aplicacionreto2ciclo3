from db.cliente_db import clienteInDB
from db.cliente_db import update_cliente, get_cliente


from models.cliente_models import clienteIn, clienteOut


import datetime

from fastapi import FastAPI, HTTPException

api = FastAPI()

#################################################################
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
##################################################################

@api.post("/cliente/auth/")
async def auth_cliente(cliente_in: clienteIn):
    
    cliente_in_db = get_cliente(cliente_in.username)

    if cliente_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    
    if cliente_in_db.password != cliente_in.password:
        return  {"Autenticado": False}

    return  {"Autenticado": True}



@api.get("/user/totalproductos/{username}")
async def get_totalproductos(username: str):
    
    cliente_in_db = get_cliente(username)

    if cliente_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    
    cliente_out = clienteOut(**cliente_in_db.dict())

    return  cliente_out




