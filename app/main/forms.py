from  flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(Form):
    name = StringField('网站主人的名字是？',validators=[DataRequired()])
    submit = SubmitField('进入')
