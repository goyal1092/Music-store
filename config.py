import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'app.db')

CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = '1234secure$#@!'