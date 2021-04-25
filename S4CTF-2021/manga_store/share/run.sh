#!/bin/bash

exec 2>/dev/null
/home/manga_store/ld-2.31.so --preload /home/manga_store/libc.so.6 /home/manga_store/manga_store 
