#!/usr/bin/env python3
from flask import Flask,Response,request,redirect
import secrets
import re
import subprocess
import pty
import os
import hashlib

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 0x100

@app.route('/')
def index(): #Poor coding skills :( can't even get process output properly
	url = request.args.get('url') or "http://localhost:8000/sayhi"
	env = request.args.get('env') or None
	outputFilename = request.args.get('file') or "myregrets.txt"
	outputFolder = f"./outputs/{hashlib.md5(request.remote_addr.encode()).hexdigest()}"
	result = ""

	if(env):
		env = env.split("=")
		env = {env[0]:env[1]}
	else:
		env = {}

	master, slave = pty.openpty()
	os.set_blocking(master,False)
	try:
		subprocess.run(["/usr/bin/curl","--url",url],stdin=slave,stdout=slave,env=env,timeout=3,)
		result = os.read(master,0x4000)
	except:
		os.close(slave)
		os.close(master)
		return '??',200,{'content-type':'text/plain;charset=utf-8'}

	os.close(slave)
	os.close(master)

	if(not os.path.exists(outputFolder)):
		os.mkdir(outputFolder)

	if("/" in outputFilename):
		outputFilename = secrets.token_urlsafe(0x10)

	with open(f"{outputFolder}/{outputFilename}","wb") as f:
		f.write(result)

	return redirect(f"/view?file={outputFilename}", code=302)

@app.route('/view')
def view():
	outputFolder = f"./outputs/{hashlib.md5(request.remote_addr.encode()).hexdigest()}"
	outputFilename = request.args.get('file')

	if(not outputFilename or "/" in outputFilename or not os.path.exists(f'{outputFolder}/{outputFilename}')):
		return '???',404,{'content-type':'text/plain;charset=utf-8'}

	with open(f'{outputFolder}/{outputFilename}','rb') as f: 
		return f.read(),200,{'content-type':'text/plain;charset=utf-8'}


@app.route('/sayhi')
def sayhi():
	return 'hi hacker ヾ(＾-＾)ノ',200,{'content-type':'text/plain;charset=utf-8'}

app.run(host='0.0.0.0', port=8000)