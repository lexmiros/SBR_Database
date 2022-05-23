from cattleDatabase.forms import FarmAddForm, PaddockAddFrom,BinUpdateForm, CattleUpdateForm, StaffUpdateForm, MotorbikeUpdateForm, QuadbikeUpdateForm, BuggiesUpdateForm, StaffUpdateManagerForm
from cattleDatabase import pymysql, app, conn, render_template, url_for, redirect, flash

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
        try:
                c = conn.cursor()
                query = f"UPDATE paddock\
                        SET PaddockName = '{form.paddockName.data}', Size = '{form.size.data}'\
                        , GrassCondition = '{form.grassCondition.data}', FarmName = '{form.farmName.data}'\
                        WHERE PaddockName = '{paddockName}'"
                c.execute(query)
                conn.commit()
                flash(f'Paddock {paddockName} updated', 'success')
                return redirect(url_for('paddock'))
        except pymysql.err.IntegrityError:
            flash(f'Please ensure the farm name exists', 'danger')

    return render_template("update_paddock.html",paddockName = paddockName, size = size, grass = grass, farm = farm , form = form) 

#Update feed bins    
@app.route("/paddock/<paddockName>/bins/<binNumber>/<lastChecked>/<binContains>/<binLevel>",methods = ['GET','POST'])
def update_bin(paddockName, binNumber, lastChecked, binContains, binLevel):
    form = BinUpdateForm()
    if form.validate_on_submit():
        if form.binLevel.data > 1:
                flash(f'Bin level cannot exceed 1', 'danger')
        else:
                try:
                        c = conn.cursor()
                        query = f"UPDATE feed_bins\
                        SET PaddockName = '{form.paddockName.data}', BinNumber = '{form.binNumber.data}'\
                        , LastChecked = '{form.lastChecked.data}', BinContains = '{form.binContains.data}', BinLevel = '{form.binLevel.data}'\
                        WHERE PaddockName = '{paddockName}' AND BinNumber = '{binNumber}'"
                        c.execute(query)
                        conn.commit()

                        flash(f'Bin{binNumber} in {paddockName} updated', 'success')
                        return redirect(url_for('feed_bins', paddockName = paddockName))
                except pymysql.err.IntegrityError:
                        flash(f'Please ensure the paddock name exists', 'danger')

    return render_template("update_bins.html",paddockName = paddockName, binNumber = binNumber, lastChecked = lastChecked, binContains = binContains, binLevel = binLevel ,form = form)


#Update cattle
@app.route("/farm/update/<ID>/<sex>/<breed>/<dob>/<weight>/<paddockName>/<dateMoved>",methods = ['GET','POST'])
def update_cattle(ID, sex, breed, dob, weight, paddockName, dateMoved):
    form = CattleUpdateForm()
    if form.validate_on_submit():
        try:
                c = conn.cursor()
                query = f"UPDATE cattle\
                        SET CattleID = '{form.ID.data}', Sex = '{form.sex.data}', Breed = '{form.breed.data}', DateOfBirth = '{form.dateOfBirth.data}',\
                        Weight = '{form.weight.data}', PaddockName = '{form.paddockName.data}', DateMoved = '{form.dateMoved.data}'\
                        WHERE cattleID = '{ID}'"
                c.execute(query)
                conn.commit()
                
                flash(f'Cattle {ID} updated', 'success')
                return redirect(url_for('cattle'))
        except pymysql.err.IntegrityError:
            flash(f'Please ensure the paddock name exists and the new ID is not taken', 'danger')
             
    return render_template("update_cattle.html",ID = ID, sex = sex, breed = breed, dob = dob, weight = weight, paddockName = paddockName, dateMoved = dateMoved, form = form)      


#Update staff
@app.route("/staff/update/<staffID>/<first>/<last>/<dob>/<farm>/<startDate>/<number>",methods = ['GET','POST'])
def update_staff(staffID, first, last,  dob, farm, startDate, number):
    form = StaffUpdateForm()
    if form.validate_on_submit():
        
                try:
                        c = conn.cursor()
                        query = f"UPDATE staff\
                                SET StaffID = '{form.staffID.data}', FirstName = '{form.firstName.data}', LastName = '{form.lastName.data}', DateOfBirth = '{form.dateOfBirth.data}', FarmName = '{form.farmLoc.data}', StartDate = '{form.startDate.data}', PrimaryContactNumber = '{form.contactNumber.data}' \
                                WHERE StaffID = '{staffID}'"
                        c.execute(query)
                        conn.commit()
                        
                        flash(f'Staff member {staffID} updated', 'success')
                        return redirect(url_for('staff_home'))
                except pymysql.err.IntegrityError:
                        flash(f'Please ensure the new staff IDs are not in use, and if this staff member is a manager, other staff are assigned new managers before updating the staff ID', 'danger')
          

    return render_template("update_staff.html",staffID = staffID, first = first, last = last,  dob = dob, farm = farm, startDate = startDate, number = number,  form = form)

#Update staff manager
@app.route("/staff/update/<staffID>/<managerID>",methods = ['GET','POST'])
def update_staff_manager(staffID, managerID):
        form = StaffUpdateManagerForm()
        if form.validate_on_submit():

                try:
                        c = conn.cursor()
                        query = f"UPDATE staff SET ManagerID = '{form.managerID.data}' WHERE StaffID = '{staffID}'"
                        c.execute(query)
                        conn.commit()

                        flash(f'Staff member {staffID} updated', 'success')
                        return redirect(url_for('staff_home'))
                except pymysql.err.IntegrityError:
                        flash(f'Please ensure the farm name and manager ID exists and the new staff ID is not taken', 'danger')
        return render_template("update_staff_manager.html",staffID = staffID, managerID = managerID,  form = form)

#Update motorbike
@app.route("/vehicles/motorbikes/<vehicleID>/<model>/<farm>/<date>/<brand>/<engine>",methods = ['GET','POST'])
def update_motorbike(vehicleID, model, farm, date, brand, engine):
    form = MotorbikeUpdateForm()
    if form.validate_on_submit():  
        try:
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
        except pymysql.err.IntegrityError:
            flash(f'Please ensure the farm name exists and the new ID is not taken', 'danger')

    return render_template("update_motorbike.html",vehicleID = vehicleID, model = model, farm = farm, date = date, brand = brand, engine = engine,  form = form)

#Update quadbike
@app.route("/vehicles/quadbike/<vehicleID>/<model>/<farm>/<date>/<brand>/<rollCage>",methods = ['GET','POST'])
def update_quadbike(vehicleID, model, farm, date, brand, rollCage):
    form = QuadbikeUpdateForm()
    if form.validate_on_submit():  
        try:
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
        except pymysql.err.IntegrityError:
            flash(f'Please ensure the farm name exists and the new ID is not taken', 'danger')
    return render_template("update_quadbike.html",vehicleID = vehicleID, model = model, farm = farm, date = date, brand = brand, rollCage = rollCage,  form = form)


#Update buggy
@app.route("/vehicles/buggy/<vehicleID>/<model>/<farm>/<date>/<brand>/<numberOfSeats>",methods = ['GET','POST'])
def update_buggy(vehicleID, model, farm, date, brand, numberOfSeats):
    form = BuggiesUpdateForm()
    if form.validate_on_submit():  
        try:
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
        except pymysql.err.IntegrityError:
            flash(f'Please ensure the farm name exists and the new ID is not taken', 'danger')
    return render_template("update_buggy.html",vehicleID = vehicleID, model = model, farm = farm, date = date, brand = brand, numberOfSeats = numberOfSeats,  form = form)    
