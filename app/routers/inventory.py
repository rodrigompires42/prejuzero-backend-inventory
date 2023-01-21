from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app import schemas
from app.controllers import inventory_controller
from app.database import get_db

router = APIRouter(
    prefix="/api/v1/inventory",
    tags=["Inventory"]
)

@router.get("/", response_model=List[schemas.InventoryShow], status_code=status.HTTP_200_OK)
def get_all_inventory(db: Session = Depends(get_db)):
    return inventory_controller.get_all(db)


@router.post("/", response_model=schemas.InventoryShow, status_code=status.HTTP_202_ACCEPTED)
def insert_inventory(
    request: schemas.Inventory,
    db: Session = Depends(get_db)):
    return inventory_controller.create(request, db)


@router.delete("/", status_code=status.HTTP_200_OK)
def delete_inventory(id: int, db: Session = Depends(get_db)):
    inventory_controller.delete(id, db)


@router.get("/{id}", response_model=schemas.InventoryShow, status_code=status.HTTP_200_OK)
def get_inventory(id: int, db: Session = Depends(get_db)):
    return inventory_controller.show(id, db)


@router.put("/{id}", response_model=schemas.Inventory, status_code=status.HTTP_200_OK)
def update_inventory(id: int, request: schemas.InventoryUpdate, db: Session = Depends(get_db)):
    return inventory_controller.update(id, request, db)