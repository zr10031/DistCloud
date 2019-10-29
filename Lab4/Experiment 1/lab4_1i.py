"""
Lab 4: 1i
Create a new security group
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.create_security_group(Description='Test group for Lab 4.', GroupName='zcr006SecGroup')
    print(response)
except ClientError as e:
    print(e)