"""
Lab 4: 1c
Starting and Stopping an EC2 Instance
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
action = sys.argv[1].upper()
if(action == 'ON'):
    # do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=['i-03b16e8c8427cc60d'],DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=['i-03b16e8c8427cc60d'],DryRun=False)
        print(response)
    except ClientError as e:
        print(response)
else:
    # do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=['i-03b16e8c8427cc60d'],DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    #Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=['i-03b16e8c8427cc60d'],DryRun=False)
        print(response)
    except ClientError as e:
        print(response)
