from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    product_description = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    measure = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    def __repr__(self):
        return f"<Inventory user_id={self.user_id} product={self.product_description}>"
    

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_description": self.product_description,
            "quantity": self.quantity,
            "measure": self.measure,
            "price": self.price
        }
