# 1. import Flask
from flask import Flask

# Create an app, being sure to pass __name__
app = Flask(__name__)

# 1. Define what to do when a user hits the index route


@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to the Climate App. Available routes: . . ."

# 2. Convert the query results to a dictionary by using date as the key and prcp as the value.
#    Return the JSON representation of your dictionary.


@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for precipitation information ...")
    return "<placeholder for info>"

# 3. Return a JSON list of stations from the dataset.


@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for stations information ...")
    return "<placeholder for info>"

# 4. Query the dates and temperature observations of the most-active station for the previous year of data.
#    Return a JSON list of temperature observations for the previous year.


@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for tobs information ...")
    return "<placeholder for info>"

# 5. Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
#    For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.


@app.route("/api/v1.0/<start>")
def start():
    print("Server received request for information after <start date>...")
    return "<placeholder for info>"


# 5. Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
#    For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
@app.route("/api/v1.0/<start>/<end>")
def startEnd():
    print("Server received request for stations information between <start> and <end> ...")
    return "<placeholder for info>"

# `python app.py`


if __name__ == "__main__":
    app.run(debug=True)
