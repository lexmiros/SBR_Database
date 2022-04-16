from decimal import ROUND_UP
from random import choices
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,PasswordField, SubmitField, BooleanField, DateField, SelectField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo 


class StaffAddFrom(FlaskForm):
    #staffID = IntegerField("Staff ID")
    firstName = StringField('FirstName', validators=[DataRequired(), Length(min = 2, max = 20)])
    lastName = StringField('LastName', validators=[DataRequired(), Length(min = 2, max = 20)])
    dateOfBirth = DateField("Date of birth", validators=[DataRequired()])
    startDate = DateField("Start Date", validators=[DataRequired()])
    managerID = StringField("Manager ID if applicable")
    farmLoc = StringField("Staff's primary farm", validators=[DataRequired()])
    contactNumber = IntegerField("Primary Contact Number", validators=[DataRequired()])
    submit = SubmitField("Add Staff")

class CattleAddForm(FlaskForm):
    sex = SelectField("Sex: ", choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    breed = SelectField("Brred: ", choices=[('Belmont Red', 'Belmont Red'), ('Angus', 'Angus'), ('Cross', 'Cross')], validators=[DataRequired()])
    dateOfBirth = DateField("Date of birth", validators=[DataRequired()])
    weight = DecimalField("Weight", places = 2, rounding = ROUND_UP,validators=[DataRequired()])
    paddockName = StringField("Paddock name: ", validators=[DataRequired()])
    dateMoved = DateField("Date moved to paddock", validators=[DataRequired()])
    submit = SubmitField("Add Cattle")