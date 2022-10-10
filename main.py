import asyncio
import json

from fastapi import FastAPI

app = FastAPI()


@app.post("/search")
async def search():
    await asyncio.sleep(60)
    with open('response_b.json') as f:
        data = json.load(f)
    return data
