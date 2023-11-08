from flask import render_template, request, redirect
from flask_login import login_user

from app import app, dao, login
from app.models import User


@app.route('/')
def index():
    kw = request.args.get('kw')

    cates = dao.load_categories()
    products = dao.load_products(kw)

    return render_template('index.html', categories=cates, products=products)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter(username == username,password == password).first()
        if user:
            login_user(user=user)
    return redirect("/admin")

if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
