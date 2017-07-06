######################################################
# DATA MODELS
######################################################

# For an ORMish for DynamoDB
import riak

rClient = riak.RiakClient(pb_port=8087)

class RiakModel ():
  
  def __init__(self, **kwargs):
    # Hopefully this is the child class...
    self.bucket = rClient.bucket(type(self).__name__)
    # We have to init with keyword args.
    for k, v in kwargs.items():
  		setattr(self, k, v)
  
  def set_keys(self, keys=[]):
    self.__keys = keys
        
  def save ():
    keys = self.__dict__.keys()
    print ("Saving keys: %s" % keys)
    obj = self.bucket.new(__keys.join(), keys)
    obj.store()

class Item (RiakModel):
  # What do you do with the child now?
  pass
    
  
# There really isn't a notion of a primary key.
# If you want one, you need to track it.
# See:
# http://stackoverflow.com/questions/11721308/how-to-make-a-uuid-in-dynamodb
# itemid = NumberAttribute(hash_key=True)

