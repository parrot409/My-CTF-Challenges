CNAME response can contain slashes so you can hit the internal endpoint!

The trick to read the response from the flag server is that you have to pad your response to 1024*1024 characters and then append the flag at the end of the response. The response is sliced so the response can have your known body plus the first char of flag. 

