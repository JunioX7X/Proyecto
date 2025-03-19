from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Item no encontrado"}}
)

class Item(BaseModel):
    id: str = None
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    disponible: bool = True
    creado: str = None

items_db = []

@router.get("/", response_model=List[Item])
async def listar_items():
    return items_db

@router.post("/", response_model=Item, status_code=201)
async def crear_item(item: Item):
    item_dict = item.dict()
    item_dict["id"] = str(uuid.uuid4())
    item_dict["creado"] = datetime.now().isoformat()
    items_db.append(item_dict)
    return item_dict

@router.get("/{item_id}", response_model=Item)
async def obtener_item(item_id: str):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")