"""
Lab 4: 2c
Uploading files to a bucket
"""

import boto3
s3_client = boto3.client('s3')
filename = 'README.md'
bucket_name = 'zcrlabbuc'
s3_client.upload_file(filename,bucket_name,filename)
