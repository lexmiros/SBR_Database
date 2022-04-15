from flask import Flask, render_template, url_for, flash, redirect
from graphviz import render
from forms import StaffAddFrom

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfjkhnfdgjijasdfjk' 

cattle_data = [
    {"ID" : 1,
    "Weight" : 900,
    "Sex" : "Male",
    "Age" : 10},
    {"ID" : 2,
    "Weight" : 850,
    "Sex" : "Female",
    "Age" : 20},
]

#Home page
@app.route("/")
def home():
    return render_template("home.html")


#Cattle pages
@app.route("/cattle")
def cattle():
    return render_template("cattle.html", cattle_info = cattle_data, title = "Cattle")


#Staff pages

#staff homepage
@app.route("/staff_home")
def staff_home():
    return render_template("staff_home.html")

#Add staff
@app.route("/staff_add", methods = ['GET','POST'])
def staff_add():   
    form = StaffAddFrom()
    if form.validate_on_submit():
        flash(f'Staff member created for {form.firstName.data}', 'success')
        return redirect(url_for('staff_home'))
    
    return render_template("staff_add.html", form = form)


#Vehicle pages
@app.route("/vehicles")
def vehicles():
    return render_template("vehicles.html")


if __name__ == "__main__":
    app.run(debug = True)