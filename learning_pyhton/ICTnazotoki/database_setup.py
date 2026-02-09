from flask import Flask
from models import db, Answer, ICTUser

def setup_database():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ICTnazotoki.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

        #問題と答えを追加
        Q1 = Answer(
            questionnumber='Q1', 
            correctanswer='おしあげ',
        )
        Q2 = Answer(
            questionnumber='Q2', 
            correctanswer='おおじま', 
        )
        Q3 = Answer(
            questionnumber='Q3', 
            correctanswer='りょうごく', 
        )
        Q4 = Answer(
            questionnumber='Q4', 
            correctanswer='つきしま', 
        )

        Q5 = Answer(
            questionnumber='Q5', 
            correctanswer='しんばし', 
        )
        Q6 = Answer(
            questionnumber='Q6', 
            correctanswer='ひびや', 
        )
        Q7 = Answer(
            questionnumber='Q7', 
            correctanswer='あかばねばし', 
        )
        Q8 = Answer(
            questionnumber='Q8', 
            correctanswer='あけぼのばし', 
        )
        Q9 = Answer(
            questionnumber='Q9', 
            correctanswer='ねりま', 
        )
        Q10 = Answer(
            questionnumber='Q10', 
            correctanswer='しんいたばし', 
        )
        Q11 = Answer(
            questionnumber='Q11', 
            correctanswer='くだんした', 
        )

        #ユーザーを追加
        user1 = ICTUser(
            username = 'groupA',
            password = 'shinjuku',
            Q1 = False,
            Q2 = False,
            Q3 = False,
            Q4 = False,
            Q5 = False,
            Q6 = False,
            Q7 = False,
            Q8 = False,
            Q9 = False,
            Q10 = False,
            Q11 = False ,
        )

        user2 = ICTUser(
            username = 'groupB',
            password = 'chiyoda',
            Q1 = False,
            Q2 = False,
            Q3 = False,
            Q4 = False,
            Q5 = False,
            Q6 = False,
            Q7 = False,
            Q8 = False,
            Q9 = False,
            Q10 = False,
            Q11 = False ,
        )

        user3 = ICTUser(
            username = 'groupC',
            password = 'bunkyou',
            Q1 = False,
            Q2 = False,
            Q3 = False,
            Q4 = False,
            Q5 = False,
            Q6 = False,
            Q7 = False,
            Q8 = False,
            Q9 = False,
            Q10 = False,
            Q11 = False ,
        )

        user4 = ICTUser(
            username = 'groupD',
            password = 'sumida',
            Q1 = False,
            Q2 = False,
            Q3 = False,
            Q4 = False,
            Q5 = False,
            Q6 = False,
            Q7 = False,
            Q8 = False,
            Q9 = False,
            Q10 = False,
            Q11 = False ,
        )

        db.session.add_all([Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q9,Q10,Q11,user1,user2,user3,user4])
        db.session.commit()

if __name__ == '__main__':
    setup_database()
