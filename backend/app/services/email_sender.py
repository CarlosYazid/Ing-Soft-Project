import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from core import SETTINGS

class EmailSender:
    """Service for sending emails using SMTP."""
    
    
    session : smtplib.SMTP

    
    def __init__(self):
        self.session = smtplib.SMTP(SETTINGS.smtp_host, SETTINGS.smtp_port)
        self.session.starttls()
        self.session.login(SETTINGS.smtp_corp_email, SETTINGS.smtp_corp_password.get_secret_value())

    def send_email(self):
        pass

class Email:
    def __init__(self, subject : str, body: str, to_email: str, attachments : list[File] = None):
        self.subject = subject
        self.body = body
        self.to_email = to_email
        self.attachments = attachments if attachments else []

    def to_message(self):
        
        msg = MIMEMultipart()

        msg['From'] = SETTINGS.smtp_corp_email
        msg['To'] = self.to_email
        msg['Subject'] = self.subject

        msg.attach(MIMEText(self.body, 'plain'))


        # Attach files if any
        if not self.attachments:
            return msg
        else:
            for attachment in self.attachments:
                if isinstance(attachment, File):
                    msg.attach(attachment.to_Mime())


        return msg

class FileType(enum.Enum):
    PDF = 1
    IMAGE = 2
    TEXT = 3
    OTHER = 4

    @classmethod
    def from_extension(cls, extension):
        if extension.lower() == '.pdf':
            return cls.PDF
        elif extension.lower() in ['.jpg', '.jpeg', '.png']:
            return cls.IMAGE
        elif extension.lower() == '.txt':
            return cls.TEXT
        else:
            return cls.OTHER
    @classmethod
    def from_file(cls, file_path):
        _, extension = os.path.splitext(file_path)
        return cls.from_extension(extension)

class File:
    
    def __init__(self, file_path : str, type : 'FileType' = None):
        self.file_path = file_path
        self.type = type if type else FileType.from_file(file_path)

    def read(self):
        with open(self.file_path, 'rb') as file:
            return file.read()

    def name(self):
        return os.path.basename(self.file_path)
    
    def to_Mime(self):
        
        if self.type == FileType.PDF:
            content_type = 'application/pdf'
        elif self.type == FileType.IMAGE:
            content_type = 'image/jpeg' if self.file_path.lower().endswith(('.jpg', '.jpeg')) else 'image/png'
        elif self.type == FileType.TEXT:
            content_type = 'text/plain'
        else:
            content_type = 'application/octet-stream'
        
        mime = MIMEBase('application', content_type)
        mime.set_payload(self.read())
        encoders.encode_base64(mime)
        mime.add_header('Content-Disposition', f'attachment; filename={self.name()}')
        mime.add_header('Content-Type', content_type)
        mime.add_header('Content-Transfer-Encoding', 'base64')
        
        return mime