# <<<<<<< HEAD
from flask import render_template, request, redirect, url_for, flash, abort
from . import main
# from ..models import User, Blog, Comment, Email
from flask_login import login_required, current_user
# from .. import db, photos
# from .forms import BlogForm, CommentForm, EmailForm
from datetime import datetime
from time import time, sleep
# from ..user_emails import send_subscriptions, send_blogs
import markdown2


@main.route('/', methods=['GET', 'POST'])
def index():
    """
    root page function that returns the index page and its data
    """
    # form = EmailForm()
    #
    # if form.validate_on_submit():
    #     user_name = form.name.data
    #     user_email = form.email.data
    #
    #     new_subscription = Email(name=user_name, email_data=user_email)
    #     new_subscription.save_email()
    #
    #     send_subscriptions(new_subscription)
    #     return redirect(url_for('main.subscribed'))
    #
    # title = "Welcome | Kellen's Blog"
    #
    # all_blogs = Blog.get_all_blogs()
    #
    # if all_blogs:
    #     blogs = all_blogs
    #     return render_template('index.html', title=title, all_blogs=blogs, subscribe_form=form)
    # elif not all_blogs:
    #     blog_message = 'So hakuna blogs'
    #     return render_template('index.html', title=title, blog_message=blog_message, subscribe_form=form)
    return ('index.html')


# =======
# from flask import render_template, request, redirect, url_for, abort, flash
# from . import main
# from flask_login import login_required, current_user
# from .. import db
#
#
# @main.route('/')
# def index():
#     '''
#    view function that defines the routes decorater for the index
#     '''
#
#     title = 'Home - Welcome to The best Movie Review Website Online'
#
#     return render_template('index.html', title=title, )
#
# #  end of index root functions
# # >>>>>>> 23f9be2b9ac64560f2653a0f4169d8cccbdddd34
