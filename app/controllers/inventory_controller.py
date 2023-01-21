from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas


def get_all(db: Session):
    inventory = db.query(models.Inventory).all()
    if not inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No inventory found")

    return inventory


def create(request: schemas.Inventory, db: Session):
    new_inventory = models.Inventory(
        user_id=request.user_id,
        product_description=request.product_description,
        quantity=request.quantity,
        measure=request.measure,
        price=request.price
    )

    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


def show(id: int, db: Session):
    inventory = db.query(models.Inventory).filter(models.Inventory.id == id).first()
    if not inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Inventory with the id {id} is not available")
    return inventory


def update(id: int, request: schemas.InventoryUpdate, db: Session):
    inventory = db.query(models.Inventory).filter(models.Inventory.id == id)
    if not inventory.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Inventory with the id {id} is not available")
    
    
    updated_inventory_dict = {
        "user_id":inventory.first().to_dict()["user_id"],
        "product_description":request.product_description,
        "quantity":request.quantity,
        "measure":request.measure,
        "price":request.price
    }

    inventory.update(updated_inventory_dict)
    db.commit()
    return inventory.first()


def delete(id: int, db: Session):
    inventory = db.query(models.Inventory).filter(models.Inventory.id == id).first()
    if not inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Inventory with the id {id} is not available")
    
    db.delete(inventory)
    db.commit()