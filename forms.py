from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class StuDetailsForm(FlaskForm):
    fName = StringField('Given name: ', validators=[DataRequired()])
    sName = StringField('Surname: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FindStudent(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    submit = SubmitField('Submit')