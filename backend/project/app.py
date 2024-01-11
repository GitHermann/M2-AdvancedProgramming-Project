from flask import Flask
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__),".ini"))

# create and initialize a new Flask app
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['MONGO_URI'] = config['PROD']['DB_URI']

@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    #app.config['DEBUG'] = True
    #app.config['MONGO_URI'] = config['PROD']['DB_URI']
    app.run()