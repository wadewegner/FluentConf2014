import requests
import json
import base64

consumer_key = base64.b64decode("M01WRzlBMmtOM0JuMTdoc0V5TXFSVFRhRWZmWWN0ZG9oME1hMW03YlpGenJDZ0pzR2RHMHZGanEzcHlOMnBJMEFkSHVrX2RIQ1FFanZjLlFRWXBXWQ==")
consumer_secret = base64.b64decode("NDIyMzM1MTQzNzYxMDg4ODIwNA==")
username = base64.b64decode("ZGVtb0BzZmRjYXBpLmNvbQ==")
password = base64.b64decode("UGEkJHcwcmQh")

payload = {
    'grant_type': 'password',
    'client_id': consumer_key,
    'client_secret': consumer_secret,
    'username': username,
    'password': password
}

r = requests.post("https://login.salesforce.com/services/oauth2/token", 
    headers={"Content-Type":"application/x-www-form-urlencoded"},
    data=payload)

token = json.loads(r.content)
access_token = token[u'access_token']
instance_url = token[u'instance_url']

print ""
print "Access Token: " + access_token
print "Instance URL: " + instance_url
print ""

object_name = "Widget__c"
payload = {"Name":"New Widget from Python"}

r = requests.post(instance_url + "/services/data/v29.0/sobjects/" + object_name,
	headers={"Content-Type":"application/json",
		"Authorization":"Bearer " + access_token},
	data=json.dumps(payload))

print r.content