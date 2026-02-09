from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class AnswerForm(FlaskForm):
    questionnumber = SelectField(
        'Questionを選択してください',choices=[
            ('Q1', 'Question1'),
            ('Q2', 'Question2'),
            ('Q3', 'Question3'),
            ('Q4', 'Question4'),
            ('Q5', 'Question5'),
            ('Q6', 'Question6'),
            ('Q7', 'Question7'),
            ('Q8', 'Question8'),
            ('Q9', 'Question9'),
            ('Q10', 'Question10'),
            ('Q11', 'Question11'),
        ]
    )
    answer = StringField(
        "Answerをひらがなで入力してください", validators=[DataRequired(), Length(min=2, max=80)]
    )
    submit = SubmitField("送信")

class LoginForm(FlaskForm):
    username = SelectField(
        'グループ名を選択してください',choices=[
            ('groupA', 'グループA'),
            ('groupB', 'グループB'),
            ('groupC', 'グループC'),
            ('groupD', 'グループD'),
        ])
    password = StringField("パスワード", validators=[DataRequired(), Length(max=80)])
    submit = SubmitField("ログイン")


class FinalForm(FlaskForm):
    finalanswer = StringField("解答（半角英数字で入力してください）", validators=[DataRequired(), Length(max=80)])
    submit = SubmitField("送信")
