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