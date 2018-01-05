
import os
from . import main
from flask import render_template,request






@main.route('/',methods = ['GET','POST'])
def login():
    return render_template('login.html')


@main.route('/train',methods = ['GET','POST'])
def train():
    return render_template('train.html')




@main.route('/main',methods = ['GET','POST'])
def main():
    return render_template('main.html')


