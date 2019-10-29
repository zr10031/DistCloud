"""
Lab 4: 2g
Get bucket access control list
"""

import boto3
import json
bucket_name = 'zcrlabbuc'
s3 = boto3.client('s3')
response = s3.get_bucket_acl(Bucket=bucket_name)
print(response)