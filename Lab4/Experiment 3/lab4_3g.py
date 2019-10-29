"""
Lab 4: 3g
Query and Scan in tables
"""

import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('zcr006')

print("Query:")
response = table.query(
    KeyConditionExpression=Key('username').eq('user2'))
items = response['Items']
print(items)

print("Scan:")
response = table.scan(
    FilterExpression=Attr('age').lt(25)
)
items = response['Items']
print(items)