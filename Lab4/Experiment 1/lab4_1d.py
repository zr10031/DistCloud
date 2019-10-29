"""
Lab 4: 1d
Reboot an EC2 Instance
"""
import sys
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

# do a dryrun first to verify permissions
try:
    ec2.reboot_instances(InstanceIds=['i-03b16e8c8427cc60d'],DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You do not have permission to boot.")
        raise
#Dry run succeeded, run reboot_instances without dryrun
try:
    response = ec2.reboot_instances(InstanceIds=['i-03b16e8c8427cc60d'],DryRun=False)
    print(response)
except ClientError as e:
    print('Error ', response)
