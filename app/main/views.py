from flask import render_template , request , redirect , url_for , abort,flash
from . import main
from flask_login import login_required , current_user
from .forms import UpdateProfile
from .. import db
from ..models import User


@main.route ( '/' )
def index():
    '''
   view function that defines the routes decorater for the index
    '''

    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template ( 'index.html' , title=title,)


#  end of index root functions

@main.route ( '/user/<uname>' )
def profile(uname):
    user = User.query.filter_by(username=uname).first()


    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user)


@main.route ( '/user/<uname>/update' )
@login_required
def update_profile(uname):
    user = User.query.filter_by ( username=uname ).first ( )
    if user is None:
        abort ( 404 )

    form = UpdateProfile ( )

    if form.validate_on_submit ( ):
        user.bio = form.bio.data

        db.session.add ( user )
        db.session.commit ( )

        return redirect ( url_for ( '.profile' , uname=user.username ) )

    return render_template ( 'profile/update.html' , form=form )