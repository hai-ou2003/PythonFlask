from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app import db, app
from app.models import Category, Product

class ProductView(ModelView):
    column_list = ['name', 'price', 'category']
    can_view_details = True
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['price']
    column_editable_list = ['name', 'price', ]
class CategoryView(ModelView):
    column_list = ['name', 'products']
    can_view_details = True
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['name']
    column_editable_list = ['name', 'products']

class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')


app.config['SECRET_KEY'] = 'hfsahgjkahgtiusahgi'
admin = Admin(app=app, name="QUAN TRI BAN HANG", template_mode='bootstrap4')
admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StatsView(name="THỐNG KÊ BÁO CÁO"))
