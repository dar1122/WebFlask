from app import app,lm,db
from flask import render_template,redirect,g,url_for,flash,request
from .forms import LoginForm,EditForm,PostForm
from .models import User,Post
from flask.ext.login import login_user,current_user,logout_user,login_required
import datetime
from app.method.del_1 import sp_tan
from app.method.top_search import search





@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('First'))

@app.before_request
def before_request():
    g.user = current_user



@app.route('/index/<subject_name>',methods = ['GET','POST'])

def index(subject_name):

    title_list = []
    comments = db.session.query(Post.title).filter_by(subject=subject_name).all()
    com_num = len(comments)
    for x in comments:
        del_comments = str(x)
        dar = sp_tan(del_comments)
        title_list.append(dar)

    python_title = db.session.query(Post.title).filter_by(subject='python').all()
    python_num = len(python_title)

    java_title = db.session.query(Post.title).filter_by(subject='java').all()
    java_num = len(java_title)

    movie_title = db.session.query(Post.title).filter_by(subject='movie').all()
    movie_num = len(movie_title)

    music_title = db.session.query(Post.title).filter_by(subject='music').all()
    music_num = len(music_title)

    food_title = db.session.query(Post.title).filter_by(subject='food').all()
    food_num = len(food_title)


    return render_template('index.html',title='Home',title_list=title_list,subject_name=subject_name,python_num=python_num,java_num=java_num,movie_num=movie_num,music_num=music_num,food_num=food_num)









@app.route('/login',methods = ['GET','POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect('/index')

    form = LoginForm()
    if form.validate_on_submit():
        g.user = User.query.filter_by(username = form.username.data).first()
        if g.user.verify_password(form.password.data):
            login_user(g.user,form.remember_me.data)
            return redirect('/First')
        else:
            flash('用户名或密码错误')
    return render_template('login.html',title='登录',form=form)








@app.route('/login1',methods = ['GET','POST'])
def login1():

    form = EditForm()
    if form.validate_on_submit():
        username_1 = form.username.data
        about = form.about_me.data
        x = User()
        x.password = form.password.data
        newobj = User(username=username_1,password_hash=x.password_hash,about_me=about)
        db.session.add(newobj)
        db.session.commit()
    return render_template('login1.html',form=form)

@app.route('/',methods = ['GET','POST'])
@app.route('/First',methods = ['GET','POST'])
def First():

    get_search_list = search()

    python_title = db.session.query(Post.title).filter_by(subject='python').all()
    python_num = len(python_title)

    java_title = db.session.query(Post.title).filter_by(subject='java').all()
    java_num = len(java_title)

    movie_title = db.session.query(Post.title).filter_by(subject='movie').all()
    movie_num = len(movie_title)

    music_title = db.session.query(Post.title).filter_by(subject='music').all()
    music_num = len(music_title)

    food_title = db.session.query(Post.title).filter_by(subject='food').all()
    food_num = len(food_title)
    return render_template('First.html',python_num=python_num,java_num=java_num,movie_num=movie_num,music_num=music_num,food_num=food_num,get_search_list=get_search_list)

@app.route('/user/<username>',methods = ['GET','POST'])
@login_required
def user(username):
    user = User.query.filter_by(username = username).first()
    if user == None:
        flash('User ' + username + ' not found.')
        return redirect(url_for('index'))

    return render_template('user.html',
        user = user,
        nickname=username)


@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        g.user.username = form.username.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    else:
        form.username.data = g.user.username
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)



@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User %s not found.' % username)
        return redirect(url_for('index'))
    if user == g.user:
        flash('You can\'t follow yourself!')
        return redirect(url_for('user', username=username))
    u = g.user.follow(user)
    if u is None:
        flash('Cannot follow ' + username + '.')
        return redirect(url_for('user', username=username))
    db.session.add(u)
    db.session.commit()
    flash('You are now following ' + username + '!')
    return redirect(url_for('user', username=username))

@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User %s not found.' % username)
        return redirect(url_for('index'))
    if user == g.user:
        flash('You can\'t unfollow yourself!')
        return redirect(url_for('user', username=username))
    u = g.user.unfollow(user)
    if u is None:
        flash('Cannot unfollow ' + username + '.')
        return redirect(url_for('user', username=username))
    db.session.add(u)
    db.session.commit()
    flash('You have stopped following ' + username + '.')
    return redirect(url_for('user', username=username))


@app.route('/write', methods=['GET', 'POST'])
def write():
    if g.user.is_authenticated:
        if request.method == 'POST':
            get_title = request.values.get("title")
            get_post = request.values.get("comment")
            get_subject = request.values.get("subject")
            post = Post(title=get_title,body=get_post,subject=get_subject, timestamp=datetime.datetime.utcnow(), author=g.user)
            db.session.add(post)
            db.session.commit()
            flash('提交成功!')
            return redirect(url_for('write'))
    else:
        flash('您未登录')
    return render_template('write.html')

@app.route('/comment/<name>', methods=['GET', 'POST'])
def comment(name):
    x = db.session.query(Post.body).filter_by(title = name).first()
    n = str(x)
    posts = sp_tan(n)
    return render_template('comment.html',name=name,posts=posts)