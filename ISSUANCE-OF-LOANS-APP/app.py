# -*- coding utf-8 -*-
import secrets
from datetime import datetime

from flask import Flask, render_template, redirect, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{0}:{1}@{2}/{3}".format(
    secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Loan_issuance_list(db.Model):

    __tablename__ = "loan_issuance_list"
    id = db.Column(db.Integer, primary_key=True)
    loan_name = db.Column(db.String(50), nullable=False)
    client_passport_number = db.Column(db.String(50), nullable=False)
    # add_date = db.Column(db.DateTime, default=datetime.utcnow)
    loan_amount = db.Column(db.Integer, nullable=False)
    loan_term = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<loan_issuance_list %r>" % self.id


class Clients_list(db.Model):

    __tablename__ = "clients_list"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)
    passport_number = db.Column(db.String(50), nullable=False)
    number_of_loan_applications = db.Column(db.Integer)

    def __init__(self, age):
        self.first_name = first_name
        self.last_name = last_name
        self.registration_date = registration_date
        self.passport_number = passport_number
        self.number_of_loan_applications = number_of_loan_applications

    def __repr__(self):
        return "<clients_list %r>" % self.id


class Loans_list(db.Model):

    __tablename__ = "loans_list"
    id = db.Column(db.Integer, primary_key=True)
    loan_name = db.Column(db.String(50), nullable=False)
    loan_rate = db.Column(db.Float, nullable=False)
    number_of_loan_applications = db.Column(db.Integer)

    def __init__(self, age):
        self.loan_name = loan_name
        self.loan_rate = loan_rate
        self.number_of_loan_applications = number_of_loan_applications

    def __repr__(self):
        return "<loans_list %r>" % self.id


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/loan_issuance_list")
def Loan_issuance_list_func():
    Loan_issuance_list_table = Loan_issuance_list.query.order_by(
        Loan_issuance_list.id.desc()
    ).all()
    return render_template(
        "loan_issuance_list.html", Loan_issuance_list_table=Loan_issuance_list_table
    )


@app.route("/add_loan_issuance", methods=["POST", "GET"])
def add_loan_issuance():
    if request.method == "POST":
        loan_name = request.form["loan_name"]
        client_passport_number = request.form["client_passport_number"]
        loan_amount = request.form["loan_amount"]
        loan_term = request.form["loan_term"]

        Loan_issuance_list_form = Loan_issuance_list(
            loan_name=loan_name,
            client_passport_number=client_passport_number,
            loan_amount=loan_amount,
            loan_term=loan_term,
        )

        try:
            db.session.add(Loan_issuance_list_form)
            db.session.commit()
            return redirect("/loan_issuance_list")
        except:
            return "an error occurred while adding an article"
    else:
        return render_template("add_loan_issuance.html")


@app.route("/loan_issuance_list/<int:id>/edit", methods=["POST", "GET"])
def edit_loan_issuance(id):
    edit_element = Loan_issuance_list.query.get(id)
    if request.method == "POST":
        edit_element.loan_name = request.form["loan_name"]
        edit_element.client_passport_number = request.form["client_passport_number"]
        edit_element.loan_amount = request.form["loan_amount"]
        edit_element.loan_term = request.form["loan_term"]

        try:
            db.session.commit()
            return redirect("/loan_issuance_list")
        except:
            return "error while editing"
    else:

        return render_template("edit_loan_issuance.html", edit_element=edit_element)


@app.route("/loan_issuance_list/<int:id>/del")
def delete_loan_issuance(id):
    Loan_issuance_list_delete_element = Loan_issuance_list.query.get_or_404(id)

    try:
        db.session.delete(Loan_issuance_list_delete_element)
        db.session.commit()
        return redirect("/loan_issuance_list")
    except:
        return "an error occurred while deleting the article"


if __name__ == "__main__":
    app.run(debug=True)
