from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo 


class StaffAddFrom(FlaskForm):
    staffID = IntegerField("Staff ID")
    firstName = StringField('FirstName', validators=[DataRequired(), Length(min = 2, max = 20)])
    lastName = StringField('LastName', validators=[DataRequired(), Length(min = 2, max = 20)])
    dateOfBirth = DateField("Date of birth", validators=[DataRequired()])
    startDate = DateField("Start Date", validators=[DataRequired()])
    managerID = IntegerField("Manager ID if applicable")
    farmLoc = StringField("Staff's primary farm", validators=[DataRequired()])
    submit = SubmitField("Add Staff")

