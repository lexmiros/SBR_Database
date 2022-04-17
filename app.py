from flask import Flask, render_template, url_for, flash, redirect
from graphviz import render
from matplotlib.pyplot import title
from forms import CattleAddForm, FarmAddForm, PaddockAddFrom, StaffAddFrom
import pymysql

conn = pymysql.connect(host='localhost',
                             user='adminflask',
                             password='adminflask',
                             database='project_db_2',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfjkhnfdgjijasdfjk' 




#Home page
@app.route("/")
def home():
    return render_template("home.html", title = "Home Page")

#Farm pages

#Farm view
@app.route("/farm")
def farm():
    return render_template("farm.html", title = "Farms")

#Add farm
@app.route("/farm_add",methods = ['GET','POST'])
def farm_add():
    form = FarmAddForm()
    if form.validate_on_submit():
        c = conn.cursor()
        query = f"INSERT INTO FARM(FarmName, Address)\
                VALUES('{form.name.data}','{form.address.data}')"
        c.execute(query)
        conn.commit()
        
        flash(f'Farm {form.name.data} created', 'success')
        return redirect(url_for('farm'))

    return render_template("farm_add.html", form = form,title = "Add farms")


#Paddock pages

#Paddock view
@app.route("/paddock")
def paddock():
    return(render_template("paddock.html"))

#Add paddock
@app.route("/paddock_add",methods = ['GET','POST'])
def paddock_add():
    form = PaddockAddFrom()
    if form.validate_on_submit():
        c = conn.cursor()
        query = f"INSERT INTO PADDOCK(PaddockName, Size, GrassCondition, FarmName)\
                VALUES('{form.paddockName.data}','{str(form.size.data)}','{form.grassCondition.data}','{form.farmName.data}')"
        c.execute(query)
        conn.commit()
        
        flash(f'Paddock {form.paddockName.data} created', 'success')
        return redirect(url_for('paddock'))

    return render_template("paddock_add.html", form = form, title = "Add paddocks")



#Cattle pages

#Cattle view
@app.route("/cattle")
def cattle():
    return render_template("cattle.html",title = "Cattle")

#Add cattle
@app.route('/cattle_add',methods = ['GET','POST'])
def cattle_add():
    form = CattleAddForm()
    if form.validate_on_submit():
        c = conn.cursor()
        query = f"INSERT INTO CATTLE (Sex, Breed, DateOfBirth, Weight, PaddockName, DateMoved)\
                VALUES('{form.sex.data}','{form.breed.data}','{form.dateOfBirth.data}','{str(form.weight.data)}','{str(form.paddockName.data)}','{form.dateMoved.data}')"
        c.execute(query)
        conn.commit()
        
        flash(f'Cattle added to {form.paddockName.data}', 'success')
        return redirect(url_for('cattle'))

    return render_template("cattle_add.html", form = form, title = "Add cattle")

#Staff pages

#staff homepage
@app.route("/staff_home")
def staff_home():
    return render_template("staff_home.html", title = "Staff")

#Add staff
@app.route("/staff_add", methods = ['GET','POST'])
def staff_add():   
    form = StaffAddFrom()
    if form.validate_on_submit():
        #print(form.dateOfBirth.data)
        c = conn.cursor()

        query = f"insert into STAFF(FirstName, LastName, DateOfBirth, FarmName, StartDate, ManagerID, PrimaryContactNumber)\
         VALUES ('{form.firstName.data}','{form.lastName.data}','{str(form.dateOfBirth.data)}','{form.farmLoc.data}','{str(form.startDate.data)}','{str(form.managerID.data)}' ,'{str(form.contactNumber.data)}')"
        c.execute(query) #Execute the query
        conn.commit() #Commit the changes
        
        flash(f'Staff member created for {form.firstName.data}', 'success')
        return redirect(url_for('staff_home'))
    
    return render_template("staff_add.html", form = form, title = "Add staff")


#Vehicle pages
@app.route("/vehicles")
def vehicles():
    return render_template("vehicles.html")


if __name__ == "__main__":
    app.run(debug = True)