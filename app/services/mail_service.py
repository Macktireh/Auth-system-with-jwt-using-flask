from flask import render_template, current_app
from flask_mail import Mail, Message
from threading import Thread


app = current_app._get_current_object()
mail = Mail(app)

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except ConnectionRefusedError:
            raise ValueError("[MAIL SERVER] not working")

def send_email(user, subject, template, domain=None, token=None):
    msg = Message(
        subject,
        recipients=[user.email],
        html=render_template(template, user=user, domain=domain, token=token),
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    Thread(target=send_async_email, args=(app, msg)).start()