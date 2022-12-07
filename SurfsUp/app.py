# Import dependencies
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(autoload_with=engine)

# Save reference to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create an app, being sure to pass __name__
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
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start><end>"
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


#     results = list(np.ravel(results_output))
    
    
#     for result in results_output:
        
#         print(f"{result._asdict()}")

#     results = list(np.ravel(results_output))
#     return jsonify(results)

    
    # data = [((f"{result[0]}, {result[1]}") for result in results_output)]
    # precip = {key: value for (key, value) in data}   
    # return jsonify(precip)
# two methods _____________
#     prior12_rows = [{"Date": result[0], "Precipitation": result[1]}
#                 for result in results_output]
#     return (f"{prior12_rows}")

if __name__ == "__main__":
    app.run(debug=True)
  
