from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap5
from forms import LoginForm , BookRequestForm

# Webアプリを作成し、appという変数に代入する
app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_KEY_FOR_DEVELOPMENT"
Bootstrap5(app)
@app.route("/login", methods=["GET", "POST"])
def login():
    user_id = session.get("user_id")
    if user_id: #user_idが空では無かったら
        return redirect(url_for("index"))   

    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == "tamapass" and form.username.data == "tama":
            session["user_id"] = 100
            flash("ログインに成功しました", "success")
            return redirect(url_for("index"))
        else:
            flash("ユーザーIDまたはパスワードが間違っています", "danger")
    return render_template("login.html", form=form)


# このファイルが直接実行された場合にサーバーを起動
@app.route("/")
def index():
    if not session.get("user_id"): #user_idが空なら
        return redirect(url_for("login"))

    today = datetime.now().strftime("%Y年%m月%d日")
    return_deadline = (datetime.now() + timedelta(weeks=2)).strftime("%Y年%m月%d日")
    
    return render_template("index.html", today=today, return_deadline=return_deadline, username="tama")

# リクエスト申請用
request_list_data = []

@app.route("/request_book", methods=["GET", "POST"])
def request_book():
    form = BookRequestForm()
    if form.validate_on_submit():
        request_list_data.append(
            {
                "title": form.title.data,
                "author": form.author.data,
                "reason": form.reason.data,
            }
        )
        return redirect(url_for("request_list"))
    return render_template("request_form.html", form=form, username="tama")

#申請リスト
@app.route("/request_list")
def request_list():
    return render_template("request_list.html", requests=request_list_data, username="tama")

#ログアウト
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("ログアウトしました", "success")
    return redirect(url_for("login"))

if __name__ == '__main__':
    # debug=Trueにすると、コードを変更したときに自動で再起動される
    app.run(debug=True)