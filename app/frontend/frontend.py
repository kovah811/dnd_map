from flask import jsonify, render_template, url_for
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_login import current_user
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator

from app.frontend import bp
from app.forms import AddMarkerForm
from .nav import nav, ExtendedNavbar


@nav.navigation()
def frontend_top():
    # Sample navbar with left and right align
    # TODO: Adapt to dnd map and incorporate dynamic logged in/out nav items
    return ExtendedNavbar(
        title=View('Flask-Bootstrap', 'frontend.index'),
        root_class='navbar navbar-inverse',
        items=(
            View('Home', 'frontend.index'),
            View('Debug-Info', 'frontend.index'),
            Subgroup(
                'Docs',
                Link(
                    'Flask-Bootstrap',
                    'http://pythonhosted.org/Flask-Bootstrap',
                ),
                Link(
                    'Flask-AppConfig', 'https://github.com/mbr/flask-appconfig'
                ),
                Link('Flask-Debug', 'https://github.com/mbr/flask-debug'),
                Separator(),
                Text('Bootstrap'),
                Link(
                    'Getting started',
                    'http://getbootstrap.com/getting-started/',
                ),
                Link('CSS', 'http://getbootstrap.com/css/'),
                Link('Components', 'http://getbootstrap.com/components/'),
                Link('Javascript', 'http://getbootstrap.com/javascript/'),
                Link('Customize', 'http://getbootstrap.com/customize/'),
            ),
        ),
        right_items=(
            Text('Using Flask-Bootstrap {}'.format(FLASK_BOOTSTRAP_VERSION)),
            View('SignUp', 'frontend.index'),
        ),
    )


@bp.route('/')
def index():
    form = AddMarkerForm()

    return render_template('index.html', form=form)


@bp.route('/addMarker', methods=['POST'])
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
