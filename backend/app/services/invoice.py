from fastapi import BackgroundTasks, HTTPException
from weasyprint import HTML

from models import Invoice, InvoiceItem, Email, File
from crud import OrderCrud, ProductCrud, ServiceCrud, UserCrud
from core import SETTINGS
from services import EmailService


class InvoiceService:
    
    @classmethod
    async def workflow(cls, order_id: int, tax_rate: float):
        """Generate an invoice and send it via email."""
        invoice = await cls.generate_invoice(order_id, tax_rate)
        await cls.generate_invoice_pdf(invoice)
        return invoice
    
    
    @classmethod
    async def generate_invoice(cls, order_id: int, tax_rate : float) -> Invoice:
        """Generate an invoice for a client."""
        order = await OrderCrud.read_order(order_id)
        client = await UserCrud.read_client_base(order.client_id)
        order_products = await OrderCrud.read_orders_products_by_order_id(order_id)
        order_services = await OrderCrud.read_orders_services_by_order_id(order_id)

        invoice_items = []
        
        for order_product in order_products:

            product = await ProductCrud.read_product_base(order_product.product_id)

            invoice_items.append(InvoiceItem(
                name=product.name,
                quantity=order_product.quantity,
                unit_price=product.price
            ))
            
        for order_service in order_services:

            service = await ServiceCrud.read_service_base(order_service.service_id)

            invoice_items.append(InvoiceItem(
                name=service.name,
                quantity=order_service.quantity,
                unit_price=service.price
            ))

        return Invoice(
            client=client,
            number=order.id,
            items=invoice_items,
            date=order.created_at,
            tax_rate=tax_rate
        )
    
    @classmethod
    async def generate_invoice_pdf(cls, invoice: Invoice) -> str:
        """Generate a PDF invoice from an Invoice object."""
        template = SETTINGS.jinja_env.get_template("invoice_pdf.html")
        html = template.render(
            invoice={
                "number": invoice.number,
                "date": invoice.date.strftime("%d/%m/%Y"),
                "client": invoice.client.model_dump(),
                "subtotal": invoice.subtotal,
                "tax_rate": invoice.tax_rate,
                "tax_amount": invoice.tax_amount,
                "total": invoice.total
            },
            company={
                "name": SETTINGS.company_name,
                "email": SETTINGS.company_email,
                "phone": SETTINGS.company_phone,
                "address": SETTINGS.company_address,
                "footer_message": SETTINGS.footer_message,
                "support_email": SETTINGS.smtp_comp_email,
                "logo_url": SETTINGS.logo_url
            },
            items=[item.model_dump() for item in invoice.items],
            current_year=invoice.date.year,
        )

        client_folder = SETTINGS.INVOICES_PATH / f"{invoice.client.id}"
        client_folder.mkdir(parents=True, exist_ok=True)

        HTML(string=html).write_pdf(client_folder / f"invoice_{invoice.number}.pdf")

        return client_folder / f"invoice_{invoice.number}.pdf"

    @classmethod
    async def generate_email_invoice(cls, invoice: Invoice) -> str:
        """Generate an invoice PDF and send it via email."""
        template = SETTINGS.jinja_env.get_template("invoice_email.html")
        return template.render(
            invoice= {
                "number": invoice.number,
                "date": invoice.date.strftime("%d/%m/%Y"),
                "client": invoice.client.model_dump(),
                "subtotal": invoice.subtotal,
                "tax_rate": invoice.tax_rate,
                "tax_amount": invoice.tax_amount,
                "total": invoice.total
            },
            company={
                "name": SETTINGS.company_name,
                "email": SETTINGS.company_email,
                "logo_url": SETTINGS.logo_url,
            },
            current_year=invoice.date.year,
            items=[item.model_dump() for item in invoice.items]
        )
        
        
    
    
    @classmethod
    async def send_invoice_email(cls, invoice: Invoice):
        """Send the generated invoice PDF to the client via email."""
        
        subject = f"Factura #{invoice.number}"
        body = await cls.generate_email_invoice(invoice)

        file_path = SETTINGS.INVOICES_PATH / f"{invoice.client.id}/invoice_{invoice.number}.pdf"

        file = File(path=file_path, name=f"Factura-{invoice.number}.pdf")
        if not file.exists():
            raise HTTPException(status_code=500, detail="Invoice PDF not found")
        email = Email(
            subject=subject,
            body=body,
            to=invoice.client.email,
            attachments=[file],
            type="html"  # Assuming the email body is HTML
        )

        EmailService.send_email(email)
    