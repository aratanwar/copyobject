import json
import boto3
import os
import urllib

def eventTrigger(event, context):
    Bucket_Name= event['Records'][0]['s3']['bucket']['name']
    print (Bucket_Name)
    object_Name=event['Records'][0]['s3']['object']['key']
    print (object_Name)
    return Bucket_Name,object_Name
