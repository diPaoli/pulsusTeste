import logging
from datetime import datetime

# Em caso de erro, deixa salvo a data, usuário que fez a requisição,
#   mensagem de erro e stack_info
def createLog(data: datetime, user: str,  msg: Exception):
    logging.basicConfig(filename="trace.log", filemode='w')
    logging.error(msg=f"\nDate Time: {data} \nUser: {user}\nMessage: {msg}", stack_info=True)