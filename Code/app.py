# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)



# Clean the JSON data to grab the specifc information to visualize


# create route that renders index.html template
@app.route("/")
def index():
    team_list = ["Jumpers", "Dunkers", "Dribblers", "Passers"]
    return render_template("index.html", list=team_list)
#Need to edit the homepage index.html to display car crash theme (background pic info stats, etc)
# Gif example of complex data
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
    #code exmaples for bubble chart
    #http://jsfiddle.net/VividD/WDCpq/8/
    #https://observablehq.com/@d3/bubble-chart
    


if __name__ == "__main__":
    app.run(debug=True)