from datetime import datetime
from pydantic import BaseModel


# replica entidade devices
class Device(BaseModel):
    id: int
    motorista: str    
    

# replica entidade locals
class Local(BaseModel):
    id: int
    nome_motorista: str
    data: datetime
    lat: float
    lon: float

