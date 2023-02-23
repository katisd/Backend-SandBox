from fastapi import FastAPI
from routers import std
from config.database import mongo_connection

app = FastAPI()
# file based routing
app.include_router(std.router)


@app.get("/")
def root():
    data = mongo_connection["enrollment_system"].find({}, {"_id": False})
    parsed_data = list(data)
    return parsed_data
