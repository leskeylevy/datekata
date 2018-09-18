from flask import render_template, redirect, url_for, flash, request
# from flask_dance.contrib.github import github
#from ..models import User
# from flask_login import login_user, login_required, logout_user, current_user
# from .. import db
from .forms import RegistrationForm, LoginForm, ResetPassword, NewPassword
from . import github
#from ..email import send_email, send_reset_email, send_registration_email


# @github.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(email=form.email.data, username=form.username.data, password=form.password.data)
#         pass_key = form.password.data
#          db.session.add(user)
#          db.session.commit()
#
#         send_registration_email(user, pass_key)
#
#         return redirect(url_for('github.login'))
#
#     title = "Create New Account"
#
#     return render_template('github/register.html', registration_form=form, title=title)

@github.route('/github')
def github_login():
    if not github.authorized:
        return redirect(url_for(github_login))

    account_info= github.get('user')

    if account_info.ok:
        account_info_json = account_info_json()

        return '<h1> Your Github name is {}'.format(account_info_json['login'])
    return '<h1> Request failed </h1>'

