import json
from pymongo import MongoClient


client = MongoClient("mongodb+srv://vi280708ovv:l20nfH2au0qg63ml@cluster0.h1bqaam.mongodb.net/hw8", ssl=True)
db = client["hw8"]
collection_authors = db["authors"]
collection_qoutes = db["qoutes"]


with open("authors.json", "r") as fd:
    author_data = json.load(fd)

with open("qoutes.json", "r") as fd:
    qoutes_data = json.load(fd)


collection_authors.insert_many(author_data)
collection_qoutes.insert_many(qoutes_data)