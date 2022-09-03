from flask import render_template, current_app as app
from flask_mail import Mail, Message




def send_email(user, subject, template, domain=None, token=None):
    from manage import mail
    msg = Message(
        subject,
        recipients=[user.email],
        html=render_template(template, user=user, domain=domain, token=token),
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)