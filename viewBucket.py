import boto3, os

def lambda_handler(event, context):
    myS3 = boto3.client('s3')
    try:
     results = myS3.list_buckets()
     print(results)
     output = ""
     for bucket in results['Buckets']:
      output = output + bucket['Name'] + "<br>"
     return ("<h1><font color=green>S3 Bucket List:</font></h1><br><br>" + output)
    except:
     return ("<h1><font color=Error!</font></h1><br><br>" )
