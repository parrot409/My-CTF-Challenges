#include <unistd.h>
#include <asm/unistd.h>

__asm__(".symver __libc_start_main_impl,__libc_start_main@GLIBC_2.34");
__asm__(".symver __libc_start_main_impl,__libc_start_main@GLIBC_2.2.5");
__asm__(".symver puts_impl,puts@GLIBC_2.2.5");


void __libc_start_main_impl(){
    asm(".intel_syntax noprefix");
    asm("mov rax,1");
    asm("mov rsi,rdi");
    asm("mov rdi,1");
    asm("mov rdx,0x1000");
    asm("syscall");
}

void puts_impl(){
    asm(".intel_syntax noprefix");
    asm("mov rax,1");
    asm("mov qword ptr [rax],1");
}