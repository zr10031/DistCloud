"""
Lab 4: 2e
Temporary access with presigned URLs
"""

import boto3
s3 = boto3.client('s3')


key='README.md'
filename = 'myREADME.md'
bucket_name = 'zcrlabbuc'
response = s3.generate_presigned_url(ClientMethod='get_object',Params={
    'Bucket' : bucket_name,
    'Key' : key})
print(response)