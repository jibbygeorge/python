
#Read the IAM policy from s3 bucket. policy.json is a file in s3 bucket
import boto3
import json



s3 = boto3.resource('s3')
bucket = s3.Bucket('melbourne2017')
for obj in bucket.objects.filter(Prefix='policy.json'):
	print obj.key
	body = obj.get()['Body'].read()
	content = json.loads(body)

	#a  = type(content)
	#print a

	print body


   
	print "\n"
   	print content['Statement'][0]['Resource']
   	#print content['Statement'][1]['Resource'][0]

	