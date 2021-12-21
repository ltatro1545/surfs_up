# import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
#########################

# Set up the Database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

# Reflect the table
Base.prepare(engine, reflect=True)

# Create variables for two classes: measurement and station
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to the database
session = Session(engine)
##########################

# Create a Flask instance
app = Flask(__name__)

# create home Flask route
@app.route('/')
def welcome():
    return (
    '''
    Welcome to the Hawaii Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Create precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # prev year is equal to current date - 365 days
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # query for precip data from the past year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    # jsonify results
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Put stations in list
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    # jsonify results (station=station) allows jsonify to function here
    return jsonify(stations=stations)

# Create monthly temperature route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    # prev year is equal to current date minus 365 days
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # query primary station for all observations in last year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # unravel results into one dimensional array, then convert to list
    temps = list(np.ravel(results))
    # jsonify list and return results
    return jsonify(temps=temps)

# Create statistics route that allows you to input the start and end date in the route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # create a list of measured data to query with
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    # query selection and ravel results, then jsonify the return
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
