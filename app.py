from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, InfoModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ghdcurxdtgbxqu:8f59105edbba75ccd115e3bae7ec41e336850cfd3f0e3af0fdd00e6cd45e5168@ec2-23-23-133-10.compute-1.amazonaws.com:5432/dok6t6itvuucf"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

@app.route("/")
def index():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)