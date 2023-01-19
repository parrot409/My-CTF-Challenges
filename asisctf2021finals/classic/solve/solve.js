#!/usr/bin/env node
const express = require('express')
const app = express()

app.get('/video',(req,res)=>{
	console.log("VIDEO")
	res.setHeader('Cache-Control','max-age=904800')
	res.sendFile('./test.mp4',{root:'.'})
})

app.get('/',(req,res)=>{
	console.log("COME")
	res.sendFile('./solve.html',{root:'.'})
})

app.get('/hit',(req,res)=>{
	console.log(req.query.wow,req.query.wow2)
	res.send("A")
})

app.listen(9001)