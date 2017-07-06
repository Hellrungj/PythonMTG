# Source this.
# Setup virtualenv
if [ ! -d venv ]
then
  virtualenv venv
fi

. venv/bin/activate

pip install Flask
#pip install boto3
#pip install pynamodb
# pip install CodernityDB
# pip install riak
#pip install aerospike
pip install peewee

