# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)



# Clean the JSON data to grab the specifc information to visualize
# need graph variables for D3: 
# lan/lng of crash sites for map:
#count of 

# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/graph")
def graph():
    return render_template("index.html")
#Need d3 code to graph the crash data Need variables to compare

@app.route("/map")
def map():
    return render_template("index.html")
# this map code is in the week 17 class 2 act 3
    #This code needs its own html and static folder for the js and css

@app.route("/bubble")
def bubble():
    return render_template("index.html")
    #New java script library 

    


if __name__ == "__main__":
    app.run(debug=True)