from typing import Optional, TYPE_CHECKING

from sqlmodel import Relationship

from models.abs import UserModel

if TYPE_CHECKING:
    from models.order import Order
    from models.payment import Payment

class Client(UserModel, table = True):
    
    orders: Optional[list['Order']] = Relationship(back_populates="client", sa_relationship_kwargs={
                                                                      "lazy": "selectin",
                                                                      "cascade": "all, delete-orphan"
                                                                      })
    payments: Optional[list['Payment']] = Relationship(back_populates="client", sa_relationship_kwargs={
                                                                      "lazy": "selectin",
                                                                      "cascade": "all, delete-orphan"
                                                                      })
