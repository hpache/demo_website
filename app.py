from flask import Flask, render_template, request, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, InfoModel
import psycopg2

# Starting our flask session
app = Flask(__name__)

# Connecting to the postgresql data base
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://@localhost:5432/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)

# Landing page look at html for more detail
@app.route("/")
def index():

    return render_template("index.html")

# Create page look at html for more detail 
@app.route("/create_account")
def form():
    return render_template("create.html")

# This isn't a page the user can see, just an intermediary
@app.route("/add", methods=["POST"])
def add():

    # Getting the name from the create.html file
    name = request.form["name"]
    # Getting the email from the create.html file
    email = request.form["email"]
    # Getting the password from the create.html file
    password = request.form["password"]
    # Creating a new user object, not secured at all 
    new_user = InfoModel(name = name, email= email, password = password)
    # Adding the user information to local database 
    db.session.add(new_user)
    db.session.commit()

    # The add method sends the user back to the landing page
    return redirect(url_for("index"))

# Login method, look at html file for more info
@app.route("/login")
def login():
    return render_template("login.html")

# Check method, validates user information
@app.route("/check", methods = ["POST"])
def check():
    
    # Connecting to the database with psycopg2 library, don't really need this but I found it online
    connection = psycopg2.connect("postgresql://@localhost:5432/flask")
    cursor = connection.cursor()
    # Requesting the email from the database
    email = request.form["email"]
    # SQL Syntax
    select_Query = "SELECT * FROM info_table WHERE email = %s"
    cursor.execute(select_Query,(email,))
    data = cursor.fetchall()

    if len(data) == 0:
        return "Error Account Not Found"
    else:
        # Getting the password from the html file 
        password = request.form["password"]
        
        # Comparing the input password with the password in the database
        if password == data[0][3]:
            return "Success"
        else:
            return "Fail"




if __name__ == "__main__":
    app.run(debug=True)

