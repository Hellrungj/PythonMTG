######################################################
# DATA MODELS
######################################################

# For an ORMish for DynamoDB
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

# Item class
class Item(Model):
    """
    An Inventory Item
    """
    class Meta:
        table_name = 'Inventory'
        region = 'us-east-1'
    name   = UnicodeAttribute()
    value  = UnicodeAttribute()
    count  = NumberAttribute()


# There really isn't a notion of a primary key.
# If you want one, you need to track it.
# See:
# http://stackoverflow.com/questions/11721308/how-to-make-a-uuid-in-dynamodb
# itemid = NumberAttribute(hash_key=True)

