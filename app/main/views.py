from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from .forms import UpdateProfile
from .. import db
from ..models import User
from ..request import get_github_user


@main.route('/')
def index():
    '''
   view function that defines the routes decorater for the index
    '''

    title = 'Home - Welcome to The best Dating website Online'

    get_github_user = request.args.get('user_query')

    if get_github_user:
        return redirect(url_for('.search', username=get_github_user))
    else:
        return render_template('index.html')


@main.route('/github')
def github():
    return render_template('auth/github.html')


#  end of index root functions

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update')
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/search/github/<username>')
def search(username):
    '''
    test function todisplay users
    :param username:
    :return:
    '''
    username_list = username.split('username')
    username = '+'.join(username_list)
    searched_users = get_github_user(username)
    if searched_users:
        return render_template('auth/register.html')
    else:
        return render_template('404.html')
    title = f'search results for {username}'
    return render_template('auth/github.html', username=searched_users,title=title)
