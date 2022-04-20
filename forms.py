from decimal import ROUND_UP
from random import choices
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,PasswordField, SubmitField, BooleanField, DateField, SelectField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo 
"""
Forms for select functionality
"""


"""
Forms for insert fucnitonality 
"""
class StaffAddFrom(FlaskForm):
    staffID = IntegerField("Staff ID", validators=[DataRequired()])
    firstName = StringField('FirstName : ', validators=[DataRequired(), Length(min = 2, max = 20)])
    lastName = StringField('LastName : ', validators=[DataRequired(), Length(min = 2, max = 20)])
    dateOfBirth = DateField("Date of birth : ", validators=[DataRequired()])
    startDate = DateField("Start Date : ", validators=[DataRequired()])
    managerID = StringField("Manager ID if applicable : ")
    farmLoc = StringField("Staff's primary farm : ", validators=[DataRequired()])
    contactNumber = IntegerField("Primary Contact Number : ", validators=[DataRequired()])
    submit = SubmitField("Add Staff")
    submit_update = SubmitField("Update Staff")

class CattleAddForm(FlaskForm):
    ID = IntegerField("Cattle ID : ", validators=[DataRequired()])
    sex = SelectField("Sex: ", choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    breed = SelectField("Breed: ", choices=[('Belmont Red', 'Belmont Red'), ('Angus', 'Angus'), ('Cross', 'Cross')], validators=[DataRequired()])
    dateOfBirth = DateField("Date of birth", validators=[DataRequired()])
    weight = DecimalField("Weight", places = 2, rounding = ROUND_UP,validators=[DataRequired()])
    paddockName = StringField("Paddock name: ", validators=[DataRequired()])
    dateMoved = DateField("Date moved to paddock", validators=[DataRequired()])
    submit = SubmitField("Add Cattle")
    submit_update = SubmitField("Update Cattle")

class FarmAddForm(FlaskForm):
    name = StringField("Name of the farm: ",validators=[DataRequired(), Length(min = 2, max = 20)] )
    address = StringField("Address : Street # Street name, Suburb, State, Postcode :", validators=[DataRequired()])
    submit = SubmitField("Add Farm")
    submit_update = SubmitField("Update Farm")

class PaddockAddFrom(FlaskForm):
    paddockName = StringField("Name of the paddock : ", validators=[DataRequired(), Length(min = 2, max = 20)] )
    size =  DecimalField("Paddock size : ", places = 2, rounding = ROUND_UP,validators=[DataRequired()])
    grassCondition = SelectField("Grass condition : ", choices=[('Green', 'Green'), ('Dry', 'Dry')], validators=[DataRequired()])
    farmName = StringField("Containing farm name : ", validators=[DataRequired()])
    submit = SubmitField("Add Paddock")
    submit_update = SubmitField("Update Paddock")

class BinAddForm(FlaskForm):
    binNumber = IntegerField("Bin number", validators=[DataRequired()])
    paddockName = StringField("Name of the paddock : ", validators=[DataRequired(), Length(min = 2, max = 20)] )
    lastChecked = DateField("Date bin was last checked :", validators=[DataRequired()])
    binContains = SelectField("Bin contains ", choices=[('Wheat', 'Wheat'), ('Salt Lick', 'Salt Lick'), ('Sorghum','Sorghum')], validators=[DataRequired()])
    binLevel = DecimalField("Bin level between 0 (empty) to 1 (full))", places = 2, rounding = ROUND_UP,validators=[DataRequired()])
    
    submit = SubmitField("Add Bin")

class MotorbikeAddForm(FlaskForm):
    #vehicleID = IntegerField("Vehicle ID", validators=[DataRequired()])
    model = StringField("Vehicle model : ", validators=[DataRequired()])
    brand = StringField("Vehicle brand : ", validators=[DataRequired()])
    farmName = StringField("Containing farm name : ", validators=[DataRequired()])
    purchaseDate = DateField("Date purchased", validators=[DataRequired()])
    engineCC = IntegerField("Motorbike engine CC", validators=[DataRequired()])
    submit = SubmitField("Add Motorbike")

class QuadbikeAddForm(FlaskForm):
    #vehicleID = IntegerField("Vehicle ID", validators=[DataRequired()])
    model = StringField("Vehicle model : ", validators=[DataRequired()])
    brand = StringField("Vehicle brand : ", validators=[DataRequired()])
    farmName = StringField("Containing farm name : ", validators=[DataRequired()])
    purchaseDate = DateField("Date purchased", validators=[DataRequired()])
    rollCage = SelectField("Roll cage attached: ", choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    submit = SubmitField("Add Quadbike")


class BuggiesAddForm(FlaskForm):
    #vehicleID = IntegerField("Vehicle ID", validators=[DataRequired()])
    model = StringField("Vehicle model : ", validators=[DataRequired()])
    brand = StringField("Vehicle brand : ", validators=[DataRequired()])
    farmName = StringField("Containing farm name : ", validators=[DataRequired()])
    purchaseDate = DateField("Date purchased", validators=[DataRequired()])
    numberOfSeats = IntegerField("Number of Seats", validators=[DataRequired()])
    submit = SubmitField("Add Buggy")
