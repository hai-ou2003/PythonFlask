import math

from flask import render_template, request, redirect
from flask_login import login_user, login_manager
import hashlib
from app import app, dao, login
from app.models import User


@app.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')
    cates = dao.load_categories()
    num = dao.count_row()
    products = dao.load_products(kw, cate_id, page)

    return render_template('index.html', categories=cates, products=products,
                           pages=math.ceil(num/app.config['PAGE_SIZE']))


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = dao.authenicate_user(username, password)
        if user:
            login_user(user=user)
    return redirect("/admin")


if __name__ == '__main__':
    from app import admin

    app.run(debug=True)
