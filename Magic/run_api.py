import os
import json
from flask import render_template, request,Flask, redirect
from mtgsdk import Card

app = Flask(__name__)

@app.route("/")
def Home():
  return(render_template('index.html', DATA = None))

@app.route("/search/name=<name>", methods = ['POST', 'GET'])
@app.route("/search/colors=<colors>", methods = ['POST', 'GET'])
@app.route("/search/cost=<cost>", methods = ['POST', 'GET'])
@app.route("/search/name=<name>&colors=<colors>", methods = ['POST', 'GET'])
@app.route("/search/name=<name>&cost=<cost>", methods = ['POST', 'GET'])
@app.route("/search/colors=<colors>&colors=<cost>", methods = ['POST', 'GET'])
@app.route("/search/name=<name>&colors=<colors>&colors=<cost>", methods = ['POST', 'GET'])
def Search(name=" ",colors=" ",cost =" "):
  try:
    if request.method == 'POST':
      if len(request.form['name']) != 0 and len(request.form['colors']) != 0 and len(request.form['type']) != 0:
        return(redirect("/search/name={0}&colors={1}&type={2}".format(request.form['name'],request.form['colors'],request.form['type'])))
      elif len(request.form['name']) != 0 and len(request.form['colors']) != 0:
        return(redirect("/search/name={0}&colors={1}".format(request.form['name'],request.form['colors'])))
      elif len(request.form['name']) != 0:
        return(redirect("/search/name={0}".format(request.form['name'])))
      elif len(request.form['colors']) != 0:
        return(redirect("/search/colors={0}".format(request.form['colors'])))
      elif len(request.form['type']) != 0:
        return(redirect("/search/colors={0}".format(request.form['type'])))
      else:
        return "404"
  # By redirecting to the GET, we guarantee bookmarkable search results.
    elif request.method == 'GET':
      cards = Card.where(name = name).where(colors = colors).where(mana_cost = cost).where(page=1).where(pageSize=10).all()
      #ListOfName = []
      #for i in range(len(cards)):
      #    ListOfName.append(str(cards[i].name))
      return(render_template('index.html', DATA = cards))
    else:
    # FIXME: Return a proper error message here.
      return "404"
  except e:
    return("{}.".format(str(e)))

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