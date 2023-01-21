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

