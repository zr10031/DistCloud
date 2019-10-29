"""
Lab 4: 3d
Updating an item
"""

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('zcr006')

table.update_item(
    Key={
        'username': 'zr10031',
        'last_name': 'Rogers'})