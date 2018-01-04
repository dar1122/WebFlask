
from . import main
from flask import render_template,flash,redirect,session
import os
from config import APP_STATIC_TXT



@main.route('/',methods = ['GET','POST'])
def login():
    name1 = 'dar'
    return render_template('login.html',name1=name1)

@main.route('/train',methods = ['GET','POST'])
def train():
    with open(os.path.join(APP_STATIC_TXT,'info.txt')) as f:
        s = f.readline()
        f.close()
    return render_template('train.html',info=s)

@main.route('/main',methods = ['GET','POST'])
def main():
    return render_template('main.html')


