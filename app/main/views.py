
from . import main
from flask import render_template,flash,redirect,session
from datetime import datetime
from .forms import NameForm


@main.route('/',methods = ['GET','POST'])
def login():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        if session.get('name') == '刁盎然':
            return redirect("http://127.0.0.1:5000/main")
        else:
            flash('你似乎并不认识我')
    return render_template('login.html',name = session.get('name'),form = form)

@main.route('/main',methods = ['GET','POST'])
def main():
    return render_template('main.html')