######################################################
# DATA MODELS
######################################################

# For an ORMish for DynamoDB
from CodernityDB.database import Database
from CodernityDB.hash_index import HashIndex


db = Database('/tmp/tut1')
db.create()


# Item class
class Item():
    name   = UnicodeAttribute()
    value  = UnicodeAttribute()
    count  = NumberAttribute()


# There really isn't a notion of a primary key.
# If you want one, you need to track it.
# See:
# http://stackoverflow.com/questions/11721308/how-to-make-a-uuid-in-dynamodb
# itemid = NumberAttribute(hash_key=True)

