
#Read the IAM policy from s3 bucket
#import boto3
#dumps takes an object and produces a string:
#load string to object(dict)



import json

new_acct = "arn:aws:s3:::acxsynctest3,"


file = open('policy.json', 'r')
data = json.load(file)

file.close()

print data

print "\n"

print data['Statement'][0]['Resource']


tmp = data['Statement'][0]['Resource']
	

tmp.append(new_acct)

print tmp

print '\n'

file = open('policy.json', 'w')
file.write(json.dumps(data))
file.close()

'''



data['Statement'][0]['Resource'][2] = "new_acct"

print data['Statement'][0]['Resource'][2]


with open('policy.json') as f:
	data = json.load(f)
	print data['Statement'][0]['Resource']

#data.update(a_dict)

with open('test.json', 'w') as f:
    json.dump(data, f)
'''



