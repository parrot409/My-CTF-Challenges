#!/bin/bash

gcc ./exploit.c -o ./exploit
gcc ./payload.c -shared -Wl,--version-script,payload.map -o ./payload
gcc ./exploit2.c -o ./exploit2

./solve.py