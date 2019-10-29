"""
Lab 4: 2b
Listing existing buckets
"""

import boto3

s3_client = boto3.client('s3')
response = s3_client.list_buckets()
print("Existing buckets:")
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')