Run both scripts at the same time

The solution uses the REQUEST_BODY_FILE env and race condition to read other process's /proc/$/mem. 
