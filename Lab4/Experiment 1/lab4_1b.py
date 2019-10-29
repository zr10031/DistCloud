"""
Lab 4: 1b
Starting and Stopping Monitoring
"""
import sys
import boto3
ec2 = boto3.client('ec2')
if(sys.argv[1] == 'ON'):
    response = ec2.monitor_instances(InstanceIds=['i-09842b80b247b5eef'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-09842b80b247b5eef'])
print(response)