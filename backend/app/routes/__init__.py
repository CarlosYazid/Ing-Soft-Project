from routes.user import router as UserRouter
from routes.auth import router as AuthRouter
from routes.service import router as ServiceRouter
from routes.product import router as ProductRouter
from routes.order import router as OrderRouter
from routes.others import router as PaymentRouter
from routes.invoice import router as InvoiceRouter
__all__ = [
    "UserRouter",
    "AuthRouter",
    "ServiceRouter",
    "ProductRouter",
    "OrderRouter",
    "PaymentRouter",
    "InvoiceRouter"
]