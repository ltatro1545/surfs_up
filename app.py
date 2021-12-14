# import dependencies
from flask import Flask

# Create a Flask instance
app = Flask(__name__)

# create Flask route
@app.route('/')
def hello_world():
    return "Hello world"

# Run Flask app
