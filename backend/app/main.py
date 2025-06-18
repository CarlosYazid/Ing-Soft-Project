from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


from core import SETTINGS
from routers import userRouter, authRouter

app = FastAPI()

# Middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=SETTINGS.allowed_origins,
    allow_credentials=SETTINGS.allow_credentials,
    allow_methods=SETTINGS.allow_methods,
    allow_headers=SETTINGS.allow_headers,
)

# Include routers
app.include_router(userRouter)
app.include_router(authRouter)

# Static files configuration
app.mount("/", StaticFiles(directory="../frontend/dist", html=True), name="frontend")


@app.get("/")
async def root():
    return {"status": "Ok"}