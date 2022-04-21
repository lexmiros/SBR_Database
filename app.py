from operator import add
from flask import Flask, render_template, url_for, flash, redirect
from forms import BinAddForm, BinUpdateForm, BuggiesAddForm, BuggiesUpdateForm, CattleAddForm, CattleUpdateForm, FarmAddForm, MotorbikeAddForm, MotorbikeUpdateForm, PaddockAddFrom, QuadbikeAddForm, QuadbikeUpdateForm, StaffAddFrom
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

#Farm Stats
@app.route("/farm/stats/<farmName>", methods = ["POST", "GET"])  
def farm_stats(farmName):
    #Get total number of staff for the farm
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(staffID) FROM staff WHERE FarmName = '{farmName}' ")
    staffNumbers = c.fetchall()
    for numbers in staffNumbers:
        countStaff = numbers["COUNT(staffID)"]


    #Get total number of staff for the paddocks
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(PaddockName) FROM paddock WHERE FarmName = '{farmName}' ")
    paddockNumbers = c.fetchall()
    for numbers in paddockNumbers:
        countPaddock = numbers["COUNT(PaddockName)"]

     #Get total number of staff for the vehicles
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(VehicleID) FROM vehicles WHERE FarmName = '{farmName}' ")
    vehicleNumbers = c.fetchall()
    for numbers in vehicleNumbers:
        countVehicles = numbers["COUNT(VehicleID)"]

    #Get total number of cattle for the vehicles
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    cattleNumbers = c.fetchall()
    for numbers in cattleNumbers:
        countCattle = numbers["COUNT(CattleID)"]


    return render_template('farm_stats.html', staffNumbers = countStaff, paddockNumbers = countPaddock, vehicleNumbers = countVehicles, farmName = farmName, cattleNumbers = countCattle)
#View paddocks based on farm name
@app.route("/farm/paddock/<farmName>", methods = ["POST", "GET"])
def paddock_farm(farmName):
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM paddock WHERE FarmName = '{farmName}'")
    posts = c.fetchall()
    return render_template('paddock.html', posts=posts, farmName = farmName )

#View staff based on farm name
@app.route("/farm/paddock/<farmName>", methods = ["POST", "GET"])
def staff_farm(farmName):
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM staff WHERE FarmName = '{farmName}'")
    posts = c.fetchall()
    return render_template('staff.html', posts=posts, farmName = farmName )

#View cattle based on farm name
@app.route("/farm/cattle/<farmName>", methods = ["POST", "GET"])
def cattle_farm(farmName):
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM cattle WHERE PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    posts = c.fetchall()
    return render_template('cattle.html', posts=posts, farmName = farmName )

#Paddock view
@app.route("/paddock")
def paddock():
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM paddock")
    posts = c.fetchall()
    return render_template('paddock.html', posts=posts)

#Bin view
@app.route("/feed_bins/<paddockName>", methods = ['GET','POST'])
def feed_bins(paddockName):
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM feed_bins WHERE PaddockName = '{paddockName}'")
    posts = c.fetchall()
    return render_template('bins.html', posts=posts, paddockName = paddockName)


#Cattle view
@app.route("/cattle")
def cattle():
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM cattle")
    posts = c.fetchall()
    return render_template('cattle.html', posts=posts)

#Cattle for specific paddock
@app.route("/cattle/<paddockName>", methods = ['GET', 'POST'])
def cattle_paddock(paddockName):
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM cattle\
        WHERE PaddockName = '{paddockName}'")
    posts = c.fetchall()

    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle\
        WHERE PaddockName = '{paddockName}'")
    posts_count = c.fetchall()
    for post in posts_count:
        cattleCount = post["COUNT(CattleID)"]
    return render_template('cattle.html', posts=posts, paddockName = paddockName, cattleCount = cattleCount)

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
        
        c = conn.cursor()

        query = f"insert into STAFF(FirstName, LastName, DateOfBirth, FarmName, StartDate, ManagerID, PrimaryContactNumber)\
         VALUES ('{form.firstName.data}','{form.lastName.data}','{str(form.dateOfBirth.data)}','{form.farmLoc.data}','{str(form.startDate.data)}','{str(form.managerID.data)}' ,'{str(form.contactNumber.data)}')"
        c.execute(query) #Execute the query
        conn.commit() #Commit the changes
        
        flash(f'Staff member created for {form.firstName.data}', 'success')
        return redirect(url_for('staff_home'))
    
    return render_template("staff_add.html", form = form, title = "Add staff")

#Add feed bin
@app.route("/bin_add/<paddockName>", methods = ['GET','POST'])
def bin_add(paddockName):   
    form = BinAddForm()
    if form.validate_on_submit():
       
        
        c = conn.cursor()

        query = f"insert into feed_bins(BinNumber, PaddockName, LastChecked, BinContains, BinLevel)\
         VALUES ('{form.binNumber.data}','{paddockName}','{str(form.lastChecked.data)}','{form.binContains.data}','{str(form.binLevel.data)}')"
        c.execute(query) 
        conn.commit() 
        
        flash(f'Bin {form.binNumber.data} created for {paddockName}', 'success')
        return redirect(url_for('paddock'))
        
    return render_template("bin_add.html", form = form, paddockName = paddockName)

#Add motorbike
@app.route("/motorbike_add", methods = ['GET', 'POST'])
def motorbike_add():
    form = MotorbikeAddForm()
    if form.validate_on_submit():
       
        #Add vehicle to vehicles table
        c = conn.cursor()
        query = f"INSERT INTO vehicles(Model, FarmName, PurchaseDate) \
        VALUES('{form.model.data}','{form.farmName.data}','{form.purchaseDate.data}')"
        c.execute(query)
        conn.commit()
        
        #Get the auto-incremented vehicle ID from vehicles table
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute("SELECT MAX(VehicleID), Model FROM vehicles;")
        posts = c.fetchall()
        for post in posts:
            max_ID = (post["MAX(VehicleID)"])

        #Add vehicle to motorbikes table 
        query = f"INSERT INTO motorbikes(VehicleID, EngineCC) \
        VALUES('{max_ID}','{form.engineCC.data}')"
        c.execute(query)
        conn.commit()


        #Add vehicle to vehicle_brands table 
        c = conn.cursor() 
        query = f"INSERT INTO vehicle_brands(VehicleID, Brand) \
        VALUES('{max_ID}','{form.brand.data}')"
        c.execute(query)
        conn.commit()

        flash(f"Motorbike added to {form.farmName.data}",  'success')

        return redirect(url_for('vehicles'))

    return render_template("motorbike_add.html", form = form, title = "Add motorbike")

#Add buggy
@app.route("/buggies_add", methods = ['GET', 'POST'])
def buggies_add():
    form = BuggiesAddForm()
    if form.validate_on_submit():
       
        #Add vehicle to vehicles table
        c = conn.cursor()
        query = f"INSERT INTO vehicles(Model, FarmName, PurchaseDate) \
        VALUES('{form.model.data}','{form.farmName.data}','{form.purchaseDate.data}')"
        c.execute(query)
        conn.commit()
        
        #Get the auto-incremented vehicle ID from vehicles table
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute("SELECT MAX(VehicleID), Model FROM vehicles;")
        posts = c.fetchall()
        for post in posts:
            max_ID = (post["MAX(VehicleID)"])

        #Add vehicle to buggies table 
        query = f"INSERT INTO buggies(VehicleID, NumberOfSeats) \
        VALUES('{max_ID}','{form.numberOfSeats.data}')"
        c.execute(query)
        conn.commit()


        #Add vehicle to vehicle_brands table 
        c = conn.cursor() 
        query = f"INSERT INTO vehicle_brands(VehicleID, Brand) \
        VALUES('{max_ID}','{form.brand.data}')"
        c.execute(query)
        conn.commit()

        flash(f"Buggy added to {form.farmName.data}",  'success')

        return redirect(url_for('vehicles'))

    return render_template("buggies_add.html", form = form)

#Add quadbike
@app.route("/quadbike_add", methods = ['GET', 'POST'])
def quadbike_add():
    form = QuadbikeAddForm()
    if form.validate_on_submit():
       
        #Add vehicle to vehicles table
        c = conn.cursor()
        query = f"INSERT INTO vehicles(Model, FarmName, PurchaseDate) \
        VALUES('{form.model.data}','{form.farmName.data}','{form.purchaseDate.data}')"
        c.execute(query)
        conn.commit()
        
        #Get the auto-incremented vehicle ID from vehicles table
        conn.row_factory = dict_factory
        c = conn.cursor()
        c.execute("SELECT MAX(VehicleID), Model FROM vehicles;")
        posts = c.fetchall()
        for post in posts:
            max_ID = (post["MAX(VehicleID)"])

        #Add vehicle to quadbikes table 
        query = f"INSERT INTO quadbikes(VehicleID, RollCage) \
        VALUES('{max_ID}','{form.rollCage.data}')"
        c.execute(query)
        conn.commit()


        #Add vehicle to vehicle_brands table 
        c = conn.cursor() 
        query = f"INSERT INTO vehicle_brands(VehicleID, Brand) \
        VALUES('{max_ID}','{form.brand.data}')"
        c.execute(query)
        conn.commit()

        flash(f"Quadbike added to {form.farmName.data}",  'success')

        return redirect(url_for('vehicles'))


    return render_template("quadbike_add.html", form = form)

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

#Delete staff
@app.route("/staff/delete/<int:staffID>", methods=['POST'])
def delete_staff(staffID):
    c = conn.cursor()
    current_id = staffID
    query = f"DELETE FROM staff WHERE StaffID = {current_id}"
    c.execute(query)
    conn.commit()
    return redirect(url_for('staff_home'))

#Delete cattle
@app.route("/cattle/delete/<int:cattleID>", methods=['POST'])
def delete_cattle(cattleID):
    c = conn.cursor()
    current_id = cattleID
    query = f"DELETE FROM cattle WHERE CattleID = '{current_id}'"
    c.execute(query)
    conn.commit()
    return redirect(url_for('cattle'))


#Delete paddock
@app.route("/paddock/delete/<paddockName>", methods=['POST'])
def delete_paddock(paddockName):
    c = conn.cursor()
    current_paddock = paddockName
    query = f"DELETE FROM paddock WHERE PaddockName = '{current_paddock}'"
    c.execute(query)
    conn.commit()
    return redirect(url_for('paddock'))

#Delete bin
@app.route("/bin/delete/<paddockName>/<binNumber>", methods=['POST'])
def delete_bin(paddockName, binNumber):
    c = conn.cursor()
    query = f"DELETE FROM feed_bins WHERE PaddockName = '{paddockName}' AND BinNumber = '{binNumber}'"
    c.execute(query)
    conn.commit()
    return redirect(url_for('feed_bins', paddockName = paddockName))


#Delete vehicles 
@app.route("/vehicles/delete<vehicleID>", methods=['POST'])
def delete_vehicle(vehicleID): 
     
    #Delete from vehicles  
    #Deletes on casecade to also remove from vehicle_brands and specilisation table
    c = conn.cursor()
    query = f"DELETE FROM vehicles WHERE VehicleID = '{vehicleID}'"
    c.execute(query)
    conn.commit()
    return redirect(url_for('vehicles'))

#Update farm
@app.route("/farm/update/<updateName>/<updateAddress>",methods = ['GET','POST'])
def update_farm(updateName ,updateAddress):
    form = FarmAddForm()
    if form.validate_on_submit():
            
            c = conn.cursor()
            query = f"UPDATE farm\
                     SET FarmName = '{form.name.data}', Address = '{form.address.data}'\
                     WHERE FarmName = '{updateName}'"
            c.execute(query)
            conn.commit()
            
            flash(f'Farm {updateName} updated', 'success')
            return redirect(url_for('farm'))
    return render_template("update_farm.html", updateName = updateName , updateAddress = updateAddress, form = form)
    
#Update paddock
@app.route("/paddock/update/<paddockName>/<size>/<grass>/<farm>",methods = ['GET','POST'])
def update_paddock(paddockName ,size, grass, farm):
    form = PaddockAddFrom()
    if form.validate_on_submit():
            
            c = conn.cursor()
            query = f"UPDATE paddock\
                     SET PaddockName = '{form.paddockName.data}', Size = '{form.size.data}'\
                    , GrassCondition = '{form.grassCondition.data}', FarmName = '{form.farmName.data}'\
                     WHERE PaddockName = '{paddockName}'"
            c.execute(query)
            conn.commit()
            
            flash(f'Paddock {paddockName} updated', 'success')
            return redirect(url_for('paddock'))
    return render_template("update_paddock.html",paddockName = paddockName, size = size, grass = grass, farm = farm , form = form) 

#Update feed bins    
@app.route("/paddock/<paddockName>/bins/<binNumber>/<lastChecked>/<binContains>/<binLevel>",methods = ['GET','POST'])
def update_bin(paddockName, binNumber, lastChecked, binContains, binLevel):
    form = BinUpdateForm()
    if form.validate_on_submit():
            
            c = conn.cursor()
            query = f"UPDATE feed_bins\
                     SET PaddockName = '{form.paddockName.data}', BinNumber = '{form.binNumber.data}'\
                    , LastChecked = '{form.lastChecked.data}', BinContains = '{form.binContains.data}', BinLevel = '{form.binLevel.data}'\
                     WHERE PaddockName = '{paddockName}' AND BinNumber = '{binNumber}'"
            c.execute(query)
            conn.commit()
            
            flash(f'Bin{binNumber} in {paddockName} updated', 'success')
            return redirect(url_for('paddock'))
    return render_template("update_bins.html",paddockName = paddockName, binNumber = binNumber, lastChecked = lastChecked, binContains = binContains, binLevel = binLevel ,form = form)


#Update cattle
@app.route("/farm/update/<ID>/<sex>/<breed>/<dob>/<weight>/<paddockName>/<dateMoved>",methods = ['GET','POST'])
def update_cattle(ID, sex, breed, dob, weight, paddockName, dateMoved):
    form = CattleUpdateForm()
    if form.validate_on_submit():
            
            c = conn.cursor()
            query = f"UPDATE cattle\
                     SET CattleID = '{form.ID.data}', Sex = '{form.sex.data}', Breed = '{form.breed.data}', DateOfBirth = '{form.dateOfBirth.data}',\
                     Weight = '{form.weight.data}', PaddockName = '{form.paddockName.data}', DateMoved = '{form.dateMoved.data}'\
                     WHERE cattleID = '{ID}'"
            c.execute(query)
            conn.commit()
            
            flash(f'Cattle {ID} updated', 'success')
            return redirect(url_for('cattle'))
    return render_template("update_cattle.html",ID = ID, sex = sex, breed = breed, dob = dob, weight = weight, paddockName = paddockName, dateMoved = dateMoved, form = form)      


#Update staff
@app.route("/staff/update/<staffID>/<first>/<last>/<dob>/<farm>/<startDate>/<number>/<managerID>",methods = ['GET','POST'])
def update_staff(staffID, first, last,  dob, farm, startDate, number, managerID):
    form = StaffAddFrom()
    if form.validate_on_submit():
            
            c = conn.cursor()
            query = f"UPDATE staff\
                     SET StaffID = '{form.staffID.data}', FirstName = '{form.firstName.data}', LastName = '{form.lastName.data}', DateOfBirth = '{form.dateOfBirth.data}', FarmName = '{form.farmLoc.data}', StartDate = '{form.startDate.data}', ManagerID = '{form.managerID.data}', PrimaryContactNumber = '{form.contactNumber.data}' \
                     WHERE StaffID = '{staffID}'"
            c.execute(query)
            conn.commit()
            
            flash(f'Staff member {staffID} updated', 'success')
            return redirect(url_for('staff_home'))
    return render_template("update_staff.html",staffID = staffID, first = first, last = last,  dob = dob, farm = farm, startDate = startDate, number = number, managerID = managerID,  form = form)

#Update motorbike
@app.route("/vehicles/motorbikes/<vehicleID>/<model>/<farm>/<date>/<brand>/<engine>",methods = ['GET','POST'])
def update_motorbike(vehicleID, model, farm, date, brand, engine):
    form = MotorbikeUpdateForm()
    if form.validate_on_submit():  
            #update vehicles table
            c = conn.cursor()
            query = f"UPDATE vehicles\
                     SET VehicleID = '{form.vehicleID.data}', Model = '{form.model.data}', FarmName = '{form.farmName.data}', PurchaseDate = '{form.purchaseDate.data}' \
                     WHERE VehicleID = '{vehicleID}'"
            c.execute(query)
            conn.commit()
            
            #update brands table
            #use new vehicle ID as vehicles table set to cascade update
            c = conn.cursor()
            query = f"UPDATE vehicle_brands\
                     SET Brand = '{form.brand.data}'\
                     WHERE VehicleID = '{form.vehicleID.data}'"
            c.execute(query)
            conn.commit()

            #update motorbikes table
            #use new vehicle ID as vehicles table set to cascade update
            c = conn.cursor()
            query = f"UPDATE motorbikes\
                     SET EngineCC = '{form.engineCC.data}'\
                     WHERE VehicleID = '{form.vehicleID.data}'"
            c.execute(query)
            conn.commit()
            
            
            flash(f'Motorbike {vehicleID} updated', 'success')
            return redirect(url_for('vehicles'))
    return render_template("update_motorbike.html",vehicleID = vehicleID, model = model, farm = farm, date = date, brand = brand, engine = engine,  form = form)

#Update quadbike
@app.route("/vehicles/quadbike/<vehicleID>/<model>/<farm>/<date>/<brand>/<rollCage>",methods = ['GET','POST'])
def update_quadbike(vehicleID, model, farm, date, brand, rollCage):
    form = QuadbikeUpdateForm()
    if form.validate_on_submit():  
            #update vehicles table
            c = conn.cursor()
            query = f"UPDATE vehicles\
                     SET VehicleID = '{form.vehicleID.data}', Model = '{form.model.data}', FarmName = '{form.farmName.data}', PurchaseDate = '{form.purchaseDate.data}' \
                     WHERE VehicleID = '{vehicleID}'"
            c.execute(query)
            conn.commit()
            
            #update brands table
            #use new vehicle ID as vehicles table set to cascade update
            c = conn.cursor()
            query = f"UPDATE vehicle_brands\
                     SET Brand = '{form.brand.data}'\
                     WHERE VehicleID = '{form.vehicleID.data}'"
            c.execute(query)
            conn.commit()

            #update motorbikes table
            #use new vehicle ID as vehicles table set to cascade update
            c = conn.cursor()
            query = f"UPDATE quadbikes\
                     SET RollCage = '{form.rollCage.data}'\
                     WHERE VehicleID = '{form.vehicleID.data}'"
            c.execute(query)
            conn.commit()
            
            
            flash(f'Quadbike {vehicleID} updated', 'success')
            return redirect(url_for('vehicles'))
    return render_template("update_quadbike.html",vehicleID = vehicleID, model = model, farm = farm, date = date, brand = brand, rollCage = rollCage,  form = form)


#Update buggy
@app.route("/vehicles/buggy/<vehicleID>/<model>/<farm>/<date>/<brand>/<numberOfSeats>",methods = ['GET','POST'])
def update_buggy(vehicleID, model, farm, date, brand, numberOfSeats):
    form = BuggiesUpdateForm()
    if form.validate_on_submit():  
            #update vehicles table
            c = conn.cursor()
            query = f"UPDATE vehicles\
                     SET VehicleID = '{form.vehicleID.data}', Model = '{form.model.data}', FarmName = '{form.farmName.data}', PurchaseDate = '{form.purchaseDate.data}' \
                     WHERE VehicleID = '{vehicleID}'"
            c.execute(query)
            conn.commit()
            
            #update brands table
            #use new vehicle ID as vehicles table set to cascade update
            c = conn.cursor()
            query = f"UPDATE vehicle_brands\
                     SET Brand = '{form.brand.data}'\
                     WHERE VehicleID = '{form.vehicleID.data}'"
            c.execute(query)
            conn.commit()

            #update motorbikes table
            #use new vehicle ID as vehicles table set to cascade update
            c = conn.cursor()
            query = f"UPDATE buggies\
                     SET NumberOfSeats = '{form.numberOfSeats.data}'\
                     WHERE VehicleID = '{form.vehicleID.data}'"
            c.execute(query)
            conn.commit()
            
            
            flash(f'Buggy {vehicleID} updated', 'success')
            return redirect(url_for('vehicles'))
    return render_template("update_buggy.html",vehicleID = vehicleID, model = model, farm = farm, date = date, brand = brand, numberOfSeats = numberOfSeats,  form = form)    


if __name__ == "__main__":
    app.run(debug = True)
    
