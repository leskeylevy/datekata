from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class LanguageForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Python'), ('2', 'Java'), ('3', 'JavaScript'), ('4','swift'), ('5','ruby')])
    languages =TextAreaField('YOUR language')
    submit = SubmitField('Create post')

class UpvoteForm(FlaskForm):
    '''
    Class to create a wtf form for upvoting a post
    '''
    submit = SubmitField('Upvote','DownVote')