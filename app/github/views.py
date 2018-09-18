from flask import render_template, redirect, url_for, flash, request
from ..models import User
from flask_login import login_user, login_required, logout_user, current_user
from .. import db
from .forms import RegistrationForm, LoginForm, ResetPassword, NewPassword
from . import github
from ..email import send_email, send_reset_email, send_registration_email


@github.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        pass_key = form.password.data
        # db.session.add(user)
        # db.session.commit()

        send_registration_email(user, pass_key)

        return redirect(url_for('github.login'))

    title = "Create New Account"

    return render_template('github/register.html', registration_form=form, title=title)
