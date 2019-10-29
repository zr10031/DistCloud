"""
Lab 4: 1e
Informs on current key pair(s)
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
print(response)
