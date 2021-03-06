from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import DataRequired

class Adm_form(FlaskForm):
    username = StringField('user', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class New_adm_form(FlaskForm):
    username = StringField('user', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    power = IntegerField('power', validators=[DataRequired()])

class New_video_form(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    link = StringField('link', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
