import json
import boto3
import os


def hello(event, context):
   
    l=[]
    client = boto3.client('s3')
    src_bucket_name =os.environ['source']
    #src_object_name = 'Persistent_logo.png'
    dest_bucket_name = os.environ['desti']
    #dest_object_name = 'DEST_OBJECT_NAME'
    response = client.list_objects(
    Bucket=src_bucket_name)
    if 'Contents' in response.keys(): 
        #print("Present, ", end =" ") 
        #print("value =", dict[key])
        try:
          response = client.list_objects(Bucket=src_bucket_name )['Contents']
          for b in response :
            l.append((b["Key"]))
          length = len(l)
          for i in range(length):
            src_object_name =l[i]
            copy_source = {'Bucket': src_bucket_name, 'Key': src_object_name}
            dest_object_name = src_object_name
            client.copy_object(CopySource=copy_source, Bucket=dest_bucket_name,
                       Key=dest_object_name)
            client.delete_object(Bucket=src_bucket_name, Key=src_object_name)
        except ClientError as e:
          logging.error(e)
          return False
        return ("all objects are copied to",dest_bucket_name )
    else: 
        print("Not present")
        return ('source bucket is empty')

    
    
   


