######################################################
# IMPORTS
######################################################
import os
# Python 2/3 compat
#from __future__ import print_function

# import the Flask class from the flask module
from flask import Flask, render_template, redirect, request, url_for

# Other Imports
from random import randint

# Data models
# from pynamo_models import Item
#from codernity_models import Item

# PeeWee Import
from peewee import *

# Define the DB object.
# Takes the filename. We'll pull this out into a config file
# for the actual app. This is OK for testing for now.
db = SqliteDatabase('inventorydb.sqlite')

# Now, define a class representing the fields of our database.
class Stuffs (Model):
  uid         = PrimaryKeyField()
  name        = TextField()
  value       = TextField()
  count       = IntegerField()

  class Meta:
    database = db


# FLASK INIT
app   = Flask(__name__)

def redirect_to_morethan_0 ():
  return redirect(url_for('morethan', cnt = 0), code=302)

######################################################
# ROUTE: /
# Action:
# The root route reroutes you to a view of the inventory.
# Specifically, it shows us everything we have
# more than zero of. Note the use of url_for, which essentially
# makes sure we call the function for the handler correctly,
# with the parameters in the URL even!
@app.route('/')
def home():
    return redirect_to_morethan_0 ()

######################################################
# ROUTE: /morethan/<int:count>
# METHODS: GET
# Action:
# Updates the inventory search results to show items
# where we have more than the number given.
@app.route('/morethan/<int:cnt>')
def morethan (cnt):
  # We scan all of the items, finding ones that have a 
  # count greater than the value of the variable 'cnt'.
  # response = Item.scan(count__gt = cnt)
  response = Stuffs.select().where(Stuffs.count > cnt)
  # Render the search results, passing the list of items
  # that we found in our scan.
  return render_template('searchresults.html', items = response)

######################################################
# ROUTE: /contains/<name>
# METHODS: POST, GET
# Action:
# This takes a GET URL prefaced with /contains, and searches
# the name fields of the Items for any that contain the last part
# of the URL. This becomes the search results list on the main page.
# The side effect of this interface is that we can bookmark
# searches of the database.
@app.route('/contains/<search_string>', methods = ['POST', 'GET'])
def contains (search_string):
  # If they did a post, then just redirect to the GET version
  # The FORM on the page does a POST, so we handle this here
  # in this way.
  if request.method == 'POST':
    return redirect("/contains/{0}".format(request.form['name']))
  # By redirecting to the GET, we guarantee bookmarkable search results.
  elif request.method == 'GET':
    search_result = Stuffs.select().where(Stuffs.name.contains(search_string))
    return render_template('searchresults.html', items = search_result)
  else:
    # FIXME: Return a proper error message here.
    return "404"

######################################################
# ROUTE: /insert
# METHODS: POST
# Action:
# Does an insert into the database. No fancy URL here,
# because we do not want to accidentally bookmark a URL and
# end up with a way to have too many of one item in the DB.
@app.route('/insert', methods = ['POST'])
def insert ():
  # This only handles POST requests.
  if request.method == 'POST':
    n  = request.form['name']
    v = request.form['value']
    c = int(request.form['count'])
    # Field name = variable
    stuff = Stuffs(name = n, value = v, count = c)
    stuff.save()
    return redirect_to_morethan_0 ()
  else:
    # FIXME: Properly handle other request types.
    return "404"

# start the server with the 'run()' method
# Builds the server configuration
if os.getenv('IP'):
  IP    = os.getenv('IP')
else:
  IP    = '0.0.0.0'

if os.getenv('PORT'):
  PORT  = int(os.getenv('PORT'))
else:
  PORT  = 8080

# Print statements go to your log file in production; to your console while developing
print ("Running server at http://{0}:{1}/".format(IP, PORT))
app.run(host = IP, port = PORT, debug = True, threaded = True)