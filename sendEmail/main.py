
import smtplib
import ssl
from email.message import EmailMessage

sender=""
receiver=""
password= 'password'# can store the password in an environment variable
subject='Do the Task now'
body="""This task should be completed before tomorrow"""

em=EmailMessage()#creating the instance of the  EmailMessage
em['From']=sender
em['To']=receiver
em[subject]= subject
em.set_content(body)

context=ssl.create_default_context()


with smtplib.SMTP_SSL('smtp@gmail.com',465,context=context) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,em.as_string())



