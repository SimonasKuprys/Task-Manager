import re
import sys
import smtplib
from email.message import EmailMessage

class Mail:
    @staticmethod
    def send_email(content):
        """
        Function `send_email` sends an email with the given content to the specified email address
        using Gmail SMTP.
        
        :param content: The content parameter is the body of the email that you want to send. It can be
        a string containing any text or HTML content that you want to include in the email
        """
        mail = "samsonsonas@gmail.com"
        subject = "Tasks"
        
        email_address = "tadas.tadinskas1989@gmail.com"
        email_password = "owzvzgeucwryfaeg"
        if re.search(r"^[^@]+@[^@]+\.com$",mail):
            try:
                # Create email
                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = email_address
                msg['To'] = mail
                msg.set_content(content)
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(email_address, email_password)
                    smtp.send_message(msg)
                    smtp.quit()
                print("\nEmail sent successfully.")
            except Exception as e:
                print(f"\n/// Error sending email: {e} \\\\\\")

