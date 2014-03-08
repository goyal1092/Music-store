from app import db
from flask.ext.login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    playlist = db.relationship('Playlist', backref='list_contents', lazy='dynamic')


class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    playlist = db.relationship('Playlist', backref='song_list', lazy='dynamic')

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    songs_id = db.Column(db.Integer, db.ForeignKey('songs.id'))