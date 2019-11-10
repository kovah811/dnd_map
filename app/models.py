from flask import current_app
from flask_login import UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    fullname = db.Column(db.String(100))
    picture = db.Column(db.String(2083))
    email = db.Column(db.String(256), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    access = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.access == current_app.config.ACCESS.get('admin')

    def allowed(self, access_level):
        return self.access >= access_level


class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)
