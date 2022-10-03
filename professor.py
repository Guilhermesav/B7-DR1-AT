import pika

from atividade import Atividade


EXCHANGE_NAME = "FTGO"

SERVICE_NAME = "atividade"

# Event Types
ATIVIDADE_ENVIADA = "atividadeEnviada"
ORDER_CANCELLED = "orderCancelled"

credentials = pika.PlainCredentials('guest','guest')
def connect():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('127.0.0.1',5672,'/',credentials)
    )
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type="topic")

    return connection, channel


CONNECTION, CHANNEL = connect()


def emit_atividade_enviada(atividade: Atividade):
    CHANNEL.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=f'{SERVICE_NAME}.{ATIVIDADE_ENVIADA}',
        body=atividade.json()
    )


def emit_order_cancelled(atividade: Atividade):
    CHANNEL.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=f'{SERVICE_NAME}.{ORDER_CANCELLED}',
        body=atividade.json()
    )
