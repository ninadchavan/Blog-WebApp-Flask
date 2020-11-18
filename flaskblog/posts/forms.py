from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequiredV2


class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequiredV2()])
    content = TextAreaField('Content', validators=[InputRequiredV2()])
    submit = SubmitField('Post')
