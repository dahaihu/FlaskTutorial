from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from wtforms.validators import required

db = SQLAlchemy()


class RoleModelView(ModelView):
    pass
    # # 这个是干什么的呢, 擦，看着没什么用啊
    # form_ajax_refs = {
    #     'users': {
    #         'fields': ['name', 'email'],
    #         'page_size': 10
    #     }
    # }


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 给Role类创建一个uses属性，关联users表。
    # backref是反向的给User类创建一个role属性，关联roles表。这是flask特殊的属性。
    users = db.relationship('User', backref="role")

    # 相当于__str__方法。
    def __repr__(self):
        return "Role: %s %s" % (self.id, self.name)


class UserModelView(ModelView):
    list_template = 'custom_list.html'
    # # 目前没看出来这玩意儿有什么用
    # # 这玩意儿到底有什么用呢，我日
    # # 这个是在创建的时候显示的，会有竖着的三栏， 但是这个创建的Foobar后面是空着的
    # form_create_rules = ('name', rules.Text('Foobar'), 'email', 'password')

    # # 下面这个得琢磨琢磨是用来做什么的了
    # form_extra_fields = ('hehehehehe')

    # 这个又是什么东西呢？
    create_modal = True
    edit_modal = True

    # 这个里面所谓的表格都指的是，编辑和创建的时候的表格
    # 这个相当于在床架你的时候，给name这个值进行有限制的选择，会有一个下拉栏的
    # 但是为什么是元组呢？ 难道是一个映射吗
    # 显示的是前面，设置的是后面
    form_choices = {
        'password': [
            ('1', '111111'),
            ('2', '222222'),
            ('3', '333333'),
            ('4', '444444'),
            ('5', '555555')
        ]
    }

    # 这个东西又是什么东西呢？
    # 在创建和编辑的时候，name字段，显示的事First Name,但是呢，这个必须存在
    form_args = {
        'name': {
            'label': 'First Name',
            'validators': [required()]
        }
    }

    # 这个是什么用的呢, 真的没看懂这个到底是干嘛的
    # 这个style中似乎是在编辑和创建的时候，输入的name或者显示的name为红色
    # 那么这个rows的参数用来干什么呢
    form_widget_args = {
        'name': {
            'rows': 10,
            'style': 'color: red'
        }
    }


class User(db.Model):
    # 给表重新定义一个名称，默认名称是类名的小写，比如该类默认的表名是user。
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(16))
    # 创建一个外键，和django不一样。flask需要指定具体的字段创建外键，不能根据类名创建外键
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "User: %s %s %s %s" % (self.id, self.name, self.password, self.role_id)