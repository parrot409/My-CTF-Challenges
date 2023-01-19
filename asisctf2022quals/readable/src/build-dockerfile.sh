#!/bin/bash
mkdir stuff 2>/dev/null
gcc ./sources/readme.c -o ./stuff/readme;
gcc ./sources/run.c -o ./stuff/run;
nasm -f elf64 ./sources/run.asm
ld -m elf_x86_64 -s -o ./stuff/runsuid ./sources/run.o
docker build . -t readable
