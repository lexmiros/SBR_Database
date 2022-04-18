from flask import Flask, render_template, url_for, flash, redirect
from forms import BinAddForm, CattleAddForm, FarmAddForm, MotorbikeAddForm, PaddockAddFrom, StaffAddFrom
import pymysql



conn = pymysql.connect(host='localhost',
                             user='adminflask',
                             password='adminflask',
                             database='project_db_2',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )

#Turn the results from the database into a dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfjkhnfdgjijasdfjk' 


"""
Routes for select pages : home pages
"""

#Home page
@app.route("/")
def home():
    return render_template("home.html", title = "Home Page")

#Farm view
@app.route("/farm")
def farm():
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM farm")
    posts = c.fetchall()
    return render_template('farm.html', posts=posts)
    

#Paddock view
@app.route("/paddock")
def paddock():
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM paddock")
    posts = c.fetchall()
    return render_template('paddock.html', posts=posts)

#Cattle view
@app.route("/cattle")
def cattle():
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM cattle")
    posts = c.fetchall()
    return render_template('cattle.html', posts=posts)

#Vehicle pages
@app.route("/vehicles")
def vehicles():
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM vehicles INNER JOIN vehicle_brands ON vehicles.VehicleID=vehicle_brands.VehicleID LEFT JOIN motorbikes ON vehicles.VehicleID=motorbikes.VehicleID LEFT JOIN quadbikes ON vehicles.VehicleID=quadbikes.VehicleID LEFT JOIN buggies ON vehicles.VehicleID=buggies.VehicleID;")
    posts = c.fetchall()
    return render_template('vehicles.html', posts=posts)
#staff homepage
@app.route("/staff_home")
def staff_home():
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM staff;")
    posts = c.fetchall()
    return render_template('staff.html', posts=posts)

"""
Routes for insert functionalty : Add pages
"""

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

#Add feed bin
@app.route("/bin_add", methods = ['GET', 'POST'])
def bin_add():
    form = BinAddForm()
    if form.validate_on_submit():
        c = conn.cursor()

        query = f"INSERT INTO feed_bins(BinNumber, PaddockName, LastChecked, BinContains, BinLevel) \
        VALUES('{form.binNumber.data}','{form.paddockName.data}','{form.lastChecked.data}','{form.binContains.data}','{form.binLevel.data}')"

        c.execute(query)
        conn.commit()

        flash(f"Bin {form.binNumber.data} added in paddock {form.paddockName.data}")

        return redirect(url_for('paddock'))

    return render_template("bin_add.html", form = form, title = "Add bin")

#Add motorbike
##INCOMPLETE
@app.route("/motorbike_add", methods = ['GET', 'POST'])
def motorbike_add():
    form = MotorbikeAddForm()
    if form.validate_on_submit():
        c = conn.cursor()

        query = f"INSERT INTO vehicles(Model, FarmName, PurchaseDate) \
        VALUES('{form.model.data}','{form.farmName.data}','{form.purchaseDate.data}')"

        c.execute(query)
        conn.commit()

        query = f"INSERT INTO motorbikes(Model, FarmName, PurchaseDate) \
        VALUES('{form.model.data}','{form.farmName.data}','{form.purchaseDate.data}')"

        c.execute(query)
        conn.commit()


        flash(f"Motorbike {form.vehicleID.data} added to {form.farmName.data}")

        return redirect(url_for('vehicles'))

    return render_template("motorbike_add.html", form = form, title = "Add motorbike")



"""
Routes for delete functionality : delete pages
"""
#Delete Farm
@app.route("/farm/delete/<farmName>", methods=['POST'])
def delete_farm(farmName):
    c = conn.cursor()
    current_farm= farmName
    query = f"DELETE FROM farm WHERE FarmName = '{current_farm}'"
    c.execute(query)
    conn.commit()
    return redirect(url_for('farm'))

@app.route("/staff/delete/<int:staffID>", methods=['POST'])
def delete_staff(staffID):
    c = conn.cursor()
    current_id = staffID
    query = f"DELETE FROM staff WHERE StaffID = {current_id}"
    c.execute(query)
    conn.commit()
    return redirect(url_for('staff_home'))

@app.route("/cattle/delete/<int:cattleID>", methods=['POST'])
def delete_cattle(cattleID):
    c = conn.cursor()
    current_id = cattleID
    query = f"DELETE FROM cattle WHERE CattleID = '{current_id}'"
    c.execute(query)
    conn.commit()
    return redirect(url_for('cattle'))





if __name__ == "__main__":
    app.run(debug = True)
    
