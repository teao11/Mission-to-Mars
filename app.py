# Import Dependencies

# Use Flask to render a template, redirecting to another url, and creating a URL
from flask import Flask, render_template, redirect, url_for
# PyMongo to interact with our Mongo database
from flask_pymongo import PyMongo
# to use the scraping code, we will convert from Jupyter notebook to Python
import scraping

# Set up the flask application
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for the HTML page
@app.route("/") # Tells Flask what to display when we're looking at the home page
def index(): 
   mars = mongo.db.mars.find_one() # PyMongo to find the "mars" collection in our database
   return render_template("index.html", mars=mars) # Return an HTML template using an index.html file

# Define route that will be linked to button to scrape updated data
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars # Assign a new variable that points to our Mongo database
   mars_data = scraping.scrape_all() # Variable to hold the newly scraped data (using function in .py file)
   mars.update({}, mars_data, upsert=True) # update the database
   return redirect('/', code=302) # Navigate our page back to / where we can see the updated content

# Code to run the application
if __name__ == "__main__":
   app.run()