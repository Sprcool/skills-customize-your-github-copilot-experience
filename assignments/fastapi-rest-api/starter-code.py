from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    available: bool = True

# In-memory storage for items
items = [
    Item(id=1, name="Notebook", description="A blank notebook", price=5.99, available=True),
    Item(id=2, name="Pencil", description="A graphite pencil", price=0.99, available=True),
]

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items")
def read_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
def create_item(item: Item):
    if any(existing_item.id == item.id for existing_item in items):
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    items.append(item)
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(index)
            return {"message": "Item deleted successfully", "item": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")
