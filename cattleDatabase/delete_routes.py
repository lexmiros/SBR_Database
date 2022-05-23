
from cattleDatabase import  app, url_for, redirect, flash
import pymysql

host_db='localhost'
user_db='adminflask'
password_db ='adminflask'
database_db= 'project_db_3'
charset_db= 'utf8mb4'
cursorclass_db = pymysql.cursors.DictCursor


#Delete Farm
@app.route("/farm/delete/<farmName>", methods=['POST'])
def delete_farm(farmName):
    conn = pymysql.connect(host=host_db, user=user_db, password= password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    c = conn.cursor()
    current_farm= farmName
    query = f"DELETE FROM farm WHERE FarmName = '{current_farm}'"
    c.execute(query)
    conn.commit()
    c.close()
    conn.close()


    flash(f'Farm {farmName} and all associated entites deleted', 'success')
    
    return redirect(url_for('farm'))

#Delete staff
@app.route("/staff/delete/<int:staffID>", methods=['POST'])
def delete_staff(staffID):
    try:
        conn = pymysql.connect(host=host_db, user=user_db, password= password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
        c = conn.cursor()
        current_id = staffID
        query = f"DELETE FROM staff WHERE StaffID = {current_id}"
        c.execute(query)
        conn.commit()
        c.close()
        conn.close()

        flash(f'Staff {staffID}  deleted', 'success')
        return redirect(url_for('staff_home'))
    except:
        flash(f'Deletion FAILED : Please ensure all staff ID : {current_id } manages change their manager ID before deleting', 'danger')
        return redirect(url_for('staff_home'))
#Delete cattle
@app.route("/cattle/delete/<int:cattleID>", methods=['POST'])
def delete_cattle(cattleID):
    conn = pymysql.connect(host=host_db, user=user_db, password= password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    c = conn.cursor()
    current_id = cattleID
    query = f"DELETE FROM cattle WHERE CattleID = '{current_id}'"
    c.execute(query)
    conn.commit()
    c.close()
    conn.close()
    flash(f'Cow {cattleID}  deleted', 'success')
    return redirect(url_for('cattle'))


#Delete paddock
@app.route("/paddock/delete/<paddockName>", methods=['POST'])
def delete_paddock(paddockName):
    conn = pymysql.connect(host=host_db, user=user_db, password= password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    c = conn.cursor()
    current_paddock = paddockName
    query = f"DELETE FROM paddock WHERE PaddockName = '{current_paddock}'"
    c.execute(query)
    conn.commit()
    c.close()
    conn.close()
    flash(f'Paddock {paddockName}  deleted', 'success')
    return redirect(url_for('paddock'))

#Delete bin
@app.route("/bin/delete/<paddockName>/<binNumber>", methods=['POST'])
def delete_bin(paddockName, binNumber):
    conn = pymysql.connect(host=host_db, user=user_db, password= password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    c = conn.cursor()
    query = f"DELETE FROM feed_bins WHERE PaddockName = '{paddockName}' AND BinNumber = '{binNumber}'"
    c.execute(query)
    conn.commit()
    c.close()
    conn.close()
    flash(f'Bin {binNumber} at paddock {paddockName}  deleted', 'success')
    return redirect(url_for('feed_bins', paddockName = paddockName))


#Delete vehicles 
@app.route("/vehicles/delete<vehicleID>", methods=['POST'])
def delete_vehicle(vehicleID): 
     
    #Delete from vehicles  
    #Deletes on casecade to also remove from vehicle_brands and specilisation table
    conn = pymysql.connect(host=host_db, user=user_db, password= password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    c = conn.cursor()
    query = f"DELETE FROM vehicles WHERE VehicleID = '{vehicleID}'"
    c.execute(query)
    conn.commit()
    c.close()
    conn.close()

    flash(f'Vehicle {vehicleID}  deleted', 'success')
    return redirect(url_for('vehicles'))
