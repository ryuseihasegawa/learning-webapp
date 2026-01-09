from flask import Flask
from models import db, User
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)


def create():
    #ここに追記
    with app.app_context():
        admin_user = User(
            username = 'admin_user',
            password_hash = generate_password_hash('admin'),
        )
        db.session.add(admin_user)
        db.session.commit()

def read():
    #ここに追記
    with app.app_context():
        user = db.session.get(User , 3)
        if user:
            print(f'ID: {user.id}, Username: {user.username}')


            
def update():
    #ここに追記
    with app.app_context():
        user = User.query.filter_by(username='admin_user').first()
        if user:
            user.username = 'test_user'
            db.session.commit()


def delete():
    #ここに追記
    with app.app_context():
        user = User.query.filter_by(username='test_user').first()
        if user:
            db.session.delete(user)
            db.session.commit()


def read_all():
    with app.app_context():
        users = User.query.all()
        for user in users:
            print(f'ID: {user.id}, Username: {user.username}')



if __name__ == '__main__':
    #create()
    #read() 
    #update()
    #read()
    #delete()
    read_all()
