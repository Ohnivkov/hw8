from mongoengine import *

connect(host="mongodb+srv://vi280708ovv:l20nfH2au0qg63ml@cluster0.h1bqaam.mongodb.net/hw8", ssl=True)


class Emails(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_status = BooleanField(default=False)