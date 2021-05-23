from fastapi import FastAPI
import uuid
# datetime module
import datetime;
import json

app = FastAPI()

# State of key values of privious requests
record = {}


@app.get("/")
async def root():
    ts = str(datetime.datetime.now())
    uuidNew = str(uuid.uuid1())
    # updating record
    record[ts] = uuidNew
    # res = dict(reversed(list(record.items())))
    return dict(reversed(list(record.items())))