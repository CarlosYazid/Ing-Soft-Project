from routers.user import router as UserRouter
from routers.auth import router as AuthRouter
from routers.service import router as ServiceRouter
from routers.product import router as ProductRouter
from routers.order import router as OrderRouter
__all__ = [
    "UserRouter",
    "AuthRouter",
    "ServiceRouter",
    "ProductRouter",
    "OrderRouter"
]