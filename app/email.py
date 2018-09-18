from flask_mail import Message
# from manage import app
from . import mail
from flask import render_template
import os


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


# def send_reset_email(user):
#     token = user.get_reset_password_token()
#     send_email('Reset Password', sender=os.environ.get('MAIL_USERNAME'), recepients=[user.email],
#                text_body=render_template('admin/reset_password.txt', user=user, token=token),
#                html_body=render_template('admin/reset_password.html', user=user, token=token))
#
#
# def send_registration_email(user, pass_key):
#     send_email('Blog Contributor', sender=os.environ.get('MAIL_USERNAME'), recepients=[user.email],
#                text_body=render_template('emails/registration.txt', user=user, pass_key=pass_key),
#                html_body=render_template('emails/registration.html', user=user, pass_key=pass_key))
