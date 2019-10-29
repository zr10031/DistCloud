"""
Lab 4: 3b
Adding an item
"""

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('zcr006')

table.put_item(
   Item={
        'username': 'zcr006',
        'last_name': 'Rogers'})
table.meta.client.get_waiter('table_exists').wait(TableName='zcr006')
