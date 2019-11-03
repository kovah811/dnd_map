from flask import render_template, request, jsonify, flash

from app import app
from app.forms import AddMarkerForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddMarkerForm()

    return render_template('index.html', title='DnD Map', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route('/logout')
def logout():
    pass


@app.route('/addMarker', methods=['POST'])
def add_marker():
    form = AddMarkerForm()
    if form.validate_on_submit():
        return jsonify(data={'message': 'Added marker: {}'.format(
            form.location_name.data)})
    return jsonify(data=form.errors)
