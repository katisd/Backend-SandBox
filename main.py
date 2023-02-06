import os
from pymongo import MongoClient
from dotenv import load_dotenv


# import env
load_dotenv(".env")
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
# connect database
client = MongoClient(
    f"mongodb://{username}:{password}@mongo.exceed19.online:8443/?authMechanism=DEFAULT"
)
# select database
db = client["exceed02"]  # use exceed02
collection = db["sample_airbnb"]  # use sample_airbnb === db.sample_airbnb

# create collection
db.create_collection("enrollment_system2")
collection = db["enrollment_system"]

# add record
A = {"stdId": 1, "std_name": "Saurabh", "course_name": "python", "grade": 4, "unit": 3}
B = {"stdId": 2, "std_name": "AAA", "course_name": "golang", "grade": 40, "unit": 30}
data = [A, B]
collection.insert_many(data)

# update record
# if find stdId=2 then update grade to 10
collection.update_one({"stdId": 2}, {"$set": {"grade_new": 10}})
# if find stdId=3 then update grade to 10, if not found then create new record with grade=10
collection.update_one({"stdId": 3}, {"$set": {"grade_new": 10}}, upsert=True)

# delete record
collection.delete_one({"stdId": 3})

# delete collection
collection.drop()

# print all record
[print(record) for record in collection.find({})]
