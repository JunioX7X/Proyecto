from fastapi import FastAPI
from app.routers import items

app = FastAPI(
    title="API Demo",
    description="API demostrativa para el Trabajo Práctico 3",
    version="0.1.0"
)

app.include_router(items.router)

@app.get("/")
async def root():
    return {
        "message": "Bienvenido a la API de demostración",
        "status": "online",
        "version": "0.1.0"
    }