import os

# 通过对象来配置flask
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'