# Import dependencies
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
# from datetime import date
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save reference to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create an app
app = Flask(__name__)

# 1. Define what to do when a user hits the index route

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the Climate App. Available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"Replace 'start' and 'end' with dates in YYYY-MM-DD format<br/>"
    )


# 2. Convert the query results to a dictionary by using date as the key and prcp as the value.
#    Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for precipitation information ...")
    session = Session(engine)
    results_output = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date > dt.datetime(2016, 8, 23)
               ).order_by(Measurement.date.desc())
    session.close()
    precip = {date: prcp for date, prcp in results_output}
    return jsonify(precip)


# 3. Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    st_count = session.query(
        Station.station, Station.name).group_by(Station.station)
    session.close()
    # station_list = list(np.ravel(st_count))
    print("working on station query")
    station_info = {stn: nm for stn, nm in st_count}
    return jsonify(station_info)
#

# 4. Query the dates and temperature observations of the most-active station for the previous year of data.
#   Return a JSON list of temperature observations for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():
    print("working on tobs query")
    session = Session(engine)
    active_12 = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > dt.datetime(2016, 8, 18)).filter(Measurement.station == "USC00519281").\
        order_by(Measurement.date)
    session.close()
    active12_output = {day: tob for day, tob in active_12}
    return jsonify(active12_output)


# 5.a. Return the min, max, and average temperatures calculated from the given start date to the end of the dataset

@app.route("/api/v1.0/<start>")
def startDate(start):
    print("working on start date query")
    start_date = dt.date.fromisoformat(start)
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    session.close()
    
    tempList = []
    for min, avg, max in results:
        output_dict = {}
        output_dict["Min"] = min
        output_dict["Average"] = avg
        output_dict["Max"] = max
        tempList.append(output_dict)

    return jsonify(tempList)
    
                   
# 5.b. Return the min, max, and average temperatures calculated from the given start date to the given end date

@app.route("/api/v1.0/<start>/<end>")
def startEndDate(start, end):
    print("working on start/end date query")
    start_date = dt.date.fromisoformat(start)
    end_date = dt.date.fromisoformat(end)
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()
    
    tempList = []
    for min, avg, max in results:
        output_dict = {}
        output_dict["Min"] = min
        output_dict["Average"] = avg
        output_dict["Max"] = max
        tempList.append(output_dict)
         
    return jsonify(tempList)
                     
           
           
           
if __name__ == "__main__":
    app.run(debug=True)

           
           
           
           
           
           
            
            
           
           
           