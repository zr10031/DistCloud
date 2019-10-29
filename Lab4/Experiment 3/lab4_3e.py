"""
Lab 4: 3e
Deleting an item
"""

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('zcr006')

table.delete_item(
    Key={
        'username': 'zcr006',
        'last_name': 'Rogers'})
