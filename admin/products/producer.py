# amqps://frulvnjr:Zko0AytOU8R4ZXBAgCXL55pmkuu5QivT@moose.rmq.cloudamqp.com/frulvnjr

import json
import pika

params = pika.URLParameters('amqps://frulvnjr:Zko0AytOU8R4ZXBAgCXL55pmkuu5QivT@moose.rmq.cloudamqp.com/frulvnjr')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    # properties = pika.BasicProperties(method)
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
