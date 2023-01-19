BITS 64
path  db  '/home/pwn/readme',0 ;
_start:
	mov rdi,path
	mov rsi,0
	mov rdx,0
	mov rax,59
	syscall
	mov rax,60
	syscall
global _start
