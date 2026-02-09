from flask import Flask, render_template, redirect, url_for, flash, session, abort
from flask_bootstrap import Bootstrap5
from forms import AnswerForm, LoginForm,FinalForm
from models import db, Answer, ICTUser

# Webアプリを作成し、appという変数に代入する
app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY_FOR_DEVELOPMENT"
Bootstrap5(app)

# DB参照用
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ICTnazotoki.db"
db.init_app(app)


# ログイン
@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        # DBから読み出し
        user = ICTUser.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data :
            session["user_id"] = user.id
            flash("ログインに成功しました", "success")

            return redirect(url_for("index"))
        else:
            flash("パスワードが間違っています", "danger")

    return render_template("login.html", form=form)


#ログアウト
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("ログアウトしました", "success")
    return redirect(url_for("login"))

# 回答の入力
# このファイルが直接実行された場合にサーバーを起動
@app.route("/", methods=["GET", "POST"])
def index():

    user_id = session.get("user_id")
    if not user_id:  # user_idが空なら
        return redirect(url_for("login"))

    # ログインユーザー（動的）を取得
    user = ICTUser.query.get(user_id)
    if user is None:
        # セッションが古い/ユーザー削除など
        return redirect(url_for("login"))

    form = AnswerForm()
    if form.validate_on_submit():

        # DBから読み出し
        quesition = Answer.query.filter_by(
            questionnumber=form.questionnumber.data
        ).first()
        if quesition and quesition.correctanswer == form.answer.data:

            flash("正解です！", "success")

            ##DB上の回答済みフラグを変更

            col_name = form.questionnumber.data  # "Q3" など

            #  列名ホワイトリスト（安全対策）
            allowed = {f"Q{i}" for i in range(1, 12)}
            if col_name not in allowed:
                abort(400, "invalid question number")

            #  指定カラムを True に更新
            setattr(user, col_name, True)
            db.session.commit()

            return redirect(url_for("index"))
        else:
            flash("間違っています", "danger")

    # 回答済みの問題を表示

    # ① 正解済み（True）の Q を抽出
    solved_qs = [f"Q{i}" for i in range(1, 12) if getattr(user, f"Q{i}") is True]
    # ② Answer をまとめて取得（IN検索）
    answers = Answer.query.filter(Answer.questionnumber.in_(solved_qs)).all()
    # ③ questionnumber -> correctanswer の辞書にする（テンプレで扱いやすい）
    answer_map = {a.questionnumber: a.correctanswer for a in answers}
    # ④ 表示用リスト（順番を Q1..Q11 に揃える）
    solved_list = [
        {"q": q, "answer": answer_map.get(q, "（答え未登録）")} for q in solved_qs
    ]

    # ✅ ③ 全問正解判定（Q1〜Q11が全部TrueならTrue）
    all_solved = all(getattr(user, f"Q{i}") is True for i in range(1, 12))

    return render_template(
        "index.html", form=form, solved_list=solved_list, all_solved=all_solved
    )


# 最終問題
@app.route("/final", methods=["GET", "POST"])
def final():

    user_id = session.get("user_id")
    if not user_id:  # user_idが空なら
        return redirect(url_for("login"))

    # ログインユーザー（動的）を取得
    user = ICTUser.query.get(user_id)
    if user is None:
        # セッションが古い/ユーザー削除など
        return redirect(url_for("login"))
    
    # 全問正解チェック（直URLガード）
    if not all(getattr(user, f"Q{i}") is True for i in range(1, 12)):
        flash("最終問題は全問正解後に表示されます", "warning")
        return redirect(url_for("index"))

    form = FinalForm()
    passphrase = "フォローアップ"  
    correctanswer = "directory"

    if form.validate_on_submit():
        submitted = form.finalanswer.data.strip()
        if correctanswer == submitted:

            return redirect(url_for("goal"))
        else:
            flash("残念、不正解です！", "danger")
        
    return render_template("final.html", form=form, passphrase=passphrase)

@app.route("/goal", methods=["GET"])
def goal():

    user_id = session.get("user_id")
    if not user_id:  # user_idが空なら
        return redirect(url_for("login"))

    # ログインユーザー（動的）を取得
    user = ICTUser.query.get(user_id)
    if user is None:
        # セッションが古い/ユーザー削除など
        return redirect(url_for("login"))
    
    return render_template("goal.html")

@app.route("/hint", methods=["GET"])
def hint():
    return render_template("hint.html")


if __name__ == "__main__":
    # debug=Trueにすると、コードを変更したときに自動で再起動される
    app.run(debug=True)
