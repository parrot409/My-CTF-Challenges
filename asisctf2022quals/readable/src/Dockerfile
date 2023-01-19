FROM ubuntu:22.04

COPY ./stuff/readme /home/pwn/readme
COPY ./stuff/run /home/pwn/run
COPY ./stuff/runsuid /home/pwn/runsuid
RUN chown -R root /home/pwn/*   
RUN chmod +x /home/pwn/run; 

RUN chmod 111 /home/pwn/runsuid;
RUN chmod 100 /home/pwn/readme;
RUN chmod u+s /home/pwn/runsuid;

RUN useradd pwn;
CMD ["/home/pwn/run"];