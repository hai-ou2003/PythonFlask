import hashlib
from app import db, app
from app.models import Category, Product, User, UserRole


def load_categories():
    return Category.query.all()


def load_products(kw=None, cate_id=None, page=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))
    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1)*page_size

        return products.slice(start, start + page_size)
    return products.all()

def count_row():# Dem SP
    return Product.query.count()


def create_user(name, username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(name=name, username=username, password=password, user_role=UserRole.User)
    db.session.add(user)
    db.session.commit()


def authenicate_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password.strip())).first()


if __name__ == "__main__":
    with app.app_context():
        # pass
        create_user("hai", "test", "1234567890a@A")
