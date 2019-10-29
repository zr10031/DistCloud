"""
Lab 4: 1j
Delete a security group
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.delete_security_group(GroupId='sg-056493a16f1b5f958')
    print(response)
except ClientError as e:
    print(e)