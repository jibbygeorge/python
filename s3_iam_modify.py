
#Read the IAM policy from s3 bucket.
import boto3
import json

new_acct = "arn:aws:s3:::acxsynctest6,"

s3 = boto3.resource('s3')
bucket = s3.Bucket('melbourne2017')
for obj in bucket.objects.filter(Prefix='policy.json'):
	
	file = open('policy.json', 'r')
	data = json.load(file)
	file.close()

	print "\n"

	data = data['Statement'][0]['Resource'][1] + "".join(new_acct)
	#policy['Statement'][0]['Resource'].insert(1,"arn:aws:s3:::{0},".format(account)) 

	print data


	'''



	tmp = []
	tmp = data['Statement'][0]['Resource']
	tmp.append(new_acct)
	print tmp

	print '\n'
	

	file = open('policy.json', 'w+')
	file.write(json.dumps(data))
	file.close()


	
	print obj.key
	body = obj.get()['Body'].read()
	data = json.loads(body)

	print data
	
	print "\n"
	print data['Statement'][0]['Resource']
	'''


'''
#Upload the file
testfile = "replace this with an actual filename"
s3.Bucket('melbourne2017').upload_file('testfile', 'testfile')

#replaces the polciy on a bucket

response = bucket_policy.put(
    Policy='string'
)

'''