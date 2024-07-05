from fastapi import FastAPI
import paho.mqtt.client as mqtt
import json
import pymongo
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://admin:password@localhost:27017/")
db = myclient["mqtt-db"]
collection = db["iot-status"]


# consumer code
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")
    obj = json.loads(msg.payload.decode())
    obj["timestamp"] = datetime.now()
    print(f"inserting data to mongo - {obj}")
    collection.insert_one(obj)


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("mqtt_topic")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username="user", password="password")
client.connect("localhost", 1883, 60)
client.loop_start()


# initializing fastAPI app
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "FastApi Server is up and running"}


@app.get("/aggregate")
async def aggregate_data(start: str, end: str):
    print(start)
    print(end)
    try:
        dt_start = datetime.fromisoformat(start)
        dt_end = datetime.fromisoformat(end)
    except Exception:
        return "Invalid datetime format. Pls provide datetime in ISO format."

    # Aggregation pipeline
    pipeline = [
        {"$match": {"timestamp": {"$gte": dt_start, "$lt": dt_end}}},
        {"$group": {"_id": "$status", "count": {"$sum": 1}}},
        {"$project": {"status": "$_id", "count": 1, "_id": 0}},
        {"$sort": {"count": pymongo.DESCENDING}},  # Sort by count
    ]

    # Execute the aggregation
    result = list(collection.aggregate(pipeline))

    # Process the aggregated data (e.g., print or analyze)
    r = []
    for doc in result:
        print(f"Status: {doc['status']}, Count: {doc['count']}")
        r.append({"Status": doc["status"], "Count": doc["count"]})

    return r


# 2024-07-05 09:00:00.000
