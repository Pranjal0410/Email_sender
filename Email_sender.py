from email.message import EmailMessage
import ssl
import smtplib

email_sender= input("Enter your email id: ")
email_password= input("Enter your email password")
email_receiver=input("Enter receiver of email:")
subject= input("Enter the subject for your email: ") 
body="""
I'm glad you opened my email
"""

em= EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
