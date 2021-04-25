FROM ubuntu:20.10
MAINTAINER parrot
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install xinetd -y
RUN useradd -m manga_store
RUN chmod 774 /tmp
RUN chmod -R 774 /var/tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN chown -R root:root /home/manga_store
CMD ["/usr/sbin/xinetd","-dontfork"]
