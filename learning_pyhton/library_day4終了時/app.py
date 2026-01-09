from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap5
from forms import LoginForm , BookRequestForm , SearchForm
from models import db, User , BookRequest, Book, Loan
from werkzeug.security import check_password_hash
from sqlalchemy import or_

# Webアプリを作成し、appという変数に代入する
app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_KEY_FOR_DEVELOPMENT"
Bootstrap5(app)

#DB参照用
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)

#ログイン
@app.route("/login", methods=["GET", "POST"])
def login():
    #user_id = session.get("user_id")
    #if not user_id:
    #    return redirect(url_for("login"))

    form = LoginForm()
    if form.validate_on_submit():

        #DBから読み出し
        #with app.app_context(): #なくてもいい
            user = User.query.filter_by(username = form.username.data).first()
            if user and check_password_hash(user.password_hash , form.password.data) == True:
                session["user_id"] = user.id
                flash("ログインに成功しました", "success")
                
                return redirect(url_for("index"))
            else:
                flash("ユーザーIDまたはパスワードが間違っています", "danger")

    return render_template("login.html", form=form)

# このファイルが直接実行された場合にサーバーを起動
@app.route("/")
def index():
    user_id = session.get("user_id")
    if not session.get("user_id"): #user_idが空なら
        return redirect(url_for("login"))
    
    current_user = User.query.get(user_id)

    today = datetime.now().strftime("%Y年%m月%d日")
    return_deadline = (datetime.now() + timedelta(weeks=2)).strftime("%Y年%m月%d日")
    
    return render_template(
        "index.html", 
        today=today, 
        return_deadline=return_deadline, 
        username=current_user.username,
    )

# リクエスト申請用
#request_list_data = []

@app.route("/request_book", methods=["GET", "POST"])
def request_book():

    #ログインを強制
    user_id = session.get("user_id")
    if not session.get("user_id"): #user_idが空なら
        return redirect(url_for("login"))
    #ユーザー名を変数に格納
    current_user = User.query.get(user_id)

    form = BookRequestForm()

    if form.validate_on_submit():
        
        #DBを検索
        #with app.app_context(): #なくてもいい
        book_request = BookRequest(
            title = form.title.data,
            author = form.author.data,
            reason = form.reason.data
        )
        db.session.add(book_request)
        db.session.commit()

        return redirect(url_for("request_list"))
    return render_template("request_form.html", form=form, username=current_user.username)

#申請リスト
@app.route("/request_list")
def request_list():
    #ログインを強制
    user_id = session.get("user_id")
    if not session.get("user_id"): #user_idが空なら
        return redirect(url_for("login"))
    #ユーザー名を変数に格納
    current_user = User.query.get(user_id)

    #DBから引っ張る処理
    book_requests = BookRequest.query.all()

    return render_template("request_list.html", requests=book_requests, username=current_user.username)

#ログアウト
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("ログアウトしました", "success")
    return redirect(url_for("login"))

#書籍検索
@app.route("/search", methods=["GET", "POST"])
def search():

    #ログインを強制
    user_id = session.get("user_id")
    if not session.get("user_id"): #user_idが空なら
        return redirect(url_for("login"))
    #ユーザー名を変数に格納
    current_user = User.query.get(user_id)

    form = SearchForm()
    books = [] 
    #return render_template("search.html", form=form, books = books,…で使用するが、
    # Book.query.filterでヒットしないとundifinedのままになる

    if form.validate_on_submit():
        
        #DBから検索
        #with app.app_context(): #なくてもいい
        search_term = form.search_term.data
        search_pattern = f"%{search_term}%"
        books = Book.query.filter(or_(Book.title.like(search_pattern),Book.author.like(search_pattern))).all()

        if not books :
            flash(f"「{search_term}」に一致する書籍は見つかりませんでした。", "info")

    return render_template("search.html", form=form, books = books, username=current_user.username)

#借りる処理
@app.route("/borrow/<int:book_id>", methods=["POST"])
def borrow(book_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    current_user = User.query.get(user_id)

    book = Book.query.get_or_404(book_id)

    if book.is_borrowed:
        flash("この書籍はすでに貸出中です", "warning")
        return redirect(url_for("search"))

    loan = Loan(user=current_user, book=book)
    db.session.add(loan)
    db.session.commit()

    flash(f"「{book.title}」を借りました", "success")
    return redirect(url_for("search"))

#借りている本一覧
@app.route("/borrowed_books")
def borrowed_books():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    current_user = User.query.get(user_id)
    borrowed_list = Loan.query.filter_by(user=current_user, returned_at=None).all()

    return render_template(
        "borrowed_books.html", borrowed_list=borrowed_list, username=current_user.username
    )

#返却処理
@app.route("/return_book/<int:loan_id>", methods=["POST"])
def return_book(loan_id):
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))
    current_user = User.query.get(user_id)

    loan = Loan.query.filter_by(
        id=loan_id, user=current_user, returned_at=None
    ).first_or_404()
    if not loan:
        flash("返却できる貸出情報が見つかりません", "warning")
        return redirect(url_for("search"))
    loan.returned_at = db.func.now()
    db.session.commit()

    flash("返却しました", "success")
    return redirect(url_for("borrowed_books"))

if __name__ == '__main__':
    # debug=Trueにすると、コードを変更したときに自動で再起動される
    app.run(debug=True)