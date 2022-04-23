from cattleDatabase.forms import BinAddForm, BuggiesAddForm, CattleAddForm, FarmAddForm, MotorbikeAddForm, PaddockAddFrom, QuadbikeAddForm, StaffAddForm
from cattleDatabase import *



#Add farm
@app.route("/farm_add",methods = ['GET','POST'])
def farm_add():
        form = FarmAddForm()
        if form.validate_on_submit():
            try:
                c = conn.cursor()
                query = f"INSERT INTO FARM(FarmName, Address)\
                        VALUES('{form.name.data}','{form.address.data}')"
                c.execute(query)
                conn.commit()
                
                flash(f'Farm {form.name.data} created', 'success')
                return redirect(url_for('farm'))
            except pymysql.err.IntegrityError:
                flash(f'Please ensure the farm name does not already exist', 'danger')

        return render_template("farm_add.html", form = form,title = "Add farms")


#Add paddock
@app.route("/paddock_add",methods = ['GET','POST'])
def paddock_add():
    form = PaddockAddFrom()
    if form.validate_on_submit():
        try:
            c = conn.cursor()
            query = f"INSERT INTO PADDOCK(PaddockName, Size, GrassCondition, FarmName)\
                    VALUES('{form.paddockName.data}','{str(form.size.data)}','{form.grassCondition.data}','{form.farmName.data}')"
            c.execute(query)
            conn.commit()
            flash(f'Paddock {form.paddockName.data} created', 'success')
            return redirect(url_for('paddock'))
        
        except pymysql.err.IntegrityError:
            flash(f'Please ensure the paddock name is not taken and enter an existing farm name', 'danger')


    return render_template("paddock_add.html", form = form, title = "Add paddocks")


#Add cattle
@app.route('/cattle_add',methods = ['GET','POST'])
def cattle_add():
    form = CattleAddForm()
    if form.validate_on_submit():
        try:
            c = conn.cursor()
            query = f"INSERT INTO CATTLE (Sex, Breed, DateOfBirth, Weight, PaddockName, DateMoved)\
                    VALUES('{form.sex.data}','{form.breed.data}','{form.dateOfBirth.data}','{str(form.weight.data)}','{str(form.paddockName.data)}','{form.dateMoved.data}')"
            c.execute(query)
            conn.commit()
            
            flash(f'Cattle added to {form.paddockName.data}', 'success')
            return redirect(url_for('cattle'))
        
        except pymysql.err.IntegrityError:
            flash(f'Farm name  {form.paddockName.data} is NOT valid. Please enter an existing paddock name', 'danger')
    
    return render_template("cattle_add.html", form = form, title = "Add cattle")


#Add staff
@app.route("/staff_add", methods = ['GET','POST'])
def staff_add():   
    form = StaffAddForm()
    if form.validate_on_submit():
        #Create new staf member if a manager ID has been given from the GUi
        if form.managerID.data:
            try:
                c = conn.cursor()
                query = f"insert into STAFF(FirstName, LastName, DateOfBirth, FarmName, StartDate, ManagerID, PrimaryContactNumber)\
                VALUES ('{form.firstName.data}','{form.lastName.data}','{str(form.dateOfBirth.data)}','{form.farmLoc.data}','{str(form.startDate.data)}','{str(form.managerID.data)}' ,'{str(form.contactNumber.data)}')"
                c.execute(query) #Execute the query
                conn.commit() #Commit the changes
            
                flash(f'Staff member created for {form.firstName.data}', 'success')
                return redirect(url_for('staff_home'))

            except pymysql.err.IntegrityError:
                flash(f'Please ensure the farm name exists', 'danger')
        #Create staff member if no manager ID has been given. 
        else:
            try:
                c = conn.cursor()
                query = f"insert into STAFF(FirstName, LastName, DateOfBirth, FarmName, StartDate, PrimaryContactNumber)\
                VALUES ('{form.firstName.data}','{form.lastName.data}','{str(form.dateOfBirth.data)}','{form.farmLoc.data}','{str(form.startDate.data)}' ,'{str(form.contactNumber.data)}')"
                c.execute(query) #Execute the query
                conn.commit() #Commit the changes
            
                flash(f'Staff member created for {form.firstName.data}', 'success')
                return redirect(url_for('staff_home'))

            except pymysql.err.IntegrityError:
                flash(f'Please ensure the farm name exists', 'danger')

    return render_template("staff_add.html", form = form, title = "Add staff")

#Add feed bin
@app.route("/bin_add/<paddockName>", methods = ['GET','POST'])
def bin_add(paddockName):   
    form = BinAddForm()
    if form.validate_on_submit():
        if form.binLevel.data > 1:
            flash(f'Bin level cannot exceed 1', 'danger')
        else:
            try:
                c = conn.cursor()
                query = f"insert into feed_bins(BinNumber, PaddockName, LastChecked, BinContains, BinLevel)\
                VALUES ('{form.binNumber.data}','{paddockName}','{str(form.lastChecked.data)}','{form.binContains.data}','{str(form.binLevel.data)}')"
                c.execute(query) 
                conn.commit() 
                
                flash(f'Bin {form.binNumber.data} created for {paddockName}', 'success')
                return redirect(url_for('feed_bins', paddockName = paddockName))
            except pymysql.err.IntegrityError:
                flash(f'Please ensure the paddock exists', 'danger')    
        
    return render_template("bin_add.html", form = form, paddockName = paddockName)

#Add motorbike
@app.route("/motorbike_add", methods = ['GET', 'POST'])
def motorbike_add():
    form = MotorbikeAddForm()
    if form.validate_on_submit():
        try:
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
        except pymysql.err.IntegrityError:
            flash(f'Please ensure the farm name exists', 'danger')

    return render_template("motorbike_add.html", form = form, title = "Add motorbike")

#Add buggy
@app.route("/buggies_add", methods = ['GET', 'POST'])
def buggies_add():
    form = BuggiesAddForm()
    if form.validate_on_submit():
        try:
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
        except pymysql.err.IntegrityError:
            flash(f'Please ensure the farm name exists', 'danger')

    return render_template("buggies_add.html", form = form)

#Add quadbike
@app.route("/quadbike_add", methods = ['GET', 'POST'])
def quadbike_add():
    form = QuadbikeAddForm()
    if form.validate_on_submit():
        try:
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
        
        except pymysql.err.IntegrityError:
            flash(f'Please ensure the farm name exists', 'danger')    


    return render_template("quadbike_add.html", form = form)
