#!/bin/bash

exec 2>/dev/null
timeout 60 /home/heap_heap/ld-2.31.so --preload /home/heap_heap/libc.so.6 /home/heap_heap/heap_heap 
