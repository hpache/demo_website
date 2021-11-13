from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, InfoModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ccnhrenkzxnrsz:3be3d7647008c9d280a91e44a8d27f72d744387a91ae7aba0debc434a9f8e0fe@ec2-54-166-167-192.compute-1.amazonaws.com:5432/d40cickjvcgvnf"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

@app.route("/")
def index():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)