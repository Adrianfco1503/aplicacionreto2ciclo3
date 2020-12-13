from pydantic import BaseModel
class clienteIn(BaseModel):
    username: str
    password: str
class clienteOut(BaseModel):
    username: str
    cantproductos: int