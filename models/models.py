from datetime import datetime
from pydantic import BaseModel




class Device(BaseModel):
    id: int
    motorista: str    
    
    




class Local(BaseModel):
    id: int
    nome_motorista: str
    data: datetime
    lat: float
    lon: float

