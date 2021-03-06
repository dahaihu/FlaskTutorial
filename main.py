from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import User, Role
from app.models import db
from app.models import UserModelView, RoleModelView
app = Flask(__name__)
# mac下的密码是 hscxrzs1st
# ubuntu下的密码是 669193
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:hscxrzs1st@localhost/first_flask'
# 这个不设置的话，会出现不可以修改数据库的内容
app.config['SECRET_KEY'] = 'Mr.hu is handsome boy'
# 初始化数据库
db.init_app(app)
admin = Admin(app, name="Mr.Hu's test")
admin.add_view(UserModelView(User, db.session))
admin.add_view(RoleModelView(Role, db.session))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
