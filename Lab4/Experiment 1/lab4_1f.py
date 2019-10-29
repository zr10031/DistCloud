"""
Lab 4: 1f
Creating a new key pair
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName='zcr006lab4')
print(response)