# import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask
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

# create Flask route
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

# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
