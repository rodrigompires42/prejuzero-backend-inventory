from pydantic import BaseModel


class Inventory(BaseModel):
    user_id: int
    product_description: str
    quantity: float
    measure: str
    price: float

    class Config():
        orm_mode = True


class InventoryUpdate(BaseModel):
    product_description: str
    quantity: float
    measure: str
    price: float

    class Config():
        orm_mode = True


class InventoryShow(Inventory):
    id: int