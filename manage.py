from flask.ext.script import Manager
from app import db

from flask import Flask
app = Flask(__name__)

manager = Manager(app)

@manager.command
def create():
    db.create_all()

@manager.command
def drop():
    db.drop_all()

@manager.command
def recreate():
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    manager.run()