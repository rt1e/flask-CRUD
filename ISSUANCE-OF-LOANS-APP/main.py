import secrets

import pymysql
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Loan_issuance_list")
def Loan_issuance_list():
    return render_template("Loan_issuance_list.html")


if __name__ == "__main__":
    app.run(debug=True)
