# Notes

Como montar o volume no highlander:
multipass <source> <target>
multipass mount /home/juliano/Documents/github/probes highlander:/home/ubuntu/probes

## Simplest
### Run the app: 
```
python3 -m venv venv0 # (just once)
source venv0/bin/activate
python -m pip install -r requirements.txt
flask --debug --app simplest.py run -p 8080
```
### Test the app:
```
curl localhost:8080/sleep
curl localhost:8080/business
```
### Build app image:
```
docker build . -f Dockerfile-simplest -t jrkessl/probes:simplest
docker push jrkessl/probes:simplest
```
### Deploy app in cluster:
```
kubectl create deployment simplest --image jrkessl/probes:simplest
```




## long-startup
### Run the app: 
```
python3 -m venv venv0 # (just once)
source venv0/bin/activate
python -m pip install -r requirements.txt
flask --debug --app long-startup.py run -p 8080
```
### Test the app:
```
curl localhost:8080/sleep
curl localhost:8080/business
```
### Build app image:
```
docker build . -f Dockerfile-long-startup -t jrkessl/probes:long-startup 
docker push jrkessl/probes:long-startup
```
### Deploy app in cluster:
```
kubectl create deployment long-startup --image jrkessl/probes:long-startup
```




# Rinha 2.0, exercício do Juliano
Este é a submissão do Juliano Kessler para o exercício da [Rinha de Backend 2.0](https://github.com/zanfranceschi/rinha-de-backend-2024-q1).  
Sei que não vou ganhar, mas fiz pelo aprendizado mesmo. Foi a primeira vez que escrevi um microserviço REST, primeira vez que trabalhei com JSON em Python, nunca nem tinha ouvido falar em servidor WSGI. 
Tecnologias: Nginx, que aponta para middleware WSGI Gunicorn, que aponta para uma aplicação Python/Flask. Banco Postgresql. 
[Repositório original](https://github.com/jrkessl/rinha-backend-2.0)
## Como trabalhar com a versão do docker-compose
1. Dar build na imagem (não esquecer de fazer push para o docker hub). ```docker build . -t jrkessl/rinha-backend-2.0```
2. ```docker-compose down && docker-compose up --abort-on-container-exit```
3. Rodar testes de desempenho: ```./testes-carga.sh```
4. Rodar testes manuais:
Transações:  
```clear; curl -s -X POST http://localhost:9999/clientes/1/transacoes -H 'Content-Type: application/json' -d '{"tipo": "d", "valor": 20, "descricao": "abcd" }' -w "%{http_code}" | jq . ```
Extrato:  
```clear; code=$(curl -s -X GET http://localhost:9999/clientes/1/extrato -H 'Content-Type: application/json' -w "%{http_code}" -o body) && echo "resposta=$code" && cat body | jq . ```
## Como trabalhar com a versão local, servidor nginx
### Subir o banco
1.  ``` docker compose up```
### Popular banco
Não é necessário; a app vai popular automaticamente na primeira execução usando os script do arquivo ```db-init.sql```
### Subir a aplicação localmente
1.  ```pip3 install virtualenv```
2.  ```virtualenv meuenv ```
3.  ```source meuenv/bin/activate```
4.  ```pip install -r requirements.txt```
5.  ```flask --debug run```
### Rodar bateria de testes
```./testes.sh```
### Testar endpoints
#### Transações:
```clear; curl -s -X POST http://localhost:5000/clientes/1/transacoes -H 'Content-Type: application/json' -d '{"tipo": "d", "valor": 20, "descricao": "abcd" }' -w "%{http_code}" | jq . ```
#### Extrato:
```clear; code=$(curl -s -X GET http://localhost:5000/clientes/1/extrato -H 'Content-Type: application/json' -w "%{http_code}" -o body) && echo "resposta=$code" && cat body | jq . ```

## Como trabalhar com a versão local, servidor nginx
1. Instalar o gunicorn (ver arquivo requirements.txt)
2. Desabilitar o apache (se houver conflito de porta) ```sudo service apache2 stop```
3. Iniciar o gunicorn ```gunicorn --bind 0.0.0.0:8001 -w 1 'wsgi:app'```
4. Adicionar o bloco "server" na config do nxing ```/etc/nginx/nginx.conf``` aninhado dentro do bloco ```http```
```
  server {
    listen 6001;
    server_name _;
    location / {
      proxy_pass http://127.0.0.1:8001/;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
      proxy_set_header X-Forwarded-Host $host;
      proxy_set_header X-Forwarded-Prefix /;
    }
  }
```
5. Testar a config do nginx ```sudo nginx -t```
6. Iniciar o nginx ```sudo systemctl start nginx```
7. Talvez dar um reload no nginx ```sudo systemctl reload nginx```
8. Começar a usar o novo endpoint; fazer consultas na porta onde o nginx foi configurado pra ouvir (bloco "server" dentro do bloco "http" do arquivo ```/etc/nginx/nginx.conf```)
## Backlog de funcionalidades a adicionar
 - informar o flask que ele está atrás de um proxy reverso (precisa mesmo?)
 - implementar classes. Pois a app só responde uma chamada por vez. Talvez com classes ela tome chamadas de forma concorrente.
 - implementar o logger. https://flask.palletsprojects.com/en/3.0.x/quickstart/#logging
## Bloco de notas
Aqui é só anotações úteis livres, e não uma documentação estruturada.


horários?
outra vaga? 
  release eng > 1 pm to 10 pm 
  sre >         1 pm to 10 pm 
quntas pessoas?
  400 > 
  70  > 
  amanda > desde 2022 



