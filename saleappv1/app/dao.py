import hashlib
from app import db,app
from app.models import Category, Product, User


def load_categories():
    return Category.query.all()


def load_products(kw=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()


def create_user(name, username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name, username=username, password=password)
    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        #pass
        create_user("hai", "test", "1234567890a@A")