---
id: cn_lab
title: Computer Networks Lab
sidebar_label: Computer Networks Lab
---

## Linux Commands

* `wget`, usage: `wget [option] [URL]`. Wget is the non-interactive network downloader which is used to download files from the server even when the user has not logged on to the system and it can work in the background without hindering the current process. Example: To download the file in background: `wget -b http://www.example.com/samplepage.php`

## Lab 2

* HTTP 1.0 (will immediately close the connection when receiving the response and was therefore slow as setting up TCP connection is expensive. Also it had buffering).
* HTTP 1.1 (will have something like "keep alive" header (host header) to let the server know that it should not close this connection. Also it had streaming (remember images loading line by line few years ago)).
  
### FPT

* Connection
  ```
  ftp domain.com
  ftp 192.168.0.1
  ftp user@ftpdomain.com
  ```
  May ask for username and password.
  If you connect to a so-called anonymous FTP server, then try to use "anonymous" as username and an empty password:

* The commands to list, move and create folders on an FTP server are almost the same as we would use the shell locally on our computer, ls stands for list, cd to change directories, mkdir to create directories...

* Before downloading a file, we should set the local FTP file download directory by using 'lcd' command: `lcd /home/user/yourdirectoryname`
* If you dont specify the download directory, the file will be downloaded to the current directory where you were at the time you started the FTP session.
  Now, we can use the command 'get' command to download a file, the usage is:

  `get file`
* To download several files we can use wildcards, like: `mget *.xls`
* To upload a file, we can use 'put' command. `put file`
  When the file that you want to upload is not in the local directory, you can use the absolute path starting with "/" as well:

  To upload several files we can use the mput command similar to the mget example from above:

  `mput *.xls`

* There are three commands that we can use to close the connection:

  ```
  bye
  exit
  quit
  ```

## Socket programming using C/C++

```c
// server.c
/* A simple server in the internet domain using TCP
   The port number is passed as an argument */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
// This header file contains definitions of a number of data types used in system calls. These types are used in the next two include files.
#include <sys/socket.h>
// The header file socket.h includes a number of definitions of structures needed for sockets.
#include <netinet/in.h>
// The header file in.h contains constants and structures needed for internet domain addresses.

// This function is called when a system call fails. It displays a message about the error on stderr and then aborts the program.
void error(const char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
     int sockfd, newsockfd, portno;
     socklen_t clilen;
    // portno stores the port number on which the server accepts connections.
    // clilen stores the size of the address of the client. This is needed for the accept system call.
     char buffer[256];
     struct sockaddr_in serv_addr, cli_addr;
    //  A sockaddr_in is a structure containing an internet address. This structure is defined in netinet/in.h.
    // struct sockaddr_in
    // {
    //     short   sin_family; /* must be AF_INET */
    //     u_short sin_port;
    //     struct  in_addr sin_addr;
    //     char    sin_zero[8]; /* Not used, must be zero */
    // };
    // An in_addr structure, defined in the same header file, contains only one field, a unsigned long called s_addr. For server code, this will always be the IP address of the machine on which the server is running, and there is a symbolic constant INADDR_ANY which gets this address.
     int n;
     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     sockfd = socket(AF_INET, SOCK_STREAM, 0);
    //  The socket() system call creates a new socket. It takes three arguments. The first is the address domain of the socket.
    // Recall that there are two possible address domains, the unix domain for two processes which share a common file system, and the Internet domain for any two hosts on the Internet. The symbol constant AF_UNIX is used for the former, and AF_INET for the latter (there are actually many other options which can be used here for specialized purposes).

    // The second argument is the type of socket. Recall that there are two choices here, a stream socket in which characters are read in a continuous stream as if from a file or pipe, and a datagram socket, in which messages are read in chunks. The two symbolic constants are SOCK_STREAM and SOCK_DGRAM.

    // The third argument is the protocol. If this argument is zero (and it always should be except for unusual circumstances), the operating system will choose the most appropriate protocol. It will choose TCP for stream sockets and UDP for datagram sockets.
     if (sockfd < 0) 
        error("ERROR opening socket");
     bzero((char *) &serv_addr, sizeof(serv_addr));
     portno = atoi(argv[1]);
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);
    //  The second field of serv_addr is unsigned short sin_port, which contain the port number. However, instead of simply copying the port number to this field, it is necessary to convert this to network byte order using the function htons() which converts a port number in host byte order to a port number in network byte order.
     if (bind(sockfd, (struct sockaddr *) &serv_addr,
              sizeof(serv_addr)) < 0) 
              error("ERROR on binding");
    // The bind() system call binds a socket to an address.
     listen(sockfd,5);
    //  The listen system call allows the process to listen on the socket for connections. The first argument is the socket file descriptor, and the second is the size of the backlog queue, i.e., the number of connections that can be waiting while the process is handling a particular connection. This should be set to 5, the maximum size permitted by most systems.
     clilen = sizeof(cli_addr);
     newsockfd = accept(sockfd, 
                 (struct sockaddr *) &cli_addr, 
                 &clilen);
    // The accept() system call causes the process to block until a client connects to the server.
     if (newsockfd < 0) 
          error("ERROR on accept");
     bzero(buffer,256);
     n = read(newsockfd,buffer,255);
     if (n < 0) error("ERROR reading from socket");
     printf("Here is the message: %s\n",buffer);
     n = write(newsockfd,"I got your message",18);
     if (n < 0) error("ERROR writing to socket");
     close(newsockfd);
     close(sockfd);
     return 0; 
}
```


```c
// client.c

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 

// The header files are the same as for the server with one addition. The file netdb.h defines the structure hostent, which will be used below.

// struct  hostent
// {
//   char    *h_name;        /* official name of host */
//   char    **h_aliases;    /* alias list, A zero  terminated  array  of  alternate
//              names for the host. */
//   int     h_addrtype;     /* host address type */
//   int     h_length;       /* length of address */
//   char    **h_addr_list;  /* list of addresses from name server */
//   #define h_addr  h_addr_list[0]  /* address, for backward compatiblity */
// };


void error(const char *msg)
{
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, n;
    struct sockaddr_in serv_addr;
    struct hostent *server;

    char buffer[256];
    if (argc < 3) {
       fprintf(stderr,"usage %s hostname port\n", argv[0]);
       exit(0);
    }
    portno = atoi(argv[2]);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) 
        error("ERROR opening socket");
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    // void bcopy(char *s1, char *s2, int length)
    bcopy((char *)server->h_addr, 
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);
    serv_addr.sin_port = htons(portno);
    if (connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0) 
        error("ERROR connecting");
    // Notice that the client needs to know the port number of the server, but it does not need to know its own port number. This is typically assigned by the system when connect is called.
    printf("Please enter the message: ");
    bzero(buffer,256);
    fgets(buffer,255,stdin);
    n = write(sockfd,buffer,strlen(buffer));
    if (n < 0) 
         error("ERROR writing to socket");
    bzero(buffer,256);
    n = read(sockfd,buffer,255);
    if (n < 0) 
         error("ERROR reading from socket");
    printf("%s\n",buffer);
    close(sockfd);
    return 0;
}
```