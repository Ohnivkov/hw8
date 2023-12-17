import pika
import json

from faker import Faker
from pymongo import MongoClient
from models import Emails
from datetime import datetime

fake = Faker("uk-UA")

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_mock', queue='task_queue')

client = MongoClient("mongodb+srv://vi280708ovv:l20nfH2au0qg63ml@cluster0.h1bqaam.mongodb.net/hw8", ssl=True)
db = client["hw8"]
collection_emails = db["emails"]

def main():
    for i in range(5):
        contact = Emails(
            full_name=fake.name(),
            email=fake.email(),
            message_status=False,
        )
        contact.save()

    message = {
        "_id": str(contact.id),
        "full_name": contact.full_name,
        "email": contact.email,
        "message_status": contact.message_status,
        "date": datetime.now().isoformat()
    }
    inserted_result = collection_emails.insert_one(message)
    document_id = str(inserted_result.inserted_id)
    message["_id"] = document_id

    channel.basic_publish(
        exchange='task_mock',
        routing_key='task_queue',
        body=json.dumps(message).encode(),
        properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    connection.close()

if __name__ == '__main__':
    main()