from app import db
from app.models import Post

python_title = db.session.query(Post.title).filter_by(subject='python').all()
python_num = len(python_title)

java_title = db.session.query(Post.title).filter_by(subject='java').all()
java_num = len(python_title)

movie_title = db.session.query(Post.title).filter_by(subject='movie').all()
movie_num = len(python_title)

music_title = db.session.query(Post.title).filter_by(subject='music').all()
music_num = len(python_title)

food_title = db.session.query(Post.title).filter_by(subject='food').all()
food_num = len(python_title)
