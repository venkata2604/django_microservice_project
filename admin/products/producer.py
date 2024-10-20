# amqps://frulvnjr:Zko0AytOU8R4ZXBAgCXL55pmkuu5QivT@moose.rmq.cloudamqp.com/frulvnjr

import pika

params = pika.URLParametrers("amqps://frulvnjr:Zko0AytOU8R4ZXBAgCXL55pmkuu5QivT@moose.rmq.cloudamqp.com/frulvnjr")

connection = pika.BlockingCOnnection(params)

channel = connection.channel()

# publish
def publish(method, body):
    channel.basic_publish(exchange= '', routing_key='admin', body='hello')

