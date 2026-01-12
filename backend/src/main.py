from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from uvicorn import run
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi.extension import _rate_limit_exceeded_handler

from core import SETTINGS
from routes import (
    UserRouter, AuthRouter, OrderRouter,
    ProductRouter, ServiceRouter, OthersRouter,
    InvoiceRouter, FileRouter)
from db import init_db

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[
        "120/minute",     # limite sostenido
        "30/second"      # controla picos/bursts
    ]
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

# Paginacion
add_pagination(app)

# Ratelimiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# Middleware configuracion
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
app.include_router(FileRouter)

@app.get("/")
async def root():
    return { "status" : "Ok" }

if __name__ == "__main__":
    run("main:app", host='0.0.0.0', port=SETTINGS.port, reload=True)
