#!/bin/bash
gcc ./payload.c -shared -Wl,--version-script,payload.map -o ./payload
gcc ./exploit.c -o ./exploit

