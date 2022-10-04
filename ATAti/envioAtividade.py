import pika
from atividades import Atividade


EXCHANGE_NAME = "FTGO"

SERVICE_NAME = "atividade"

# Event Types
ATIVIDADE_ENVIADA = "atividadeEnviada"


credentials = pika.PlainCredentials('guest','guest')

def connect():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    )
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type="topic")

    return connection, channel


CONNECTION, CHANNEL = connect()


def emit_atividade_enviada(trabalho: Atividade):
    CHANNEL.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=f'{SERVICE_NAME}.{ATIVIDADE_ENVIADA}',
        body=trabalho.json()
    )



