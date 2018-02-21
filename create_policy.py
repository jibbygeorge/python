# Create Policy and print with indendation
import json

account = "1111111111"

policy = { 'Version' : '2012-10-17'}
policy['Statement'] = [{"Effect": "Allow",
                          "Action": ["s3:ListBucket"],
                          "Resource": ["arn:aws:s3:::acxsynctest","arn:aws:s3:::acxsynctest3"]
                        },
                         {"Effect": "Allow",

                          "Action": ["s3:PutObject","s3:GetObject","s3:DeleteObject"],
                          "Resource": ["arn:aws:s3:::acxsynctest/*"]}]

policy['Statement'][0]['Resource'].insert(1,"arn:aws:s3:::{0},".format(account)) 

policy_json = json.dumps(policy, indent=2)

print (policy_json)