"""
Lab 4: 3f
Batch writing to a file
"""

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('zcr006')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'username': 'user1',
            'last_name': 'last1',
            'age': 19})
    batch.put_item(
        Item={
            'username': 'user1',
            'last_name': 'last2',
            'age': 22})
    batch.put_item(
        Item={
            'username': 'user2',
            'last_name': 'last1',
            'age': 25})
    batch.put_item(
        Item={
            'username': 'user2',
            'last_name': 'last2',
            'age': 39})