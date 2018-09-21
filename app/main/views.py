from unicodedata import category

from flask import render_template , request , redirect , url_for , abort , flash
from . import main
from flask_login import login_required , current_user
from .. import db
from ..models import User , Follow , Language , LanguageCategory
from .forms import LanguageForm , UpdateProfile , UpvoteForm


@main.route ( '/' )
def index():
    '''
   view function that defines the routes decorater for the index
    '''
    languages=Language.query.all()


    title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template ( 'index.html' , title=title, languages=languages  )


#  end of index root functions
@main.route ( '/Python/users/' )
def Python():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'inspiration'

    users = User.get_all_users ( )

    return render_template ( 'Python.html' , title=title , users=users,languages=languages )


@main.route ( '/Java/users/' )
def Java():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'promotion posts'

    users = User.get_all_users ( )

    return render_template ( 'Java.html' , title=title , users=users )


@main.route ( '/JavaScript/users/' )
def JavaScript():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Product Pitches'
    users = User.get_all_users ( )
    return render_template ( 'JavaScript.html' , title=title , users=users )


@main.route ( '/swift/users/' )
def swift():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Product Pitches'
    users = User.get_all_users ( )
    return render_template ( 'swift.html' , title=title , users=users )


@main.route ( '/ruby/users/' )
def ruby():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Product Pitches'
    users = User.get_all_users ( )
    return render_template ( 'ruby.html' , title=title , users=users )


def get_languages_id(languages_id):
    pass


@main.route ( '/languages/<int:languages_id>' )
def languages(languages_id):
    '''
    View pitch page function that returns the post details page and its data
    '''
    found_languages = get_languages_id ( languages_id )
    title = languages_id

    return render_template ( 'languages.html' , title=title , found_languages=found_languages )


def search_languages(languages_name):
    pass


@main.route ( '/search/<languages_name>' )
def search(languages_name):
    '''
    View function to display the search results
    '''
    searched_languages = search_languages ( languages_name )
    title = f'search results for {languages_name}'

    return render_template ( 'search.html' , title=title , searched_languages=searched_languages )


@main.route ( '/languages/new/' , methods=['GET' , 'POST'] )
@login_required
def new_languages():
    '''
    Function that creates new posts
    '''
    form = LanguageForm ( )

    if category is None:
        abort ( 404 )

    if form.validate_on_submit ( ):
        languages = form.languages.data
        category_id = form.category_id.data
        new_languages = Language ( languages=languages,category_id=category_id)


        # new_languages.save_languages ()

        return redirect ( url_for ( 'main.index' ) )

    return render_template ( 'new_languages.html' , form=form)


@main.route ( '/category/<int:id>' )
def category(id):
    '''
    function that returns posts based on the entered category id
    '''
    category = LanguageCategory.query.get ( id )

    if category is None:
        abort ( 404 )

    languages_in_category = Language.get_languages ( id )
    return render_template ( 'category.html' , category=category , languages_in_category=languages_in_category )