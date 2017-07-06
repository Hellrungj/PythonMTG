import aerospike
import uuid
import base64


config = {
  'hosts': [ ('127.0.0.1', 3000) ]
}

try:
    client = aerospike.client(config).connect()
except:
    import sys
    print("failed to connect to the cluster with", config['hosts'])
    sys.exit(1)

class Aero (object):
    def __init__ (self, ns = 'default', **kwargs):
        global config
        for k, v in kwargs.items():
            # print ("Setting {0}[{1}]".format(k, v))
      	    setattr(self, k, v)
        #print ("ns: %s" % ns)
        #self.client = aerospike.client(config)
        self.ns = ns
        # Our set will be the class name
        self.set = type(self).__name__

    def namespace (self, ns):
        self.ns = ns

    def save (self):
        global client

        uid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
        print ("UID: %s" % uid)

        fields = self.__dict__.keys()
        # Remove keys we don't want saved.
        for k in ['ns', 'set', 'client']:
            print ("Removing %s" % k)
            if k in fields:
                fields.remove(k)

        print ("Saving keys: %s" % fields)
        print ("ns: %s" % self.ns)

        key = (self.ns, self.set, uid)
        value = {}
        for k in fields:
            value[k] = self.__dict__[k]

        # print ("key: {0} value: {1}".format(key, value))
        client.put (key, value)
        # teardown()

    def scan (self, bin):
        global client
        self.scanner = client.scan(self.ns, self.set)
        return self.scanner.select(bin)


class Item(Aero):
    pass




i = Item ('inventory', a = 1, b = 2)
i.save()

results = i.scan ('b')

def print_result((key, metadata, record)):
    print(key, record)

results.foreach(print_result)
