"""
Lab 4: 1h
Informs on one security group
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['sg-01050fceecc09b78a'])
    print(response)
except ClientError as e:
    print(e)