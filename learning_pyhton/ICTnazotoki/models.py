from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    questionnumber = db.Column(db.String(10),nullable=False,unique=True)
    correctanswer = db.Column(db.String(80), nullable=False)

class ICTUser(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    Q1 = db.Column(db.Boolean, nullable=False)
    Q2 = db.Column(db.Boolean, nullable=False)
    Q3 = db.Column(db.Boolean, nullable=False)
    Q4 = db.Column(db.Boolean, nullable=False)
    Q5 = db.Column(db.Boolean, nullable=False)
    Q6 = db.Column(db.Boolean, nullable=False)
    Q7 = db.Column(db.Boolean, nullable=False)
    Q8 = db.Column(db.Boolean, nullable=False)
    Q9 = db.Column(db.Boolean, nullable=False)
    Q10 = db.Column(db.Boolean, nullable=False)
    Q11 = db.Column(db.Boolean, nullable=False)