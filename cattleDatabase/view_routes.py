from cattleDatabase import app, dict_factory, render_template, dict_factory
import pymysql

host_db='localhost'
user_db='adminflask'
password_db ='adminflask'
database_db= 'project_db_3'
charset_db= 'utf8mb4'
cursorclass_db = pymysql.cursors.DictCursor

@app.route("/")
def home():
    return render_template("home.html", title = "Home Page")

@app.route("/about")
def about():
    return render_template("about.html", title = "About")

@app.route("/report")
def report():
    return render_template("report.html", title = "Report")
#Farm view
@app.route("/farm")
def farm():
    #Find all farms
    conn = pymysql.connect(host=host_db, user=user_db, password= password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM farm")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    #Find total number of farms
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(FarmName) FROM farm")
    names = c.fetchall()
    for name in names:
        countName = name["COUNT(FarmName)"]
    conn.commit()
    c.close()
    conn.close()
    
    return render_template('farm.html', posts=posts, countName = countName)
    
#staff homepage
@app.route("/staff_home")
def staff_home():
    
    #Select all staff
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM staff;")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    

    #Find total number of staff
    conn = pymysql.connect(host=host_db, user=user_db, password= password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(StaffID) FROM staff;")
    totalCount = c.fetchall()
    for count in totalCount:
        staffCount = count["COUNT(StaffID)"]
    conn.commit()
    c.close()
    conn.close()
    
    return render_template('staff.html', posts=posts, staffCount = staffCount)


#Paddock view
@app.route("/paddock")
def paddock():
    #find all paddocks
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM paddock")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    #Find total paddocks
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(PaddockName) FROM paddock")
    paddocks = c.fetchall()
    for paddock in paddocks:
       countName =  paddock["COUNT(PaddockName)"]
    conn.commit()
    c.close()
    conn.close()

    #Find average paddock size
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT ROUND(AVG(Size),2) FROM paddock")
    sizes = c.fetchall()
    for size in sizes:
        avgSize = size["ROUND(AVG(Size),2)"]
    conn.commit()
    c.close()
    conn.close()

    #Find all paddocks with grass conditon = green
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(PaddockName) FROM paddock WHERE GrassCondition = 'Green'")
    conditions = c.fetchall()
    for condition in conditions:
        green = condition["COUNT(PaddockName)"]
    conn.commit()
    c.close()
    conn.close()

    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(PaddockName) FROM paddock WHERE GrassCondition = 'Dry'")
    conditions = c.fetchall()
    for condition in conditions:
        dry = condition["COUNT(PaddockName)"]
    conn.commit()
    c.close()
    conn.close()

    return render_template('paddock.html', posts=posts, countName = countName, avgSize = avgSize, green = green, dry = dry)


#Bin view
@app.route("/feed_bins/<paddockName>", methods = ['GET','POST'])
def feed_bins(paddockName):
    #Find all bins
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM feed_bins WHERE PaddockName = '{paddockName}'")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    #Find count of bins
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(BinNumber) FROM feed_bins WHERE PaddockName = '{paddockName}'")
    totalBins = c.fetchall()
    for bin in totalBins:
        countBins = bin["COUNT(BinNumber)"]
    conn.commit()
    c.close()
    conn.close()

    #Find average bin level
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT ROUND(AVG(BinLevel),2) FROM feed_bins WHERE PaddockName = '{paddockName}'")
    totalLevels = c.fetchall()
    for bin in totalLevels:
        avgLevel = bin["ROUND(AVG(BinLevel),2)"]
    conn.commit()
    c.close()
    conn.close()

    #Find count of bins containing wheat
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(BinNumber) FROM feed_bins WHERE PaddockName = '{paddockName}' AND BinContains = 'Wheat'")
    totalBins = c.fetchall()
    for bin in totalBins:
        wheatBins = bin["COUNT(BinNumber)"]
    conn.commit()
    c.close()
    conn.close()

    #Find count of bins containing sorghum
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(BinNumber) FROM feed_bins WHERE PaddockName = '{paddockName}' AND BinContains = 'Sorghum'")
    totalBins = c.fetchall()
    for bin in totalBins:
        sorghumBins = bin["COUNT(BinNumber)"]
    conn.commit()
    c.close()
    conn.close()

    #Find count of bins containing salt lick
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(BinNumber) FROM feed_bins WHERE PaddockName = '{paddockName}' AND BinContains = 'Salt Lick'")
    totalBins = c.fetchall()
    for bin in totalBins:
        saltBins = bin["COUNT(BinNumber)"]
    conn.commit()
    c.close()
    conn.close()

    return render_template('bins.html', posts=posts, paddockName = paddockName, countBins = countBins, avgLevel = avgLevel, wheatBins = wheatBins, sorghumBins = sorghumBins, saltBins = saltBins )


#Cattle view
@app.route("/cattle")
def cattle():
    #Select and return all cattle
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM cattle")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    #Find the number of cattle
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle")
    totalCattle = c.fetchall()
    for total in totalCattle:
        count = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()
    
    #Find the average weight
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT ROUND(AVG(Weight),2) FROM cattle")
    totalWeight = c.fetchall()
    for total in totalWeight:
        avgWeight = total["ROUND(AVG(Weight),2)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total males
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Male'")
    totalMale = c.fetchall()
    for total in totalMale:
        countMale = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total females
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Female'")
    totalFemale = c.fetchall()
    for total in totalFemale:
        countFemale = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total belmont reds
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Belmont Red'")
    totalBelmont= c.fetchall()
    for total in totalBelmont:
        countBelmont = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total angus
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Angus'")
    totalAngus= c.fetchall()
    for total in totalAngus:
        countAngus = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total cross
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Cross'")
    totalCross= c.fetchall()
    for total in totalCross:
        countCross = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find average weight for males
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT ROUND(AVG(Weight),2) FROM cattle WHERE Sex = 'Male';")
    totalMale = c.fetchall()
    for total in totalMale:
        avgMale = total["ROUND(AVG(Weight),2)"]
    conn.commit()
    c.close()
    conn.close()
    
    #Find average weight for females
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT ROUND(AVG(Weight),2) FROM cattle WHERE Sex = 'Female';")
    totalFemale = c.fetchall()
    for total in totalFemale:
        avgFemale = total["ROUND(AVG(Weight),2)"]
    conn.commit()
    c.close()
    conn.close()


    return render_template('cattle.html', posts=posts, count = count, avgWeight = avgWeight, countMale = countMale, countFemale = countFemale, countBelmont = countBelmont, countAngus = countAngus, countCross = countCross, avgMale = avgMale, avgFemale = avgFemale)


#Cattle for specific paddock
@app.route("/cattle/<paddockName>", methods = ['GET', 'POST'])
def cattle_paddock(paddockName):
    
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM cattle\
        WHERE PaddockName = '{paddockName}'")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle\
        WHERE PaddockName = '{paddockName}'")
    posts_count = c.fetchall()
    for post in posts_count:
        cattleCount = post["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find the average weight
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT ROUND(AVG(Weight),2) FROM cattle WHERE PaddockName = '{paddockName}'")
    totalWeight = c.fetchall()
    for total in totalWeight:
        avgWeight = total["ROUND(AVG(Weight),2)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total males
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Male' AND PaddockName = '{paddockName}'")
    totalMale = c.fetchall()
    for total in totalMale:
        countMale = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total females
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Female' AND PaddockName = '{paddockName}'")
    totalFemale = c.fetchall()
    for total in totalFemale:
        countFemale = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total belmont reds
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Belmont Red'  AND PaddockName = '{paddockName}'")
    totalBelmont= c.fetchall()
    for total in totalBelmont:
        countBelmont = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total angus
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Angus' AND PaddockName = '{paddockName}'")
    totalAngus= c.fetchall()
    for total in totalAngus:
        countAngus = total["COUNT(CattleID)"]

    #Find total cross
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Cross' AND PaddockName = '{paddockName}'")
    totalCross= c.fetchall()
    for total in totalCross:
        countCross = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()
    
    #Find average weight for males
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT ROUND(AVG(Weight),2) FROM cattle WHERE Sex = 'Male' AND PaddockName = '{paddockName}';")
    totalMale = c.fetchall()
    for total in totalMale:
        avgMale = total["ROUND(AVG(Weight),2)"]
    conn.commit()
    c.close()
    conn.close()
    
    #Find average weight for females
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT ROUND(AVG(Weight),2) FROM cattle WHERE Sex = 'Female' AND PaddockName = '{paddockName}';")
    totalFemale = c.fetchall()
    for total in totalFemale:
        avgFemale = total["ROUND(AVG(Weight),2)"]
    conn.commit()
    c.close()
    conn.close()



    return render_template('cattle.html', posts=posts, paddockName = paddockName, cattleCount = cattleCount, count = cattleCount, avgWeight = avgWeight, countMale = countMale, countFemale = countFemale, countBelmont = countBelmont, countAngus = countAngus, countCross = countCross, avgMale = avgMale, avgFemale = avgFemale)

#Vehicle pages
@app.route("/vehicles")
def vehicles():
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM vehicles INNER JOIN vehicle_brands ON vehicles.VehicleID=vehicle_brands.VehicleID LEFT JOIN motorbikes ON vehicles.VehicleID=motorbikes.VehicleID LEFT JOIN quadbikes ON vehicles.VehicleID=quadbikes.VehicleID LEFT JOIN buggies ON vehicles.VehicleID=buggies.VehicleID;")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    #Find total vehicles
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(VehicleID) FROM vehicles;")
    totalVehicles = c.fetchall()
    for vehicle in totalVehicles:
        countVehicle = vehicle["COUNT(VehicleID)"]
    conn.commit()
    c.close()
    conn.close()
    
    #Find total motorbikes
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(VehicleID) FROM motorbikes;")
    totalMotorbikes= c.fetchall()
    for vehicle in totalMotorbikes:
        countMotorbikes = vehicle["COUNT(VehicleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total quadbikes 
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(VehicleID) FROM quadbikes;")
    totalQuadbikes = c.fetchall()
    for vehicle in totalQuadbikes :
        countQuadbikes  = vehicle["COUNT(VehicleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total buggies 
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(VehicleID) FROM buggies;")
    totalBuggies = c.fetchall()
    for vehicle in totalBuggies :
        countBuggies  = vehicle["COUNT(VehicleID)"]
    conn.commit()
    c.close()
    conn.close()

    return render_template('vehicles.html', posts=posts, countVehicle = countVehicle, countMotorbikes = countMotorbikes, countQuadbikes = countQuadbikes, countBuggies = countBuggies)




"""
Conditional selects
Selects based on a farm name or paddock name
"""
#View paddocks based on farm name
@app.route("/farm/paddock/<farmName>", methods = ["POST", "GET"])
def paddock_farm(farmName):
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM paddock WHERE FarmName = '{farmName}'")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    #Find total paddocks
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(PaddockName) FROM paddock WHERE FarmName = '{farmName}'")
    paddocks = c.fetchall()
    for paddock in paddocks:
       countName =  paddock["COUNT(PaddockName)"]
    conn.commit()
    c.close()
    conn.close()

    #Find average paddock size
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT ROUND(AVG(Size),2) FROM paddock  WHERE FarmName = '{farmName}'")
    sizes = c.fetchall()
    for size in sizes:
        avgSize = size["ROUND(AVG(Size),2)"]
    conn.commit()
    c.close()
    conn.close()

    #Find all paddocks with grass conditon = green
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(PaddockName) FROM paddock WHERE GrassCondition = 'Green' AND FarmName = '{farmName}'")
    conditions = c.fetchall()
    for condition in conditions:
        green = condition["COUNT(PaddockName)"]
    conn.commit()
    c.close()
    conn.close()
    
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(PaddockName) FROM paddock WHERE GrassCondition = 'Dry' AND FarmName = '{farmName}'")
    conditions = c.fetchall()
    for condition in conditions:
        dry = condition["COUNT(PaddockName)"]
    conn.commit()
    c.close()
    conn.close()

    return render_template('paddock.html', posts=posts, farmName = farmName, countName = countName, avgSize = avgSize, green = green, dry = dry )

#View staff based on farm name
@app.route("/farm/staff/<farmName>", methods = ["POST", "GET"])
def staff_farm(farmName):
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM staff WHERE FarmName = '{farmName}'")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    #Find total number of staff
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(StaffID) FROM staff WHERE FarmName = '{farmName}';")
    totalCount = c.fetchall()
    for count in totalCount:
        staffCount = count["COUNT(StaffID)"]
    conn.commit()
    c.close()
    conn.close()

    return render_template('staff.html', posts=posts, farmName = farmName, staffCount = staffCount )

#View cattle based on farm name
@app.route("/farm/cattle/<farmName>", methods = ["POST", "GET"])
def cattle_farm(farmName):
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM cattle WHERE PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle\
        WHERE PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    posts_count = c.fetchall()
    for post in posts_count:
        cattleCount = post["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find the average weight
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT ROUND(AVG(Weight),2) FROM cattle WHERE PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalWeight = c.fetchall()
    for total in totalWeight:
        avgWeight = total["ROUND(AVG(Weight),2)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total males
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db ,database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Male' AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalMale = c.fetchall()
    for total in totalMale:
        countMale = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total females
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Female' AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalFemale = c.fetchall()
    for total in totalFemale:
        countFemale = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total belmont reds
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Belmont Red'  AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalBelmont= c.fetchall()
    for total in totalBelmont:
        countBelmont = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total angus
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Angus' AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalAngus= c.fetchall()
    for total in totalAngus:
        countAngus = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total cross
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Cross' AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalCross= c.fetchall()
    for total in totalCross:
        countCross = total["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find average weight for males
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT ROUND(AVG(Weight),2) FROM cattle WHERE Sex = 'Male' AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' ) ;")
    totalMale = c.fetchall()
    for total in totalMale:
        avgMale = total["ROUND(AVG(Weight),2)"]
    conn.commit()
    c.close()
    conn.close()
    
    #Find average weight for females
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT ROUND(AVG(Weight),2) FROM cattle WHERE Sex = 'Female' AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' ) ;")
    totalFemale = c.fetchall()
    for total in totalFemale:
        avgFemale = total["ROUND(AVG(Weight),2)"]
    conn.commit()
    c.close()
    conn.close()
    
    return render_template('cattle.html', posts=posts, farmName = farmName, count = cattleCount, avgWeight = avgWeight, countMale = countMale, countFemale = countFemale, countBelmont = countBelmont, countAngus = countAngus, countCross = countCross, avgMale = avgMale, avgFemale = avgFemale )

#View vehicles based on farm name
@app.route("/farm/vehicles/<farmName>", methods = ["POST", "GET"])
def vehicle_farm(farmName):
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM vehicles INNER JOIN vehicle_brands ON vehicles.VehicleID=vehicle_brands.VehicleID AND vehicles.FarmName = '{farmName}' LEFT JOIN motorbikes ON vehicles.VehicleID=motorbikes.VehicleID LEFT JOIN quadbikes ON vehicles.VehicleID=quadbikes.VehicleID LEFT JOIN buggies ON vehicles.VehicleID=buggies.VehicleID;")
    posts = c.fetchall()
    conn.commit()
    c.close()
    conn.close()

    #Find total vehicles
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(VehicleID) FROM vehicles WHERE FarmName = '{farmName}';")
    totalVehicles = c.fetchall()
    for vehicle in totalVehicles:
        countVehicle = vehicle["COUNT(VehicleID)"]
    conn.commit()
    c.close()
    conn.close()
    
    #Find total motorbikes
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(VehicleID) FROM vehicles WHERE VehicleID IN ( SELECT VehicleID FROM motorbikes ) AND FarmName = '{farmName}';")
    totalMotorbikes= c.fetchall()
    for vehicle in totalMotorbikes:
        countMotorbikes = vehicle["COUNT(VehicleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total quadbikes 
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(VehicleID) FROM vehicles WHERE VehicleID IN ( SELECT VehicleID FROM quadbikes ) AND FarmName = '{farmName}';")
    totalQuadbikes = c.fetchall()
    for vehicle in totalQuadbikes :
        countQuadbikes  = vehicle["COUNT(VehicleID)"]
    conn.commit()
    c.close()
    conn.close()

    #Find total buggies 
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(VehicleID) FROM vehicles WHERE VehicleID IN ( SELECT VehicleID FROM buggies ) AND FarmName = '{farmName}';")
    totalBuggies = c.fetchall()
    for vehicle in totalBuggies :
        countBuggies  = vehicle["COUNT(VehicleID)"]
    conn.commit()
    c.close()
    conn.close()

    return render_template('vehicles.html', posts=posts, farmName = farmName, countVehicle = countVehicle, countMotorbikes = countMotorbikes, countQuadbikes = countQuadbikes, countBuggies = countBuggies )


#Farm Stats
@app.route("/farm/stats/<farmName>", methods = ["POST", "GET"])  
def farm_stats(farmName):
    #Get total number of staff for the farm
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(staffID) FROM staff WHERE FarmName = '{farmName}' ")
    staffNumbers = c.fetchall()
    for numbers in staffNumbers:
        countStaff = numbers["COUNT(staffID)"]
    conn.commit()
    c.close()
    conn.close()


    #Get total number of staff for the paddocks
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(PaddockName) FROM paddock WHERE FarmName = '{farmName}' ")
    paddockNumbers = c.fetchall()
    for numbers in paddockNumbers:
        countPaddock = numbers["COUNT(PaddockName)"]
    conn.commit()
    c.close()
    conn.close()

    #Get total number of staff for the vehicles
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(VehicleID) FROM vehicles WHERE FarmName = '{farmName}' ")
    vehicleNumbers = c.fetchall()
    for numbers in vehicleNumbers:
        countVehicles = numbers["COUNT(VehicleID)"]
    conn.commit()
    c.close()
    conn.close()
    
    #Get total number of cattle for the vehicles
    conn = pymysql.connect(host=host_db, user=user_db, password=password_db, database=database_db, charset=charset_db, cursorclass=cursorclass_db)
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    cattleNumbers = c.fetchall()
    for numbers in cattleNumbers:
        countCattle = numbers["COUNT(CattleID)"]
    conn.commit()
    c.close()
    conn.close()
    


    return render_template('farm_stats.html', staffNumbers = countStaff, paddockNumbers = countPaddock, vehicleNumbers = countVehicles, farmName = farmName, cattleNumbers = countCattle)
