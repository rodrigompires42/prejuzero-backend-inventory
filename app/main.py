from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import inventory

app = FastAPI(
    title="PrejuZero Inventory Microservice"
)

app.include_router(inventory.router)