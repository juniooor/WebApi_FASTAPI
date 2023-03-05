from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

class Item(BaseModel):
    name:str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id" : item_id}

@app.post("/items/")
async def post_item(item:Item):
    return item
