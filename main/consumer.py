# amqps://frulvnjr:Zko0AytOU8R4ZXBAgCXL55pmkuu5QivT@moose.rmq.cloudamqp.com/frulvnjr
import json
import pika
from main import Product, db

params = pika.URLParameters("amqps://frulvnjr:Zko0AytOU8R4ZXBAgCXL55pmkuu5QivT@moose.rmq.cloudamqp.com/frulvnjr")

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='main')


# publish
def callback(ch, method, properties, body):
    print("Received in main")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'Product Created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print("Product Created")

    elif properties.content_type == 'Product Updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print("Product Updated")

    elif properties.content_type == "Product Deleted":
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print("Product Deleted")


channel.basic_consume(queue='main', on_message_callback=callback)
print("Started Consuming")
channel.start_consuming()
channel.close()
