from cattleDatabase import *

@app.route("/")
def home():
    return render_template("home.html", title = "Home Page")


#Farm view
@app.route("/farm")
def farm():
    #Find all farms
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM farm")
    posts = c.fetchall()

    #Find total number of farms
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(FarmName) FROM farm")
    names = c.fetchall()
    for name in names:
        countName = name["COUNT(FarmName)"]


    return render_template('farm.html', posts=posts, countName = countName)
    

#Paddock view
@app.route("/paddock")
def paddock():
    #find all paddocks
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM paddock")
    posts = c.fetchall()

    #Find total paddocks
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(PaddockName) FROM paddock")
    paddocks = c.fetchall()
    for paddock in paddocks:
       countName =  paddock["COUNT(PaddockName)"]

    #Find average paddock size
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT AVG(Size) FROM paddock")
    sizes = c.fetchall()
    for size in sizes:
        avgSize = size["AVG(Size)"]

    #Find all paddocks with grass conditon = green

    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(PaddockName) FROM paddock WHERE GrassCondition = 'Green'")
    conditions = c.fetchall()
    for condition in conditions:
        green = condition["COUNT(PaddockName)"]

    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(PaddockName) FROM paddock WHERE GrassCondition = 'Dry'")
    conditions = c.fetchall()
    for condition in conditions:
        dry = condition["COUNT(PaddockName)"]

    return render_template('paddock.html', posts=posts, countName = countName, avgSize = avgSize, green = green, dry = dry)




#Bin view
@app.route("/feed_bins/<paddockName>", methods = ['GET','POST'])
def feed_bins(paddockName):
    #Find all bins
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM feed_bins WHERE PaddockName = '{paddockName}'")
    posts = c.fetchall()

    #Find count of bins
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(BinNumber) FROM feed_bins WHERE PaddockName = '{paddockName}'")
    totalBins = c.fetchall()
    for bin in totalBins:
        countBins = bin["COUNT(BinNumber)"]

    #Find average bin level
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT AVG(BinLevel) FROM feed_bins WHERE PaddockName = '{paddockName}'")
    totalLevels = c.fetchall()
    for bin in totalLevels:
        avgLevel = bin["AVG(BinLevel)"]

    #Find count of bins containing wheat
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(BinNumber) FROM feed_bins WHERE PaddockName = '{paddockName}' AND BinContains = 'Wheat'")
    totalBins = c.fetchall()
    for bin in totalBins:
        wheatBins = bin["COUNT(BinNumber)"]

    #Find count of bins containing sorghum
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(BinNumber) FROM feed_bins WHERE PaddockName = '{paddockName}' AND BinContains = 'Sorghum'")
    totalBins = c.fetchall()
    for bin in totalBins:
        sorghumBins = bin["COUNT(BinNumber)"]

    #Find count of bins containing salt lick
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(BinNumber) FROM feed_bins WHERE PaddockName = '{paddockName}' AND BinContains = 'Salt Lick'")
    totalBins = c.fetchall()
    for bin in totalBins:
        saltBins = bin["COUNT(BinNumber)"]

    return render_template('bins.html', posts=posts, paddockName = paddockName, countBins = countBins, avgLevel = avgLevel, wheatBins = wheatBins, sorghumBins = sorghumBins, saltBins = saltBins )


#Cattle view
@app.route("/cattle")
def cattle():
    #Select and return all cattle
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM cattle")
    posts = c.fetchall()

    #Find the number of cattle
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle")
    totalCattle = c.fetchall()
    for total in totalCattle:
        count = total["COUNT(CattleID)"]
    
    #Find the average weight
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT AVG(Weight) FROM cattle")
    totalWeight = c.fetchall()
    for total in totalWeight:
        avgWeight = total["AVG(Weight)"]

    #Find total males
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Male'")
    totalMale = c.fetchall()
    for total in totalMale:
        countMale = total["COUNT(CattleID)"]

    #Find total females
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Female'")
    totalFemale = c.fetchall()
    for total in totalFemale:
        countFemale = total["COUNT(CattleID)"]

    #Find total belmont reds
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Belmont Red'")
    totalBelmont= c.fetchall()
    for total in totalBelmont:
        countBelmont = total["COUNT(CattleID)"]

    #Find total angus
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Angus'")
    totalAngus= c.fetchall()
    for total in totalAngus:
        countAngus = total["COUNT(CattleID)"]

    #Find total cross
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Cross'")
    totalCross= c.fetchall()
    for total in totalCross:
        countCross = total["COUNT(CattleID)"]


    return render_template('cattle.html', posts=posts, count = count, avgWeight = avgWeight, countMale = countMale, countFemale = countFemale, countBelmont = countBelmont, countAngus = countAngus, countCross = countCross)



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

    #Find the average weight
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT AVG(Weight) FROM cattle WHERE PaddockName = '{paddockName}'")
    totalWeight = c.fetchall()
    for total in totalWeight:
        avgWeight = total["AVG(Weight)"]

    #Find total males
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Male' AND PaddockName = '{paddockName}'")
    totalMale = c.fetchall()
    for total in totalMale:
        countMale = total["COUNT(CattleID)"]

    #Find total females
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Female' AND PaddockName = '{paddockName}'")
    totalFemale = c.fetchall()
    for total in totalFemale:
        countFemale = total["COUNT(CattleID)"]

    #Find total belmont reds
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Belmont Red'  AND PaddockName = '{paddockName}'")
    totalBelmont= c.fetchall()
    for total in totalBelmont:
        countBelmont = total["COUNT(CattleID)"]

    #Find total angus
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Angus' AND PaddockName = '{paddockName}'")
    totalAngus= c.fetchall()
    for total in totalAngus:
        countAngus = total["COUNT(CattleID)"]

    #Find total cross
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Cross' AND PaddockName = '{paddockName}'")
    totalCross= c.fetchall()
    for total in totalCross:
        countCross = total["COUNT(CattleID)"]

    return render_template('cattle.html', posts=posts, paddockName = paddockName, cattleCount = cattleCount, count = cattleCount, avgWeight = avgWeight, countMale = countMale, countFemale = countFemale, countBelmont = countBelmont, countAngus = countAngus, countCross = countCross)

#Vehicle pages
@app.route("/vehicles")
def vehicles():
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM vehicles INNER JOIN vehicle_brands ON vehicles.VehicleID=vehicle_brands.VehicleID LEFT JOIN motorbikes ON vehicles.VehicleID=motorbikes.VehicleID LEFT JOIN quadbikes ON vehicles.VehicleID=quadbikes.VehicleID LEFT JOIN buggies ON vehicles.VehicleID=buggies.VehicleID;")
    posts = c.fetchall()

    #Find total vehicles
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(VehicleID) FROM vehicles;")
    totalVehicles = c.fetchall()
    for vehicle in totalVehicles:
        countVehicle = vehicle["COUNT(VehicleID)"]
    
    #Find total motorbikes
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(VehicleID) FROM motorbikes;")
    totalMotorbikes= c.fetchall()
    for vehicle in totalMotorbikes:
        countMotorbikes = vehicle["COUNT(VehicleID)"]

    #Find total quadbikes 
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(VehicleID) FROM quadbikes;")
    totalQuadbikes = c.fetchall()
    for vehicle in totalQuadbikes :
        countQuadbikes  = vehicle["COUNT(VehicleID)"]

    #Find total buggies 
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(VehicleID) FROM buggies;")
    totalBuggies = c.fetchall()
    for vehicle in totalBuggies :
        countBuggies  = vehicle["COUNT(VehicleID)"]

    return render_template('vehicles.html', posts=posts, countVehicle = countVehicle, countMotorbikes = countMotorbikes, countQuadbikes = countQuadbikes, countBuggies = countBuggies)

#staff homepage
@app.route("/staff_home")
def staff_home():
    
    #Select all staff
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT * FROM staff;")
    posts = c.fetchall()

    #Find total number of staff
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute("SELECT COUNT(StaffID) FROM staff;")
    totalCount = c.fetchall()
    for count in totalCount:
        staffCount = count["COUNT(StaffID)"]
    return render_template('staff.html', posts=posts, staffCount = staffCount)


"""
Conditional selects
Selects based on a farm name or paddock name
"""
#View paddocks based on farm name
@app.route("/farm/paddock/<farmName>", methods = ["POST", "GET"])
def paddock_farm(farmName):
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM paddock WHERE FarmName = '{farmName}'")
    posts = c.fetchall()

    #Find total paddocks
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(PaddockName) FROM paddock WHERE FarmName = '{farmName}'")
    paddocks = c.fetchall()
    for paddock in paddocks:
       countName =  paddock["COUNT(PaddockName)"]

    #Find average paddock size
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT AVG(Size) FROM paddock  WHERE FarmName = '{farmName}'")
    sizes = c.fetchall()
    for size in sizes:
        avgSize = size["AVG(Size)"]

    #Find all paddocks with grass conditon = green

    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(PaddockName) FROM paddock WHERE GrassCondition = 'Green' AND FarmName = '{farmName}'")
    conditions = c.fetchall()
    for condition in conditions:
        green = condition["COUNT(PaddockName)"]

    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(PaddockName) FROM paddock WHERE GrassCondition = 'Dry' AND FarmName = '{farmName}'")
    conditions = c.fetchall()
    for condition in conditions:
        dry = condition["COUNT(PaddockName)"]

    return render_template('paddock.html', posts=posts, farmName = farmName, countName = countName, avgSize = avgSize, green = green, dry = dry )

#View staff based on farm name
@app.route("/farm/staff/<farmName>", methods = ["POST", "GET"])
def staff_farm(farmName):
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM staff WHERE FarmName = '{farmName}'")
    posts = c.fetchall()

    #Find total number of staff
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(StaffID) FROM staff WHERE FarmName = '{farmName}';")
    totalCount = c.fetchall()
    for count in totalCount:
        staffCount = count["COUNT(StaffID)"]

    return render_template('staff.html', posts=posts, farmName = farmName, staffCount = staffCount )

#View cattle based on farm name
@app.route("/farm/cattle/<farmName>", methods = ["POST", "GET"])
def cattle_farm(farmName):
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM cattle WHERE PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    posts = c.fetchall()

    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle\
        WHERE PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    posts_count = c.fetchall()
    for post in posts_count:
        cattleCount = post["COUNT(CattleID)"]

    #Find the average weight
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT AVG(Weight) FROM cattle WHERE PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalWeight = c.fetchall()
    for total in totalWeight:
        avgWeight = total["AVG(Weight)"]

    #Find total males
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Male' AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalMale = c.fetchall()
    for total in totalMale:
        countMale = total["COUNT(CattleID)"]

    #Find total females
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Sex = 'Female' AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalFemale = c.fetchall()
    for total in totalFemale:
        countFemale = total["COUNT(CattleID)"]

    #Find total belmont reds
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Belmont Red'  AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalBelmont= c.fetchall()
    for total in totalBelmont:
        countBelmont = total["COUNT(CattleID)"]

    #Find total angus
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Angus' AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalAngus= c.fetchall()
    for total in totalAngus:
        countAngus = total["COUNT(CattleID)"]

    #Find total cross
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(CattleID) FROM cattle WHERE Breed = 'Cross' AND PaddockName IN ( SELECT PaddockName FROM paddock WHERE FarmName = '{farmName}' );")
    totalCross= c.fetchall()
    for total in totalCross:
        countCross = total["COUNT(CattleID)"]
    
    return render_template('cattle.html', posts=posts, farmName = farmName, count = cattleCount, avgWeight = avgWeight, countMale = countMale, countFemale = countFemale, countBelmont = countBelmont, countAngus = countAngus, countCross = countCross )

#View vehicles based on farm name
@app.route("/farm/vehicles/<farmName>", methods = ["POST", "GET"])
def vehicle_farm(farmName):
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT * FROM vehicles INNER JOIN vehicle_brands ON vehicles.VehicleID=vehicle_brands.VehicleID AND vehicles.FarmName = '{farmName}' LEFT JOIN motorbikes ON vehicles.VehicleID=motorbikes.VehicleID LEFT JOIN quadbikes ON vehicles.VehicleID=quadbikes.VehicleID LEFT JOIN buggies ON vehicles.VehicleID=buggies.VehicleID;")
    posts = c.fetchall()

    #Find total vehicles
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(VehicleID) FROM vehicles WHERE FarmName = '{farmName}';")
    totalVehicles = c.fetchall()
    for vehicle in totalVehicles:
        countVehicle = vehicle["COUNT(VehicleID)"]
    
    #Find total motorbikes
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(VehicleID) FROM vehicles WHERE VehicleID IN ( SELECT VehicleID FROM motorbikes ) AND FarmName = '{farmName}';")
    totalMotorbikes= c.fetchall()
    for vehicle in totalMotorbikes:
        countMotorbikes = vehicle["COUNT(VehicleID)"]

    #Find total quadbikes 
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(VehicleID) FROM vehicles WHERE VehicleID IN ( SELECT VehicleID FROM quadbikes ) AND FarmName = '{farmName}';")
    totalQuadbikes = c.fetchall()
    for vehicle in totalQuadbikes :
        countQuadbikes  = vehicle["COUNT(VehicleID)"]

    #Find total buggies 
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute(f"SELECT COUNT(VehicleID) FROM vehicles WHERE VehicleID IN ( SELECT VehicleID FROM buggies ) AND FarmName = '{farmName}';")
    totalBuggies = c.fetchall()
    for vehicle in totalBuggies :
        countBuggies  = vehicle["COUNT(VehicleID)"]

    return render_template('vehicles.html', posts=posts, farmName = farmName, countVehicle = countVehicle, countMotorbikes = countMotorbikes, countQuadbikes = countQuadbikes, countBuggies = countBuggies )


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
