# Header Comment
from flask import Flask, render_template, request, session
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import flash
from flask import url_for
import urllib
import json
import random
import csv
import sqlite3
import os


class SQLHandler(object):
    """docstring for SQLHandler."""

    def __init__(self, dbname):
        super(SQLHandler, self).__init__()
        self.DB_FILE = dbname

    def run(self, command):
        self.db = sqlite3.connect(self.DB_FILE)  # open if file exists, otherwise create
        self.c = self.db.cursor()  # facilitate db ops
        self.c.execute(command)
        if "select" in command.lower():
            return self.c.fetchall()
        self.db.commit()  # save changes

    def dbclose(self):
        self.db.close()  # close database



app = Flask(__name__)  # create instance of class Flask
app.secret_key = "dfsgdfg"



@app.route("/auth")
def auth():
    command = "SELECT * FROM loginfo WHERE username LIKE '{}'".format(
        request.args["username"])
    pair = db.run(command)
    print("#######")
    print(pair)
    if len(pair) == 0:
        flash("Username not found")
        return redirect("/login")
    if pair[0][0] == request.args["username"]:
        if pair[0][1] == request.args["password"]:
            session["username"] = request.args["username"]
            flash("Successfully logged in as: {}".format(session['username']))
            print("HERE")
            return redirect("/welcome")
        flash("Wrong password")
        return redirect("/login")
    flash("Wrong username")
    return redirect("/login")



@app.route("/")  # assign following fxn to run when root route requested
def index():
    if "username" in session:
        return redirect("/welcome")
    # return redirect("/login")
    return render_template("index.html")

@app.route("/login")
def login():
    if "username" in session:
        return redirect("/welcome")
    else:
        return render_template("login.html")


@app.route("/register")
def register():
    if len(request.args) > 0:
        username = request.args["username"]
        password = request.args["password"]
        confirm = request.args["confirm"]
        existence_command = "SELECT * FROM loginfo WHERE username LIKE '{}'".format(
            username)
        names = db.run(existence_command)
        if len(names) != 0:
            flash("Username already taken")
            return redirect("/register")
        if password != confirm:
            flash("Password and confirmation don't match")
            return redirect("/register")
        else:
            insert_username = "INSERT INTO loginfo VALUES ('{}', '{}')".format(
                username, password)
            db.run(insert_username)html 
            flash("Successful registration")
            return redirect("/login")
    if "username" in session:
        return redirect("/welcome")
    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("username")
    flash("just loggged out")
    return redirect("/login")



@app.route("/welcome")
def welcome():
    if "username" in session:
        return render_template('welcome.html', username = session["username"])
    return redirect("/")


if __name__ == "__main__":
    db = SQLHandler("data.db")
    app.debug = True
    app.run()
