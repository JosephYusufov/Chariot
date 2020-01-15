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
import random


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


@app.route("/itinerary/list", methods=["GET"])
def itinerary():
    # get request that responds with a list of all the itinerary that the user has
    command = "SELECT * FROM {}".format(session["username"])
    useritens = db.run(command)
    # print(useritens)
    out_dict = {}
    out_dict["itinerary"] = []
    for iten in useritens:
        iten_dict = json.loads(iten[1])
        print(iten_dict)
        out_dict["itinerary"].append({"name":iten_dict["name"], "id":iten_dict["id"], "date":iten_dict["itineraryDate"]})
    # print(out_dict)
    return json.dumps(out_dict)


@app.route("/itinerary/create", methods=["GET", "POST"])
def itinerary_create():
    # get request: shows the creation pagepass
    # post request createst it
    if request.method == "POST":
        command = "CREATE TABLE IF NOT EXISTS {} (iten_id TEXT, iten_json TEXT);"
        command = command.format(session["username"])
        insert_command = "INSERT INTO {user} VALUES ('{id}', '{json}')"
        dumped_json = (json.dumps(request.form))
        mutable_json = json.loads(dumped_json)
        mutable_json["id"] = random.randint(0, 9999999)

        # This is where the itinerary creation magic happens. Scroll down to see this function in action.
        mutable_json["events"] = mapquest_create( mutable_json["events"].split(','), mutable_json["startPoint"] )
        print(mutable_json)
        dumped_json = json.dumps(mutable_json)
        print("JSON START")
        print(dumped_json)
        print("JSON END")
        insert_command = insert_command.format(user = session["username"], id = mutable_json["id"], json = dumped_json)
        # print(insert_command)
        db.run(command)
        db.run(insert_command)
        return dumped_json
        # json dump that object

        # take care of error handling

    else:
        return render_template("create_itinerary.html")


@app.route("/itinerary/delete/<int:id>", methods=["GET"])
def itinerary_delete(id):
    command = "DELETE FROM {username} WHERE iten_id = {id_to_delete}".format(username=session["username"], id_to_delete=id)
    db.run(command)
    return json.dumps({"status":"successful", "deleted_id":id})

@app.route("/itinerary/<int:id>")
def itinerary_details(id):
    # just return the template.
    #
    return render_template("view_itinerary.html", username=session["username"])

@app.route("/itinerary/details/<int:id>")
def itinerary_view(id):
    command = "SELECT iten_json FROM {username}".format(username = session["username"])
    allitens_raw = db.run(command)
    print("--ALLITENS--")
    print("{} LONG".format(len(allitens_raw)))
    print(allitens_raw)
    print("--ENDITENS--")
    for iten_json in allitens_raw:
        print(iten_json)
        iten_dict = json.loads(iten_json[0])
        # print("ITEN_DICT"iten_dict)
        print(json.dumps(iten_dict, indent=4, sort_keys=True))
        if (iten_dict["id"] == id):

            out_dict = {}
            out_dict["name"] = iten_dict["name"]
            out_dict["date"] = iten_dict["itineraryDate"]
            out_dict["startPoint"] = iten_dict["startPoint"]

            # When mapquest_create() is ready, get rid of this loop
            out_dict["events"] = iten_dict["events"]
            # out_dict["events"] = []
            # for x in iten_dict["events"].split(","):
            #     if x == "Zoo":
            #         out_dict["events"].append({"name":"metrozoo", "address":"345 Chambers St", "time_start":"2020-01-15T02:29:56.647Z", "time_end":"2020-01-15T02:29:56.647Z"})
            #     if x == "Food":
            #         out_dict["events"].append({"name":"mamma mia meatballs", "address":"One Infinite Loop, CA", "time_start":"2020-01-15T02:29:56.647Z", "time_end":"2020-01-15T02:29:56.647Z"})
            #     if x == "Park":
            #         out_dict["events"].append({"name":"heroin park", "address":"69 420ST", "time_start":"2020-01-15T02:29:56.647Z", "time_end":"2020-01-15T02:29:56.647Z"})
            #     else:
            #         out_dict["events"].append({"name":"hell", "address":"davey jones locker", "time_start":"2020-01-15T02:29:56.647Z", "time_end":"2020-01-15T02:29:56.647Z"})
            return json.dumps(out_dict)
        # else:
            # return json.dumps({"error":"user not found"})
    return json.dumps({"error":"database not initialized, invalid program state"})


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
            db.run(insert_username)
            flash("Successful registration")
            return redirect("/login")
    if "username" in session:
        return redirect("/welcome")
    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("username")
    flash("Successfully Logged Out")
    return redirect("/login")


@app.route("/welcome")
def welcome():
    if "username" in session:
        return render_template('welcome.html', username = session["username"])
    return redirect("/")


@app.route("/create-itinerary")
def create_itinerary():
    return render_template('create_itinerary.html', username = session["username"])

def mapquest_create(events_list, starting_point):
    origin = starting_point.replace(" ", "+")
    print(origin)
    events_toreturn = []
    for x in events_list:
        if x == "Park":
            e = urllib.request.urlopen("https://www.mapquestapi.com/search/v2/radius?origin={}&radius=5&maxMatches=3&ambiguities=ignore&hostedData=mqap.ntpois|group_sic_code=?|799951&outFormat=json&key=yNjXSwjvcoWeXAoUiJw9AZG6MiUvjX8f".format(origin))
            e = json.loads( e.read() )
            mapquest_event = random.choice( e["searchResults"] )
            print("--- PARK ---")
            print(mapquest_event)
            print("--- ENDPARK---")
            event = {}
            event["name"] = mapquest_event["name"]
            event["address"] = "{}, {}, {}, {}, {}".format( mapquest_event["name"], mapquest_event["fields"]["address"], mapquest_event["fields"]["city"], mapquest_event["fields"]["state"], mapquest_event["fields"]["postal_code"])
            event["time_start"] = "2020-01-15T02:29:56.647Z"
            event["time_end"] = "2020-01-15T02:29:56.647Z"
            events_toreturn.append( event )
        elif x == "Zoo":
            e = urllib.request.urlopen("https://www.mapquestapi.com/search/v2/radius?origin={}&radius=5&maxMatches=3&ambiguities=ignore&hostedData=mqap.ntpois|group_sic_code=?|842201&outFormat=json&key=yNjXSwjvcoWeXAoUiJw9AZG6MiUvjX8f".format(origin))
            e = json.loads( e.read() )
            mapquest_event = random.choice( e["searchResults"] )
            print("--- ZOO ---")
            print(mapquest_event)
            print("--- ENDZOO---")
            event = {}
            event["name"] = mapquest_event["name"]
            event["address"] = "{}, {}, {}, {}, {}".format( mapquest_event["name"], mapquest_event["fields"]["address"], mapquest_event["fields"]["city"], mapquest_event["fields"]["state"], mapquest_event["fields"]["postal_code"])
            event["time_start"] = "2020-01-15T02:29:56.647Z"
            event["time_end"] = "2020-01-15T02:29:56.647Z"
            events_toreturn.append( event )
        elif x == "Food":
            e = urllib.request.urlopen("https://www.mapquestapi.com/search/v2/radius?origin={}&radius=5&maxMatches=3&ambiguities=ignore&hostedData=mqap.ntpois|group_sic_code=?|581208&outFormat=json&key=yNjXSwjvcoWeXAoUiJw9AZG6MiUvjX8f".format(origin))
            e = json.loads( e.read() )
            mapquest_event = random.choice( e["searchResults"] )
            print("--- FOOD ---")
            print(mapquest_event)
            print("--- ENDFOOD---")

            event = {}
            event["name"] = mapquest_event["name"]
            event["address"] = "{}, {}, {}, {}, {}".format( mapquest_event["name"], mapquest_event["fields"]["address"], mapquest_event["fields"]["city"], mapquest_event["fields"]["state"], mapquest_event["fields"]["postal_code"])
            event["time_start"] = "2020-01-15T02:29:56.647Z"
            event["time_end"] = "2020-01-15T02:29:56.647Z"
            events_toreturn.append( event )
        else:
            return json.dumps({"error":"invalid event input"})
    return events_toreturn



if __name__ == "__main__":
    db = SQLHandler("data.db")
    db.run("CREATE TABLE IF NOT EXISTS loginfo (username TEXT, password TEXT);")
    app.debug = True
    app.run()
