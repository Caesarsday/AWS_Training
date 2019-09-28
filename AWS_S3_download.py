##first way to download files from s3
import boto3
from boto3.session import Session
aws_key=""
aws_secret = ""
session=Session(aws_access_key_id=aws_key, aws_secret_access_key=aws_secret,
                region_name="us-east-2")
s3=session.resource("s3")
bucket_name = 's3functionstraining'
file_name = 'test.txt'
local_file_name = 'z:/Pycharm/file/DATA/test1.txt'
s3.Bucket(bucket_name).download_file(file_name,local_file_name)




##second way to download file from s3
from boto3.session import Session
import boto3
aws_key=""
aws_secret = ""
session=Session(aws_access_key_id=aws_key, aws_secret_access_key=aws_secret,
                region_name="us-east-2")
s3 = session.resource('s3')
bucket_name = s3.Bucket('s3functionstraining')
key='test.txt'
filename= 'z:/Pycharm/file/DATA/test2.txt'
bucket_name.download_file(key,filename)




##download all the files in the bucket without folder
import boto3
s3=boto3.client(
's3',
aws_access_key_id="",
aws_secret_access_key= "",
region_name="us-east-2")
list=s3.list_objects(Bucket='s3functionstraining')['Contents']
for key in list:
    s3.download_file('s3functionstraining',key['Key'],key['Key'])



#download all files and folders in the bucket
import boto3
s3=boto3.client(
's3',
aws_access_key_id="",
aws_secret_access_key= "",
region_name="us-east-2")
list=s3.list_objects(Bucket='s3functionstraining')['Contents']
for s3_key in list:
    s3_object=s3_key['Key']
    if not s3_object.endswith('/'):
        s3.download_file('s3functionstraining',s3_object,s3_object)
    else:
        import os
        if not os.path.exists(s3_object):
            os.makedirs(s3_object)
