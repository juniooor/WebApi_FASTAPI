from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI


class Item(BaseModel):
    name:str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello user"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id" : item_id}


@app.post("/items/")
async def create_item(item:Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict

# @app.put("/items/{item_id}")
# async def create_item(item: int , item: Item):
#     return {"item_id": item_id, **item.dict()}
