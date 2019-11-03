from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class AddMarkerForm(FlaskForm):
    location_name = StringField('Location name', validators=[DataRequired()])
    wiki_link = StringField('Wiki link')
    latitude = FloatField('Latitude', validators=[DataRequired()])
    longitude = FloatField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Save')
