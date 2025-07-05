from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


from core import SETTINGS
from routes import UserRouter, AuthRouter, OrderRouter, ProductRouter, ServiceRouter, PaymentRouter, InvoiceRouter


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
app.include_router(UserRouter)
app.include_router(AuthRouter)
app.include_router(OrderRouter)
app.include_router(ProductRouter)
app.include_router(ServiceRouter)
app.include_router(PaymentRouter)
app.include_router(InvoiceRouter)

# Static files configuration
app.mount("/static", StaticFiles(directory="../frontend/my-app/static", html=True), name="frontend")


@app.get("/")
async def root():
    return {"status": "Ok"}