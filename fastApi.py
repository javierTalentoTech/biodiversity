from fastapi import FastAPI
from soupClima import scrape_weather
from pydantic import BaseModel

app = FastAPI()

@app.get("/usuarios/{user_id}")
def read_root():
    data = scrape_weather('https://weather.com/es-CO/tiempo/hoy/l/5.54,-73.36?par=google')
    return data

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items")
def create_item(item: Item):
    priceFinal = item.price + 20000
    return {"item_name": item.name, "item_price": priceFinal}