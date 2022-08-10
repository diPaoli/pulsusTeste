from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from models.models import Device, Local
import db_funcs as db



app = FastAPI(title="Teste Técnico - Pulsus",
description=("Exercício simples: conectar na base de dados MySQL para retornar "
            "listas em formato JSON ou inserir registros. A conexão com MySQL "
            "foi feita com MySQL Connector. A conversão dos dados para JSON foi "
            "feita usando FastAPI.Este e os outros exercícios no repositório "
            "fazem parte dos meus Eestudos na linguagem Python, que contam 12 dias "
            "na data desta publicação."))




# GET todos os Devices
@app.get('/devices', description=("Retorna um objeto JSON contendo todas os "
        "dispositivos cadastrados. Se não houver registros, retorna apenas "
        "com mensagem de informação."),
        summary="Busca todos os dispositivos",
        response_description="Retorna um Objeto JSON")
async def get_devices():
    lista = db.select_AllDevs()

    if lista:
        devices = []

        for dev in lista:
            d = Device(id=dev[0], motorista=dev[1])
            devices.append(d)       

        json_devices = jsonable_encoder(devices)
        return JSONResponse(content=json_devices, status_code=200)
    else:
        return {"Msg": "Nenhum registro encontrado."}




# GET 1 Device
@app.get('/devices/{dev_id}',
    description=("Busca um dispositivo pelo ID e retorna um objeto JSON "
    "com os dados. Se o ID não for encontrado retorna com mensagem "
    "de informação."),
    summary="Busca um dispositivo pelo ID.",
    response_description="Retorna um Objeto JSON")
async def get_device(dev_id):
    result = db.select_Dev(dev_id)

    if result:
        device = Device(id=result[0], motorista=result[1])

        json_device = jsonable_encoder(device)
        return JSONResponse(content=json_device, status_code=200)
    else:
        return {"Msg": "Nenhum registro encontrato."}





# GET Locals de 1 Device
@app.get('/locals/{dev_id}',
    description=("Busca os locais pelos quais um dispositivo passou. "
    "Se não houver registros, retorna mensagem de informação."),
    summary="Busca os Locais registrados para um dispositivo.",
    response_description="Retorna um Objeto JSON")
async def get_DevLocals(dev_id):
    result = db.select_DevLocals(dev_id)

    if result:
        locals = []
        for d in result:
            locals.append(Local(id=d[0],
                                nome_motorista=d[1],
                                data=d[2],
                                lat=d[3],
                                lon=d[4]))

        json_locals = jsonable_encoder(locals)
        return JSONResponse(content=json_locals, status_code=200)
    else:
        return {"Msg": "Nenhum registro encontrato."}





# POST 1 Local
@app.post('/locals/{dev_id}/{latitude}/{longitude}',
    description=("Registra uma localização para um dado dispositivo."),
    summary="Registra a localização de um dispositivo.",
    response_description="Retorna um Objeto JSON")
async def post_Local(dev_id, latitude, longitude):
    row = db.insert_Local(dev_id, latitude, longitude)

    if row:
        return {"Msg": "Local incluído com sucesso."}
    else:
        return {"Erro": "Não foi possível registrar a localização."}





if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host="localhost", port=8000, reload=True)