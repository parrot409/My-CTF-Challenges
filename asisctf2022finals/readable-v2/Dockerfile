FROM ubuntu:22.04@sha256:27cb6e6ccef575a4698b66f5de06c7ecd61589132d5a91d098f7f3f9285415a9
COPY ./stuff/readme /home/pwn/readme
COPY ./stuff/run /home/pwn/run
RUN chown -R root /home/pwn/*   
RUN chmod +x /home/pwn/run; 
RUN chmod 111 /home/pwn/readme;
RUN chmod u+s /home/pwn/readme;
RUN useradd pwn;
CMD ["/bin/bash","-c","while true;do /home/pwn/run /tmp/exploit; done;"];
