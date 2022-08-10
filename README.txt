# pulsusTeste

Exercício simples: conectar na base de dados MySQL para retornar listas em formato JSON ou inserir registros.
A conexão com MySQL foi feita com MySQL Connector.
A conversão dos dados para JSON foi feita usando FastAPI.
Este e os outros exercícios no repositório fazem parte dos meus primeiros estudos na linguagem Python, que contam 16 dias na data da primeira publicação deste projeto.


PARA REPLICAR O AMBIENTE
Veja o arquivo requirements.txt para instalar as bibliotecas necessárias;
Use o arquivo database.sql para replicar a base de dados no seu sistema;
Edite o arquivo db_funcs.py com o seu usuário e senha para permitir a conexão.


PARA TESTAR
Utilize a documentação automática da FastAPI: http://localhost:8000/docs

O app tem apenas 4 funções: 

1. Buscar todos os dispositivos: http://localhost:8000/devices

2. Buscar 1 dispositivo: http://localhost:8000/devices/<id do dispositivo>

3. Buscar todos as localizações registradas de 1 dispositovo: http://localhost:8000/locals/<id do dispositivo>

4. Inserir uma nova localizações para 1 dispositovo: (POST) http://localhost:8000/locals/<id do dispositivo>/<latitude>/<longitude>

