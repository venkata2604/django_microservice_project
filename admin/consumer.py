# amqps://frulvnjr:Zko0AytOU8R4ZXBAgCXL55pmkuu5QivT@moose.rmq.cloudamqp.com/frulvnjr

import pika

params = pika.URLParameters("amqps://frulvnjr:Zko0AytOU8R4ZXBAgCXL55pmkuu5QivT@moose.rmq.cloudamqp.com/frulvnjr")

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='admin')


# publish
def callback(ch, method, properties, body):
    print("received in admin")
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)
print("Started Consuming")
channel.start_consuming()
channel.close()
