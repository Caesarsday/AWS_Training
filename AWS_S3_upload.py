##upload files to s3
import boto3
from boto3.session import Session
aws_key=""
aws_secret = ""
session=Session(aws_access_key_id=aws_key, aws_secret_access_key=aws_secret,
                region_name="us-east-2")
s3=session.resource("s3")
#client=session.client("s3")
bucket="s3functionstraining"
upload_data=open("z:/Pycharm/file/DATA/s3_test.txt","rb")
upload_key="test.txt"
file_obj = s3.Bucket(bucket).put_object(Key=upload_key, Body=upload_data)





#fast way to find out if a file exists in s3
from boto3.session import Session
import botocore
from botocore.exceptions import ClientError
aws_key=""
aws_secret = ""
session=Session(aws_access_key_id=aws_key, aws_secret_access_key=aws_secret,
                region_name="us-east-1")
s3=session.resource("s3")
bucket_name="s3functionstraining"
bucket = s3.Bucket(bucket_name)
key="test.txt"
exist=False
try:
    s3.Object(bucket_name,key).get()
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        exist = False
    else:
        raise
else:
    exist = True

print(exist)


