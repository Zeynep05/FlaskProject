from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms import validators, DecimalField


class AddFahrradForm(FlaskForm):
    Model = StringField("Model",  validators=[validators.InputRequired()])
    Farbe = StringField("Farbe",  validators=[validators.InputRequired()])
    Reifen = StringField("Reifen", validators=[validators.InputRequired()])
    Preis = DecimalField("Preis",  validators=[validators.InputRequired()])
