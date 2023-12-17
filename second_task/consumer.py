import pika
import json

from bson import ObjectId
from pymongo import MongoClient

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

client = MongoClient("mongodb+srv://vi280708ovv:l20nfH2au0qg63ml@cluster0.h1bqaam.mongodb.net/hw8", ssl=True)
db = client["hw8"]
collection_emails = db["emails"]

def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    message["message_status"] = True
    emails_id = message.get("_id")
    if emails_id:
        result = collection_emails.update_one(
            {"_id": ObjectId(emails_id), "message_status": False},
            {"$set": {"message_status": True}}
        )
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

if __name__ == '__main__':
    channel.stop_consuming()