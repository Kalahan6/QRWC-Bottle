
import bottle
from replit import db

db["TestKeyName"] = "hans"
db["TestKeyName"] = "john"
value = db["TestKeyName"]
keys = db.keys()


#this is the main page
@bottle.route('/') 
def index():
  return 'You can write html here'


#bottle.run(host='0.0.0.0', port=1234)