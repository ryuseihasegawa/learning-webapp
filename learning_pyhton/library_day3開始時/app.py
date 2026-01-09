from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from forms import BookRequestForm, LoginForm 

# Webアプリを作成し、appという変数に代入する
app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_KEY_FOR_DEVELOPMENT"
Bootstrap5(app)
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == "tamapass" and form.username.data == "tama":
            flash("ログインに成功しました", "success")
            return redirect(url_for("index"))
        else:
            flash("ユーザーIDまたはパスワードが間違っています", "danger")
    return render_template("login.html", form=form)


# このファイルが直接実行された場合にサーバーを起動
@app.route("/")
def index():
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
@app.route("/request_list")
def request_list():
    return render_template("request_list.html", requests=request_list_data, username="tama")


if __name__ == '__main__':
    # debug=Trueにすると、コードを変更したときに自動で再起動される
    app.run(debug=True)