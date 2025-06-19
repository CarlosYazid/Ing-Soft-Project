from models import PaymentBase
from crud import PaymentCrud

class PaymentService:
    
    @classmethod
    async def get_all_payments_base(cls) -> list[PaymentBase]:
        """Retrieve all payments."""
        payments = await PaymentCrud.get_all_payments()
        return [PaymentBase.model_validate({
            "id": payment.id,
            "amount": payment.amount,
            "method": payment.method,
            "status": payment.status,
            "user_id": payment.user_id,
        }) for payment in payments]
        
    @classmethod
    async def get_payment_base_by_id(cls, payment_id: int) -> PaymentBase:
        """Retrieve a payment by ID."""
        payment = await PaymentCrud.get_payment_by_id(payment_id)
        return PaymentBase.model_validate({
            "id": payment.id,
            "amount": payment.amount,
            "method": payment.method,
            "status": payment.status,
            "user_id": payment.user_id,
        })
        
    @classmethod
    async def get_payments_base_by_user(cls, user_id: int) -> list[PaymentBase]:
        """Retrieve payments by user ID."""
        payments = await PaymentCrud.get_payments_by_user(user_id)
        return [PaymentBase.model_validate({
            "id": payment.id,
            "amount": payment.amount,
            "method": payment.method,
            "status": payment.status,
            "user_id": payment.user_id,
        }) for payment in payments]
        
    @classmethod
    async def get_payments_base_by_status(cls, status: str) -> list[PaymentBase]:
        """Retrieve payments by status."""
        payments = await PaymentCrud.get_payments_by_status(status)
        return [PaymentBase.model_validate({
            "id": payment.id,
            "amount": payment.amount,
            "method": payment.method,
            "status": payment.status,
            "user_id": payment.user_id,
        }) for payment in payments]
        
    @classmethod
    async def get_payments_base_by_method(cls, method: str) -> list[PaymentBase]:
        """Retrieve payments by method."""
        payments = await PaymentCrud.get_payments_by_method(method)
        return [PaymentBase.model_validate({
            "id": payment.id,
            "amount": payment.amount,
            "method": payment.method,
            "status": payment.status,
            "user_id": payment.user_id,
        }) for payment in payments]