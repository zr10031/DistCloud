"""
Lab 4: 3c
Recieving an item
"""

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('zcr006')

response = table.get_item(
    Key={
        'username': 'zcr006',
        'last_name': 'Rogers'
    }
)
item = response['Item']
print(item)