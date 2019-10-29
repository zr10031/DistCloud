"""
Lab 4: 3f
Deleting a table
"""

import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('zcr006')
table.delete()