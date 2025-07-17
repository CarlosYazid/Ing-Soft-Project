from fastapi import APIRouter, Request, BackgroundTasks
from services import InvoiceService
from models import InvoiceRequest
from time import sleep
router = APIRouter(prefix="/invoice")

@router.post("/generate")
async def generate_invoice(invoice_request: InvoiceRequest, background_tasks: BackgroundTasks):
    invoice = await InvoiceService.workflow(
        order_id=invoice_request.order_id,
        tax_rate=invoice_request.tax_rate
    )
    background_tasks.add_task(
        InvoiceService.send_invoice_email,
        invoice=invoice
    )
    sleep(1)
    await InvoiceService.upload_invoice(invoice)
    return invoice
