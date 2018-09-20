from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required

# class CommentsForm(FlaskForm):
#     comment = TextAreaField('Comment', validators=[Required()])
#     vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])
#     submit = SubmitField('SUBMIT')
#
# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')
#
# class PostForm(FlaskForm):
#     category_id = SelectField('Select Category', choices=[('1', 'inspiration'), ('2', 'Education'), ('3', 'News'), ('4','EditorsChoice'), ('5','Desugn & Category')])
#     content = TextAreaField('YOUR post')
#     submit = SubmitField('Create post')
#
# class UpvoteForm(FlaskForm):
#     '''
#     Class to create a wtf form for upvoting a post
#     '''
#     submit = SubmitField('Upvote','DownVote')