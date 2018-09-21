from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField, RadioField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class KataForm(FlaskForm):
    user = StringField('Please input your username',validators=[Required()])
    title = StringField('Kata Title', validators=[Required()])
    kata = TextAreaField('Code Challenge', validators=[Required()])
    category = RadioField('Label', choices=[('easy','easy'),('challenging','challenging'),('very Challenging','very challenging')])
    submit = SubmitField('Post')