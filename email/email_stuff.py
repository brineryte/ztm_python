import smtplib
from email.message import EmailMessage
import dotenv
import os
from string import Template

dotenv.load_dotenv()

print(os.getenv('EMAIL'))

email = EmailMessage()
email['from'] = 'Nugakmog'
email['to'] = 'brineryte@gmail.com'
email['subject'] = 'Hey you'

email.set_content('This is a test email message, sup!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(os.getenv('EMAIL'), os.getenv('EMAIL_PASS'))
    smtp.send_message(email)
    print('email sent!')
