# gcc ./payload.c -shared -Wl,--version-script,payload.map -o ./payload && gcc ./exploit.c -o ./exploit && gcc ./readme.c -o ./readme && gcc ./run.c -o ./run && timeout 5 docker run --name wow --privileged --network=none --rm -v `pwd`/payload:/tmp/payload -v `pwd`/exploit:/tmp/exploit -v `pwd`/run:/home/pwn/run -v `pwd`/readme:/home/pwn/readme -ti ubuntu:22.04 bash -c 'chmod +x /tmp/exploit && chown root /home/pwn/* -R && chmod 111 /home/pwn/readme;chmod u+s /home/pwn/readme;useradd pwn; chmod +x /home/pwn/run;/home/pwn/run;'