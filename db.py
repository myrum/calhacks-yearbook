import collections
from typing import Collection
from pymongo import MongoClient
import pprint

connection_string = "mongodb+srv://myriam:myriam@cluster0.l8bpwup.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

# dbs = client.list_database_names()

test_db = client.test
# print(local_db.list_collection_names())

def insert_record(doc):
    collection = test_db.clustermanager
    print("here's the doc I think? ", doc)
    inserted_id = collection.insert_one(doc).inserted_id
    print(inserted_id)

printer = pprint.PrettyPrinter()

def return_all():
    collection = test_db.clustermanager

    people = collection.find()

    if len(list(people)) != 0:
        for person in people:
            printer.pprint(person)
    else:
        print("Database is empty, no members found :(\n")
