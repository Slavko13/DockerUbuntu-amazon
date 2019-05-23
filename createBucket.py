import boto3, os, time

AWS_DEFAULT_REGION = "eu-west-1" #Region where Lambda running
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION

bucketname = "lambda.create.me.on-" + str(time.time())

def lambda_handler(event, context):
    
    myS3 = boto3.resource('s3')
    try:
     results = myS3.create_bucket(
           Bucket= bucketname,
           CreateBucketConfiguration = {'LocationConstraint':AWS_DEFAULT_REGION}
           )
     return ("<h1><font color=green>S3 Bucket Created Successfully:</font></h1><br><br>" + str(results))
    except:
     return ("<h1><font color=red>Error!</font></h1><br><br>")
