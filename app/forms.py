from flask.ext.wtf import Form
from wtforms import StringField, BooleanField,PasswordField
from wtforms.validators import DataRequired,email



class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
class EditForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    about_me = StringField('about_me', validators=[DataRequired()])


class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    subject = StringField('subject', validators=[DataRequired()])