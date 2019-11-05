from flask import (
    render_template,
    jsonify,
    url_for,
)
from flask_login import current_user


from app import app
from app.forms import AddMarkerForm


@app.route('/')
@app.route('/index')
def index():
    form = AddMarkerForm()

    return render_template('index.html', title='DnD Map', form=form)


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
                    'url': url_for('auth.login') + '?next=/',
                }
            )  # Not sure about this...
    return jsonify(data=form.errors)
