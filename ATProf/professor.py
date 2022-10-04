import time
import random
import uvicorn
import requests
import pika

from fastapi import FastAPI, HTTPException
from modelos import Atividade


ATIVIDADE_ENVIADA = "atividadeEnviada"

app = FastAPI()

ATIVIDADES = {}

def on_atividade_created(ch, method, properties, body):
    atividade = Atividade.parse_raw(body)
    
    time.sleep(10)

    nota = random.randint(0,10)
    nota = float(nota)
    if nota >= 6:
        message = {"Nota": '{nota}'}
        print(f'Atividade aprovada {atividade.atividade_id}')
    else:
        message = {"Nota": '{nota}'}
        print(f'Atividade reprovada {atividade.atividade_id}')

    # PUT para o Order
    resp = requests.put(
        url=f'http://localhost:8000/atividade/{atividade.atividade_id}',
        json=message
    )
    print(resp)

@app.get("/")
async def root():
    return {"status": "ok"}



def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue=ATIVIDADE_ENVIADA)

    channel.basic_consume(
        queue=ATIVIDADE_ENVIADA,
        on_message_callback=on_atividade_created,
        auto_ack = True
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
    main()
    
    
