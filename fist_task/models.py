
from mongoengine import *

connect(host="mongodb+srv://vi280708ovv:l20nfH2au0qg63ml@cluster0.h1bqaam.mongodb.net/hw8", ssl=True)

class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=100)
    description = StringField(max_length=5000)


class Qoutes(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    qoute = StringField(max_length=5000, required=True)

    meta = {'allow_inheritance': True}