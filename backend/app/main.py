from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from core import SETTINGS
from routes import UserRouter, AuthRouter, OrderRouter, ProductRouter, ServiceRouter, OthersRouter, InvoiceRouter
from db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
    

# Middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=SETTINGS.allowed_origins,
    allow_credentials=SETTINGS.allow_credentials,
    allow_methods=SETTINGS.allow_methods,
    allow_headers=SETTINGS.allow_headers,
)


# Include routers
app.include_router(UserRouter)
app.include_router(AuthRouter)
app.include_router(OrderRouter)
app.include_router(ProductRouter)
app.include_router(ServiceRouter)
app.include_router(OthersRouter)
app.include_router(InvoiceRouter)

# Static files configuration
app.mount("/static", StaticFiles(directory="../frontend/my-app/static", html=True), name="frontend")


@app.get("/")
async def root():
    return { "status" : "Ok" }

if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8000, reload=True)