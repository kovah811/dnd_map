from flask import (
    render_template,
    redirect,
    jsonify,
    flash,
    url_for,
    request,
)
from flask_login import current_user, login_user, logout_user, login_required
from http.client import HTTPResponse
from werkzeug.urls import url_parse

from app import app
from app.forms import AddMarkerForm, LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    form = AddMarkerForm()

    return render_template('index.html', title='DnD Map', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Log in', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/addMarker', methods=['POST'])
def add_marker():
    form = AddMarkerForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            return jsonify(
                {'message': 'Added marker: {}'.format(form.location_name.data)}
            )
        else:
            return jsonify(
                {
                    'message': 'Not authorized',
                    'url': url_for('login') + '?next=/',
                }
            )  # Not sure about this...
    return jsonify(data=form.errors)
