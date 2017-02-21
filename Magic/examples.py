import os
import json
from flask import *
from mtgsdk import Card

app = Flask(__name__)

@app.route("/")
def search():
    name = request.form['name']
    cards = Card.where(name = name).all()
    ListOfName = []
    for i in range(len(cards)):
        ListOfName.append(cards[i].name)
    return(render_template('index.html'))
    

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