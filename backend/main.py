from typing import Union
from db.database import Database

from fastapi import FastAPI



app = FastAPI()


@app.get("/")
def read_root():
    test = Database().select()
    
    return {"Hello": test}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}