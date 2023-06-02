# Climate analysis and API using SQLAlchemy and Flask
Files to run are climate_starter and app.py, located in SurfsUp folder.
### Part 1: Analyse and Explore the Climate Data
In this section, Python and SQLAlchemy are used to do a basic climate analysis and data exploration of a given climate database. Specifically, SQLAlchemy ORM queries, Pandas, and Matplotlib.
1. Use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete the climate analysis and data exploration.
2. Use the SQLAlchemy create_engine() function to connect to the SQLite database.
3. Use the SQLAlchemy automap_base() function to reflect the tables into classes, and then save references to the classes named station and measurement.
4. Link Python to the database by creating a SQLAlchemy session.
5. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.
   - **Precipitation Analysis**
     1. Find the most recent date in the dataset.
     2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
     3. Select only the "date" and "prcp" values.
     4. Load the query results into a Pandas DataFrame, and set the index to the "date" column.
     5. Sort the DataFrame values by "date".
     6. Plot the results by using the DataFrame `plot` method, as the following image shows
     7. Use Pandas to print the summary statistics for the precipitation data.
   - **Station Analysis**
     1. Design a query to calculate the total number of stations in the dataset.
     2. Design a query to find the most-active stations (that is, the stations that have the most rows). Using the most-active station id, calculate the lowest, highest, and average temperatures.
     3. Design a query to get the previous 12 months of temperature observation (TOBS) data. Plot the results as a histogram with bins=12, as the following image shows:

### Part 2: Design the Climate App
Create a Flask API based on the queries developed above.

1. `/`
   - Start at the homepage. List all the available routes.

2. `/api/v1.0/precipitation`
   - Convert the query results to a dictionary by using date as the key and prcp as the value.
   - Return the JSON representation of your dictionary.

3. `/api/v1.0/stations`
   - Return a JSON list of stations from the dataset.
4. `/api/v1.0/tobs`
   - Query the dates and temperature observations of the most-active station for the previous year of data. 
   - Return a JSON list of temperature observations for the previous year.

5. `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
   - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
   - For a specified start, calculate `TMIN`, `TAVG`, and `TMA`X for all the dates greater than or equal to the start date.
   - For a specified start date and end date, calculate `TMIN`, `TAVG`, and `TMAX` for the dates from the start date to the end date, inclusive.
     
