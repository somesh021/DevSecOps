# Validates the payload, making sure the “Age” ﬁeld is between 50 and 100. 
# Saves the json to S3 if it has been validated (using the “Id” ﬁeld as ﬁle name). 


import json
import boto3

# Bucket is already created by TF code. 
bucketName = "python-store-output-in-bucket"

#Creating client connection with s3 service to push payload data to bucket
s3 = boto3.resource('s3')

# Samepl payload={"Id": 123456, "Age": 70, "Sex": "male"} 


def createBucket(bucketName,event):
    fileName = event['Id']
    obj = s3.Object(bucketName,str(event['Id'])+'.json')
    obj.put(Body=json.dumps(event))
    

def lambda_handler(event, context):
    # TODO implement
    # Age = event['Age']
    # if Age >= 50 and Age <= 100:
    if event['Age'] >= 50 and event['Age'] <= 100:
        createBucket(bucketName,event)
        print("The object is created with {}.json name in bucket {}".format(event['Id'],bucketName))
    else:
        print("This is wrong {} age".format(event['Age']))
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
    