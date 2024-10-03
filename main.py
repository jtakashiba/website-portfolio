from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app) #CSS Framework

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/aerospace")
def aerospace():
    return render_template("aerospace.html")

@app.route("/transition")
def transition():
    return render_template("transition.html")

@app.route("/soft_skills")
def soft_skills():
    return render_template("soft_skills.html")

@app.route("/goals")
def goals():
    return render_template("goals.html")

if __name__ == '__main__':
    app.run(debug=True)