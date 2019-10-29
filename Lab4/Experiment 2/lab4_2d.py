"""
Lab 4: 2d
Downloading files from a bucket
"""

import boto3
import botocore
s3 = boto3.resource('s3')
key='README.md'
filename = 'myREADME.md'
bucket_name = 'zcrlabbuc'
s3.Bucket(bucket_name).download_file(key,filename)