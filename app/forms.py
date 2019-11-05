from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


class AddMarkerForm(FlaskForm):
    location_name = StringField('Location name', validators=[DataRequired()])
    wiki_link = StringField('Wiki link')
    latitude = FloatField('Latitude', validators=[DataRequired()])
    longitude = FloatField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Save')
