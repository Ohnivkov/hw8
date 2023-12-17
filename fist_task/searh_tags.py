from pymongo import MongoClient

client = MongoClient("mongodb+srv://vi280708ovv:l20nfH2au0qg63ml@cluster0.h1bqaam.mongodb.net/hw8", ssl=True)
db = client["hw8"]


def search_qoute_by_tag(tag):
    for qoute in list(db.qoutes.find({'tags': tag})):
        return qoute['quote']


def search_goute_by_tag_list(tag_list):
    result = []
    for tag in tag_list:
        for qoute in list(db.qoutes.find({'tags': tag})):
            result.append(qoute['quote'])
    return result


def search_qoute_by_author(name):
    result = []
    for qoute in list(db.qoutes.find({'author': name})):
        result.append(qoute['quote'])
    return result


while True:
    comand = input().split(':')
    if comand[0] == 'tag':
        print(search_qoute_by_tag(comand[1]))
    if comand[0] == 'tags':
        for qoute in search_goute_by_tag_list(comand[1].split(',')):
            print(qoute)
    elif comand[0] == 'name':
        for qoute in search_qoute_by_author(comand[1].lstrip()):
            print(qoute)
    elif comand[0] == 'exit':
        break
    else:
        print('Unknown command')
