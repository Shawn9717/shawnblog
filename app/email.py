from flask_mail import Message
from flask import render_template
from . import mail

subject_pref = 'Blogs'
sender_email = 'shawnnjoga@gmail.com'

def mail_message(subject,template,to,**shawn):
    # sender_email =

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**shawn)
    email.html = render_template(template + ".html",**shawn)
    mail.send(email)
