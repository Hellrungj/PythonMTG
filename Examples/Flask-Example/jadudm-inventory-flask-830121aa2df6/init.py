######################################################
# APPLICATION GLOBALS
######################################################

# FIXME: None of these are used.
# This is essentially cruft.

# These are globals that we use throughout the 
# application. They need to be imported.

# Boto3 for AWS/DynamoDB
#import boto3
#from boto3.dynamodb.conditions import Key, Attr

# Private
dynamodb = boto3.resource('dynamodb')

# Public
table = dynamodb.Table('Inventory')

