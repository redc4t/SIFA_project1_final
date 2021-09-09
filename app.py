from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
class Register(db.Model):
    name = bd.Column(db.String(30), nullable=False, primary_key=True)
    password = db.Column(db.String(30), nullable=False)

db.create_all()



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.form:
        person = Register(name=request.form.get("name"), password=bcrypt.generate_password_hash(request.form.get("password")))
        db.session.add(person)
        db.session.commit()
    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/charsheet')
def charsheet():
    return render_template('charsheet.html')

if __name__=="__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')


