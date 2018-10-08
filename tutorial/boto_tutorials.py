#!/home/ubuntu/anaconda2/envs/p3/bin/python

'''!/usr/bin/python3: This code uploads the following formated json to elastic search:  
'''

import boto3              # 
import json     	      # build-in package
import sys			      # sys.argv()
import subprocess         # run shell scripts in python
import argparse
import pyspark
from pyspark import SparkContext, SparkConf
from pprint import pprint 
#from boto.s3.connection import S3Connection

BUCKET_NAME = "stack-overflow-s3-bucker"
FILE_NAME   = "stackoverflow.com-PostLinks"  

def distributedJsonRead(s3Key):
    s3obj = boto3.resource('s3').Object(bucket_name=BUCKET_NAME, key=s3Key)
    contents = json.loads(s3obj.get()['Body'].read().decode('utf-8'))
    for dicts in content['interactions']:
        yield Row(**dicts)

def main():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)                      # prints out bucket names

    ec2 = boto3.client('ec2')
    response = ec2.describe_key_pairs()
    print(json.dumps(response, indent=2))       # prints out key pairs

    # prints out the contents of S3 bucket
    #s3 = boto3.client('s3')
    #contents = s3.list_objects_v2(Bucket=BUCKET_NAME)           # all contents of S3 bucket  
    #for files in contents['Contents']:                          # loops over files in S3 bucket              
    #    print(files['Key'])
        #if files['Key'] == 'stackoverflow.com-PostLinks':       # finds the file of interest = Key
        #    print(files)

    sc = SparkContext()
    #pkeys = sc.parallelize()             # keyList is a list of s3 keys
    #print(pkeys)
    #dataRdd = pkeys.flatMap(distributedJsonRead)

    s3obj = boto3.resource('s3').Object(bucket_name=BUCKET_NAME, key=FILE_NAME)
    contents = s3obj.get()['Body'].read().decode('utf-8')
    sc.parallelize(contents)






'''def main():
    # Use argparse to handle some argument parsing
    parser.add_argument("-a",
                        "--aws_access_key_id",
                        help="AWS_ACCESS_KEY_ID, omit to use env settings",
                        default=None)
    parser.add_argument("-s",
                        "--aws_secret_access_key",
                        help="AWS_SECRET_ACCESS_KEY, omit to use env settings",
                        default=None)
    parser.add_argument("-b",
                        "--bucket_name",
                        help="AWS bucket name",
                        default="spirent-orion")
    # Use Boto to connect to S3 and get a list of objects from a bucket
    conn = S3Connection(args.aws_access_key_id, args.aws_secret_access_key)
    bucket = conn.get_bucket(args.bucket_name)
    keys = bucket.list()
    # Get a Spark context and use it to parallelize the keys
    conf = SparkConf().setAppName("MyFileProcessingApp")
    sc = SparkContext(conf=conf)
    pkeys = sc.parallelize(keys)
    # Call the map step to handle reading in the file contents
    activation = pkeys.flatMap(map_func)
    # Additional map or reduce steps go here...

def map_func(key)
    # Use the key to read in the file contents, split on line endings
    for line in key.get_contents_as_string().splitlines():
        # parse one line of json
        j = json.loads(line)
        if "user_id" in j && "event" in j:
            if j['event'] == "event_we_care_about":
                yield j['user_id'], j['event']
'''

if __name__  == "__main__":
    main()
