#define _GNU_SOURCE
#include <errno.h>
#include <fcntl.h>
#include <limits.h>
#include <linux/audit.h>
#include <linux/filter.h>
#include <linux/seccomp.h>
#include <signal.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <sys/prctl.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/syscall.h>
#include <sys/types.h>
#include <sys/un.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sched.h>

#define syscall_nr (offsetof(struct seccomp_data, nr))
#define arch_nr (offsetof(struct seccomp_data, arch))
#define ARCH_NR AUDIT_ARCH_X86_64

#define VALIDATE_ARCHITECTURE                             \
  BPF_STMT(BPF_LD + BPF_W + BPF_ABS, arch_nr),            \
      BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, ARCH_NR, 1, 0), \
      BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_KILL)

#define EXAMINE_SYSCALL BPF_STMT(BPF_LD + BPF_W + BPF_ABS, syscall_nr)

#define INSPECT_SYSCALL(name)                            \
  BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, __NR_##name, 0, 1), \
      BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_USER_NOTIF)

#define ALLOW_SYSCALLS BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_ALLOW)

#define errExit(msg)    \
  do {                  \
    perror(msg);        \
    exit(EXIT_FAILURE); \
  } while (0)

#define F_GETPATH 12

int seccomp(unsigned int operation, unsigned int flags, void *args) {
  return syscall(__NR_seccomp, operation, flags, args);
}

int sendfd(int sockfd, int fd) {
  struct msghdr msgh;
  struct iovec iov;
  int data;
  struct cmsghdr *cmsgp;

  union {
    char buf[CMSG_SPACE(sizeof(int))];
    /* Space large enough to hold an 'int' */
    struct cmsghdr align;
  } controlMsg;

  msgh.msg_name = NULL;
  msgh.msg_namelen = 0;

  msgh.msg_iov = &iov;
  msgh.msg_iovlen = 1;
  iov.iov_base = &data;
  iov.iov_len = sizeof(int);
  data = 12345;

  msgh.msg_control = controlMsg.buf;
  msgh.msg_controllen = sizeof(controlMsg.buf);

  cmsgp = CMSG_FIRSTHDR(&msgh);
  cmsgp->cmsg_level = SOL_SOCKET;
  cmsgp->cmsg_type = SCM_RIGHTS;
  cmsgp->cmsg_len = CMSG_LEN(sizeof(int));
  memcpy(CMSG_DATA(cmsgp), &fd, sizeof(int));

  if (sendmsg(sockfd, &msgh, 0) == -1) return -1;

  return 0;
}

void readflag(){
  int fd;
  char *buf;

  if(!(buf = malloc(0x100))) errExit("malloc");
  if((fd = open("/flag",0)) < 0) errExit("open");
  read(fd,buf,0x100);
  close(fd);
  // if(unlink("/flag")) errExit("unlink");
}

int installNotifyFilter(void) {
  struct sock_filter filter[] = {
      VALIDATE_ARCHITECTURE,
      EXAMINE_SYSCALL,
      INSPECT_SYSCALL(openat),
      ALLOW_SYSCALLS,
  };

  struct sock_fprog prog = {
      .len = sizeof(filter) / sizeof(filter[0]),
      .filter = filter,
  };

  int notifyFd = seccomp(SECCOMP_SET_MODE_FILTER, SECCOMP_FILTER_FLAG_NEW_LISTENER, &prog);
  if (notifyFd == -1) errExit("seccomp-install-notify-filter");
  return notifyFd;
}

int recvfd(int sockfd) {
  struct msghdr msgh;
  struct iovec iov;
  int data, fd;
  ssize_t nr;

  union {
    char buf[CMSG_SPACE(sizeof(int))];
    struct cmsghdr align;
  } controlMsg;
  struct cmsghdr *cmsgp;

  msgh.msg_name = NULL;
  msgh.msg_namelen = 0;

  msgh.msg_iov = &iov;
  msgh.msg_iovlen = 1;
  iov.iov_base = &data; 
  iov.iov_len = sizeof(int);


  msgh.msg_control = controlMsg.buf;
  msgh.msg_controllen = sizeof(controlMsg.buf);


  nr = recvmsg(sockfd, &msgh, 0);
  if (nr == -1) return -1;

  cmsgp = CMSG_FIRSTHDR(&msgh);

  if (cmsgp == NULL || cmsgp->cmsg_len != CMSG_LEN(sizeof(int)) ||
      cmsgp->cmsg_level != SOL_SOCKET || cmsgp->cmsg_type != SCM_RIGHTS) {
    errno = EINVAL;
    return -1;
  }

  memcpy(&fd, CMSG_DATA(cmsgp), sizeof(int));
  return fd;
}

void allocSeccompNotifBuffers(struct seccomp_notif **req,
                                     struct seccomp_notif_resp **resp,
                                     struct seccomp_notif_sizes *sizes) {
  if (seccomp(SECCOMP_GET_NOTIF_SIZES, 0, sizes) == -1)
    errExit("seccomp-SECCOMP_GET_NOTIF_SIZES");

  *req = malloc(sizes->seccomp_notif);
  if (*req == NULL) errExit("malloc-seccomp_notif");

  size_t resp_size = sizes->seccomp_notif_resp;
  if (sizeof(struct seccomp_notif_resp) > resp_size)
    resp_size = sizeof(struct seccomp_notif_resp);

  *resp = malloc(resp_size);
  if (resp == NULL) errExit("malloc-seccomp_notif_resp");
}

void *readChildPath(pid_t pid,void *addr){
  char memAddr[PATH_MAX];
  char path[PATH_MAX],readedChar;
  int fd,readed;
  char *p = path;
  printf("pid:%d\n",pid);
  snprintf(memAddr,PATH_MAX,"/proc/%d/mem",pid);
  fd = open(memAddr,0);
  if(fd < 0 || lseek(fd,addr,SEEK_SET) < 0) return 0;
  for(int i=0;i<PATH_MAX;i++,p++){
    if(!read(fd,p,1)) return 0;
    if(*p == 0) break;
  }

  close(fd);
  return strdup(path);
}

void handleNotifications(int notifyFd){
  struct seccomp_notif_sizes sizes;
  struct seccomp_notif *req;
  struct seccomp_notif_resp *resp;
  struct seccomp_notif_addfd addfd;
  char *filePath = NULL;
  char realPath[PATH_MAX];
  char fdPath[PATH_MAX];

  int fd;
  struct stat finfo;

  allocSeccompNotifBuffers(&req, &resp, &sizes);

  for (;;) {
    memset(req, 0, sizes.seccomp_notif);
    if (ioctl(notifyFd, SECCOMP_IOCTL_NOTIF_RECV, req) == -1) {
      if (errno == EINTR) continue;
      errExit("ioctl recv");
    }

    resp->id = req->id;
    resp->flags = 0;
    resp->error = resp->val = -1;

    if (req->data.nr == __NR_openat && req->data.args[2] == 0) {
      filePath = readChildPath(req->pid,req->data.args[1]);
      if(filePath){
        // fd = openat(req->data.args[0], filePath, req->data.args[2],req->data.args[3]);
        // snprintf(fdPath,PATH_MAX,"/proc/self/fd/%d",fd);
        // if(fd > 0 && readlink(fdPath,realPath,PATH_MAX) > -1 && strchr()){
        //   addfd.id = req->id;
        //   addfd.srcfd = fd;
        //   addfd.newfd = 0;
        //   addfd.flags = 0;
        //   addfd.newfd_flags = 0;
        //   resp->val = ioctl(notifyFd, SECCOMP_IOCTL_NOTIF_ADDFD, &addfd);
        //   resp->error = 0;
        // }
        // close(fd);
      }
      perror("A");
      free(filePath);
      filePath = NULL;

    }

    if (ioctl(notifyFd, SECCOMP_IOCTL_NOTIF_SEND, resp) == -1) {
      perror("ioctl-SECCOMP_IOCTL_NOTIF_SEND");
    }
  }

  free(req);
  free(resp);
  exit(1);
}

void handleParent(int sockPair[2]){
  int notifyFd;
  readflag();
  if(setgid(1000) || setuid(1000)) errExit("drop privs");
  if ((notifyFd = recvfd(sockPair[1])) == -1) errExit("recvfd");
  handleNotifications(notifyFd);
}

void handleChild(int sockPair[2]){
  int fd;
  fd = installNotifyFilter();
  if (sendfd(sockPair[0], fd) == -1) errExit("sendfd");
  if (close(fd) == -1) errExit("close-target-notify-fd");
}

int main(char **) {
  int sockPair[2];
  char *args = NULL;
  setbuf(stdout, NULL);
  if(socketpair(AF_UNIX, SOCK_STREAM, 0, sockPair) == -1)
    errExit("socketpair");
  if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)) errExit("prctl");
  if (prctl(PR_SET_CHILD_SUBREAPER,1)) errExit("prctl");
  if(fork()){
    handleParent(sockPair);
  } else {
    handleChild(sockPair);
    if(unshare(CLONE_NEWPID)) errExit("unshare");
    if(!fork()){
      int a = openat(AT_FDCWD,"/bin/",0,0);
      // system("ls");
      while(1){}
    }
  }
  //Fork child -> clone new pid - and chroot - uid and gid
  // char *args = NULL;
  // execve("/tmp/exploit",&args,&args);
  return 1;
}
