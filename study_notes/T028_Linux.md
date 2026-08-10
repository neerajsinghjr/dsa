````
-------------------------------------------------------------------------------------
-> Title   : Linux Notes
-> Author  : @neeraj-singh-jr
-> Status  : Ongoing ...
-> Created : 09/08/2026
-> Updated : 10/08/2026
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q003 : Text Mode Handling in Linux Lifecycle;;
-> Q002 : Linux Command Line;;
-> Q001 : Getitng Familiar with Linux History;;
-------------------------------------------------------------------------------------
````

### LINUX NOTES : BEGINNING

-------------------------------------------------------------------------------------
### Q003 : Text Mode Handling in Linux Lifecycle;;






-------------------------------------------------------------------------------------
### Q002 : Linux Command Line;;

#### THE SHELL 

The shell is useful because it is fast, scriptable, and available on almost
every Linux system.

**Syntax**

`command options arguments`

**Your First Linux Command**

```bash

$ echo Hello World
Hello World

```


#### PWD (PRINT WORKING DIRECTORY) COMMAND

The pwd command answers that question by printing your current working
directory.

**Syntax**
`$ pwd`


**Using the pwd Command**

```bash

$ pwd

# OUTPUT
# /home/pete

```


#### CD (CHANGE DIRECTORY) COMMAND

To move around the Linux filesystem, you use paths to specify your
destination. The primary tool for this is the cd command, short for change
directory. It changes the shell's current working directory.


**Syntax**

`cd [DIRECTORY]`

**Understanding Paths**

There are two ways to specify a path: absolute and relative.

  `Absolute path` : The full path starting from the root directory (/). For
  example: `/home/pete/Desktop`.

  `Relative path` : A path based on your current location. If you are
  in `/home/pete/Documents` and want to access a subdirectory named taxes, you
  can use `taxes/`.

**Common Usages**

```bash

$ cd .  # current directory

$ cd .. # move one directory above

$ cd ~  # move to home dir

$ cd -  # move to root dir

```


#### LS (LIST DIRECTORY) COMMAND

By default, the ls command will list the directories and files in your current
directory. However, you can also specify a path to list the contents of a
different directory.

**Basic command usage**

```bash
$ ls
# OUTPUT: /home/pete
```

**Adding Path to Directory to list down files under it**

```bash
$ ls ~/Download/

# OUTPUT:
# linuxmint-22.3-cinnamon-64bit.iso  offline  readme.md  temp

```

**Viewing hidden files**

```bash

$ ls -a

```

**Listing with detailed file information**

```bash

$ ls -l

```

**Sorting in Reverse Order as per filename**

```bash

$ ls -r

```

**Sortig as per the timestamp in Ascending order**

```bash

$ ls -at

```

**Adding Human Readable sized with 'l' argument**

```bash

$ ls -lh

```

**Combining Usefull ls Command**

```bash

$ ls -al # listing detailed hidden files;

$ ls -alt # listing detailed hidden files with asc timestamp;

$ ls -alh # listing detailed hidden file with humand readable size limit;
```


#### TOUCH COMMAND

The touch command is a standard utility on Unix-like operating systems. While
its primary purpose is to change file timestamps, it is also commonly used to
create new, empty files.

**Basic syntax/usage**

`touch [OPTIONS] FILE...`

**Creating a new file**

```bash

$ touch myNewFile.txt

# or 

$ touch file1.txt file2.txt file3.log

```

**Update timestamp of existing files**

```bash

$ touch myNewFile.txt

# or

$ touch file1.txt file2.txt file3.log

```

**Copy and past of existing file timestamp to other**

```bash

$ touch -r file.log file2.log # here r stands for reference;

```

**Set custom date manually to file**

```bash

$ touch -d "2026-08-09 00:00:00" file3.log

```

**Update timestamp only when file exist in directory**

```bash

$ touch -c file3.log

```

**Common touch Options**
  1.  `-a` : Change only the access time.
  2.  `-m` : Change only the modification time.
  3.  `-c` : Do not create the file if it does not exist.
  4.  `-d` "DATE" : Use a specific date string.
  5.  `-r` FILE   : Use another file's timestamp as a reference.
  6.  `-t` STAMP  :  Use a timestamp in a compact numeric format.


#### FILE COMMAND

In Linux, filenames aren't required to represent the contents of the file. You
can create a file called funny.gif that isn't actually a GIF.

To find out what kind of file a `file` is, you can use the file command. It
will show you a description of the file's contents.

```bash

$ file banana.jpg
# banana.jpg: JPEG image data

```

**NOTE: Why File Extensions Are Not Enough**

Linux tools usually do not require a file extension to decide what a file is.

A shell script can be named backup, a text file can be named README, and an
image can have the wrong extension. The file command inspects the file's
contents and metadata to make a better guess.

Like this, 

```bash

$ file README
# README: ASCII text

$ file /bin/ls
# /bin/ls: ELF 64-bit LSB executable

# or combined in one command

$ file notes.txt image.png archive.tar.gz
# notes.txt: ASCII text
# image.png: PNG image data
# archive.tar.gz: gzip compressed data

```

**Showing MIME Types**

```bash

$ file -i readme.md
# readme.md: text/plain; charset=us-ascii

```

**Common file Options**
  1.  `-i` : Show MIME type information.
  2.  `-b` : Brief mode, omit the filename in output.
  3.  `-L` : Follow symbolic links.
  4.  `-z` : Try to inspect compressed files.


#### CAT COMMAND 

The name cat is short for "concatenate," which hints at its ability to link
files together.

**Viewing file content**

```bash

$ cat o1.txt 
# === o1 file content ===

$ cat o2.txt 
# === o2 file content ===

```

**Concatenation of files**

```bash

$ cat o1.txt o2.txt 
# === o1 file content ===
# === o2 file content ===

```

**Redirection of cat output**

```bash

$ cat o1.txt o2.txt > o3.txt

$ cat o3.txt 
# === o1 file content ===
# === o2 file content ===

```

**When Not to Use cat**

Use cat for short files. For long files, use less so you can scroll, search,
and quit without flooding your terminal.

```bash

$ less /var/log/syslog

```

**Common cat Command Options**

The cat command has several options to modify its behavior.

  1. `-n` : Number all output lines, starting from 1.
  2. `-b` : Number only non-empty output lines.
  3. `-s` : Squeeze multiple blank lines into one blank line.
  4. `-A` : Show non-printing characters, tabs, and line endings.


#### LESS COMMAND

When viewing text files that are too large to fit on a single screen, the less
command is an invaluable tool.

The less utility displays text in a paged format, allowing you to navigate
through a file without flooding your terminal.

**Basic Usage**

```bash

$ less /home/pete/Documents/text1

```
**Navigation and Controls**

You can use several keys to move through the document:

  - Arrow Keys and Page Keys: Use Page Up, Page Down, Up, and Down to navigate
    line by line or page by page.
  - Go to Start: Press g to move directly to the beginning of the text file.
  - Go to End: Press G (Shift + g) to jump to the end of the text file.
  - Move half a page: Press u to move up and d to move down.
  - Help Menu: If you forget the commands while inside less, just press h to
    display a helpful summary.

**Searching in Less**

A powerful feature of less is its ability to search for text. Type / followed
by the text you want to find, and then press Enter.

  - /search_term: Searches forward for "search_term".
  - ?search_term: Searches backward for "search_term".
  - n: Jumps to the next occurrence of the search term.
  - N: Jumps to the previous occurrence.

**How to Exit Less**

Quit: Simply press q to quit the less viewer and go back to your shell

**Useful less Options**

You can start less with options:

```bash

$ less -N file.txt # -N : Show line number;;

$ less +G file.txt # -G : Open file at the end;;

$ less +F /var/log/syslog # +F : Open file in live mode, similar to tail -f;;

```

#### HISTORY COMMAND

Linux Shell stores every command that user ran inside the terminal and we can
use the history command to traceback all this command.

**Viewing history command**

```bash

$ history
# 101  pwd
# 102  ls -la

```

**Re-running Previous Commands**

The shell provides several shortcuts to make re-running commands easier.

  - Up Arrow: Want to run the same command you just did? Just press the up
    arrow key to cycle backward through your history.

  - The `!!` Shortcut: To execute the most recent command again, you can use
    `!!`. For example, if you just ran `cat file1`, typing `!!` and pressing
    Enter will run `cat file1` again.
  
  - Run by number: Use `!102` to run command number 102 from your history.
  
  - Run by prefix: Use `!cat` to run the most recent command that started with
    cat.

**Searching Your History**

One of the most powerful history shortcuts is `Ctrl-R` :- This initiates a
reverse search. After pressing Ctrl-R, start typing any part of the command
you're looking for, and the shell will display the most recent match. 

You can press Ctrl-R repeatedly to cycle through older matches. Once you find
the command you want, just press Enter to execute it.

**Managing the History List**

Beyond just viewing your history, you can also manage it directly.

  - Clear current history list: `history -c` removes all entries from the
    history list in memory.

  - Write history to file: `history -w` saves the current session's history to
    your history file, usually `~/.bash_history`.

  - Delete a specific entry: `history -d <offset>` removes one command by its
    history number.


#### CP (COPY) COMMAND

The cp command is the standard tool for copying files and directories in
Linux.

**Syntax**

` cp [OPTIONS] SOURCE DESTINATION `

**Basic usage**

```bash

$ cp mycoolfile /home/pete/Documents/cooldocs

```

**Copy multiple files to directory**

```bash

$ cp report.txt notes.txt summary.txt /home/pete/Documents/

```

**Using Wildcards for Bulk Copying**

Wildcards are special characters that help you select multiple files based on
patterns, providing great flexibility.

  - `*`  : Matches any sequence of characters.
  - `?`  : Matches any single character.
  - `[]` : Matches any one of the characters enclosed in the brackets.

```bash

# using asterick with cp command;;
$ cp *.jpg /home/pete/Pictures

# OUTPUT:
# a.jpg
# b.jpg
# c.jpg

# using question mark with single character;;
$ cp file?.txt /backup/

# OUTPUT:
# file1.txt
# file2.txt
# fileA.txt

# [] - matches one character from the brackets;;
$ cp file[1-3].txt /backup/

# OUTPUT:
# file1.txt
# file2.txt
# file3.txt

```

**Copying Directories Recursively**

```bash

$ cp -r Pumpkin/ /home/pete/Documents

# or 

$ cp -R website /home/pete/backups/

```

**Handling Interactive File Overwrites**

```bash

$ cp -i mycoolfile /home/pete/Pictures

# Output
# cp: overwrite '/home/pete/Pictures/mycoolfile'? n

```
**Handling Overwrite any existing file**

```bash

# if you want the cp command to overwrite;;
$ cp -f mycoolfile /home/pete/Pictures

# or

# if you dont want to overwrite any existing file;;
$ $ cp -n mycoolfile /home/pete/Pictures

```

**Preserve File Attributes**

When you copy a file, its metadata, such as modification time and ownership,
is typically updated. To preserve these original attributes, use the -p
option.

```bash

$ cp -p mycoolfile /home/pete/backups/

```

**Common cp Options**

Here are the options you will use most often:

  [+] `-r` or `-R `: Copy directories recursively.
  [+] `-i` : Ask before overwriting a file.
  [+] `-f` : Force overwriting by removing the destination first if needed.
  [+] `-n` : Do not overwrite existing files.
  [+] `-p` : Preserve mode, ownership where possible, and timestamps.
  [+] `-a` : Archive mode, useful for preserving directory trees.
  [+] `-u` : Copy only when the source is newer than the destination.
  [+] `-v` : Show each file as it is copied.


#### MV (MOVE) COMMAND

The mv command, short for "move," is a fundamental utility in any Linux env.

**Syntax**

`mv [OPTIONS] SOURCE DESTINATION`

**Renaming Files and Directories**

```bash

$ mv oldfile newfile

# or

$ mv old_directory_name new_directory_name

# or 

$ mv file_1 file_2 somedirectory/

# or, specifcy target directory with -t argument

$ mv -t targetDirectory/ file_1 file_2

```

**Important Move Directory**

```bash

# interactive move from source to directory
$ mv -i source_file destination_directory

# verbose showes each step while moving
$ mv -v file1 file2 targetDirectory/

# prevent overwriting the target file
$ mv -n sourceFile targetDirectory/targetFile

# backup target file before overwrite with (~tilde)
$ mv -b file1 directory_with_file1

```

#### MKDIR (MAKE DIRECTORY) COMMAND

The mkdir command is used to create directory

**Syntax**

`mkdir [OPTIONS] DIRECTORY...`

**Basic usage**

```bash

$ mkdir documents

# Creating Multiple Directories

$ mkdir books paintings

# Creating Nested Directories

$ mkdir -p books/hemingway/favorites

```

**Setting Directory Permissions**

Use -m to set permissions while creating a directory.


```bash

$ mkdir -m 755 public

```

**Common mkdir Options**
  [+] `-p` : Create parent directories as needed.
  [+] `-m` : MODE - Set permissions for the new directory.
  [+] `-v` : Print a message for each created directory.


#### RM (REMOVE) COMMAND

**Syntax**

`rm [OPTIONS] FILE...`

**Basic usage**

```bash

$ rm file1

# or, remove files with wildcard

$ rm *.tmp

# or, interactive deletion

```

**Interactive Deletion**

```bash

$ rm -i important.txt

#  Output: 
#  rm: remove regular file 'important.txt'? y

```
**Forece & Recursive Deletion**

```bash

$ rm -f old-cache.txt

# or, 

$ rm -r old-project

# or, combined mode

$ rm -rf old-project

```

**Using rmdir for Empty Directories**

```bash

$ rmdir empty-directory

```

#### FIND COMMAND

The find command searches directory trees using criteria such as name, type,
size, and modification time.

**Syntax**

`find [PATH] [EXPRESSION]`


**Searching by Name using '-name'**

```bash

$ find ~/Pictures/ -name "*.png"

# OUTPUT
# /home/devil/Pictures/Screenshots/test.png
# /home/devil/Pictures/Screenshots/zookeeper/Screenshot from 2024-07-15 21-36-40.png

```

**Searching by Type using '-type'**

```bash

$ find ~/Pictures/ -type d -name "zoo*"
# OUTPUT:
# /home/devil/Pictures/Screenshots/zookeeper

```

**Searching by Size and Time**

```bash

# You can search by file size:
$ find . -type f -size +10M
$ find . -type f -size -1k

# The first command finds files larger than 10 megabytes. The second finds
# files smaller than 1 kilobyte.

# You can also search by modification time:
$ find . -type f -mtime -7
$ find . -type f -mtime +30

# -mtime -7 means modified within the last 7 days. -mtime +30 means modified
#  more than 30 days ago.

```

**Running Actions on Results**


```bash

$ find . -name "*.png" -exec ls -alt {} \;

# OUTPUT
-rw-rw-r-- 1 devil devil 0 Aug 10 16:40 ./Screenshots/test.png
-rw-rw-r-- 1 devil devil 324956 Jul 15  2024 './Screenshots/zookeeper/Screenshot from 2024-07-15 21-36-40.png'
-rw-rw-r-- 1 devil devil 732045 Jul 15  2024 './Screenshots/zookeeper/Screenshot from 2024-07-15 21-37-48.png'

```

Breakdown for the above command `find . -name "*.png" -exec ls -alt {} \;`

`{} \;` -> This show end of the command to tell find command

```
-exec ls {} \;
       │  │  │
       │  │  └── End of the -exec command
       │  └───── Current file found by find
       └──────── Command to execute
```
suppose if you want to add one more command on top of above command, then 

```bash

$ find . -name "*.png" -exec ls -alt {} \; -exec df -h {} \;

# OUTPUT
-rw-rw-r-- 1 devil devil 0 Aug 10 16:40 ./Screenshots/test.png
Filesystem      Size  Used Avail Use% Mounted on
/dev/nvme0n1p8  145G   32G  106G  23% /home

```

**Common find Options**

[+] `-name PATTERN` : Match by filename.
[+] `-iname PATTERN` : Match by filename, ignoring case.
[+] `-type f` : Match regular files.
[+] `-type d` : Match directories.
[+] `-size +10M` : Match files larger than 10 megabytes.
[+] `-mtime -7` : Match files modified within the last 7 days.
[+] `-maxdepth N` : Limit how deep find searches.


#### HELP COMMAND 


**Syntax**

`$ help echo`


**'--help' with executables**

```bash

$ ls --help

```

**Finding Command Type**

If you are not sure whether a command is a Bash built-in or an external
program, use `type`.

```bash

$ type man
# OUTPUT
# man is hashed (/usr/bin/man)

$ type -a man
# OUTPUT
# man is /usr/bin/man
# man is /bin/man

```

**Choosing the Right Help Tool**

  [+] Use `help COMMAND` for Bash built-ins such as cd, echo, and history.
  [+] Use `COMMAND --help` for a quick summary from many external commands.
  [+] Use `man COMMAND` for detailed manual pages.
  [+] Use `whatis COMMAND` for a one-line description.


#### MAN COMMAND

Man pages are the built-in documentation for Linux commands, utilities, and
system calls. They provide a detailed description of what a command does, its
available options (or flags), and how to use it.

**Syntax**

`man ls`

**Finding Details on Command Options**

  [+] Press `/` and type a search term to search forward.
  [+] Press `n` to jump to the next match.
  [+] Press `N` to jump to the previous match.
  [+] Press `q` to quit.

**Understanding Man Page Sections**

Manual pages are organized into numbered sections. Common sections include:

  [+] `1` : User commands.
  [+] `2` : System calls.
  [+] `3` : Library functions.
  [+] `5` : File formats.
  [+] `8` : System administration commands.

for eg,

```bash

$ man 5 passwd
$ man 1 passwd

```

#### WHATIS COMMAND

The whatis command displays a concise, one-line description of a command
directly from its manual page. It is a quick way to get a reminder of a
command's primary function without reading the entire man page

```bash

$ whatis cat
# OUTPUT
# cat (1) - concatenate files and print on the standard output

# or If a command has multiple manual pages in different sections, whatis may
# display more than one line.

$ whatis passwd
# OUTPUT
# passwd (5)           - the password file
# passwd (1)           - change user password
# passwd (1ssl)        - OpenSSL application commands

```

**Whatis vs Man vs Apropos**
[+] `whatis ls` : Show a one-line description for an exact command name.
[+] `man ls` : Open the full manual page.
[+] `apropos keyword` : Search man page descriptions for a keyword.

**usage of apropos command**

```bash

$ apropos passwd
# OUTPUT
# chgpasswd (8)        - update group passwords in batch mode
# chpasswd (8)         - update passwords in batch mode
# fgetpwent_r (3)      - get passwd file entry reentrantly
# getpwent_r (3)       - get passwd file entry reentrantly
# gpasswd (1)          - administer /etc/group and /etc/gshadow
# grub-mkpasswd-pbkdf2 (1) - generate hashed password for GRUB
# openssl-passwd (1ssl) - compute password hashes
# pam_localuser (8)    - require users to be listed in /etc/passwd
# passwd (1)           - change user password
# passwd (1ssl)        - OpenSSL application commands
# passwd (5)           - the password file
# passwd2des (3)       - RFS password encryption
# update-passwd (8)    - safely update /etc/passwd, /etc/shadow and /etc/group

```


#### ALIAS COMMAND

An alias is a shell shortcut that lets you define a custom name for a command
or sequence of commands.

**Syntax**

`alias ll='ls -la'`

**Making an Alias Permanent**

A temporary alias will disappear once you close your terminal or reboot your
system. 

To make a command alias in linux permanent, you need to add it to your shell's
configuration file. For the Bash shell, this file is typically `~/.bashrc`.

  1. Open the file in a text editor: nano ~/.bashrc
  
  2. Add your alias definition to the file, just as you typed it on the
  command line:
  ```bash

  alias ll='ls -la'
  alias update='sudo apt update && sudo apt upgrade'

  ```

  3. Save the file and exit the editor.

  4. Execute the bashrc file using source command
  ```bash

  $ source ~/.bashrc
  
  ```

**Removing an Alias**

```bash

# Remove temporary alias from existing session of terminal
$ unalias ll

```

**Listing Existing Aliases**

```bash

$ alias
# OUTPUT
# alias ll='ls -la'
# alias grep='grep --color=auto'

```


#### EXIT COMMAND

The most common way to end a shell session is with the exit command.

**Syntax**

`$ exit`

**Exit Status Values**

The exit command can also return a status code. A status of 0 usually means
success, and a nonzero status usually means an error or special condition.

```bash

$ exit 0

```

**The Logout Command**

Another command you can use for a terminal exit is `logout`. This command is
specifically designed to terminate a login shell. While in many modern
systems it behaves similarly to exit

```bash

$ logout

```


-------------------------------------------------------------------------------------
### Q001 : Getitng Familiar with Linux History;;

**The Predecessors of Linux**

Its all started with 1969 when Ken Thompson and Dennis Ritchie of Bell
Laboratories developed the UNIX operating system. 

It was later rewritten in the C programming language, which made it portable
and led to its widespread adoption.

--- timeline

1969 -> Ken Thompson & Dennis Ritchie create UNIX at Bell Labs 

1973 -> UNIX rewritten in C lang - become portable & widely adopted

1983 -> Richard Stallman launches at the GNU Project(GNU is not Linux)

1985 -> GNU General Public License (GPL) introduced 

1990 -> GNU Kernel "Hurd" remains incomplete

1991 -> Linux Torvald starts developing Linux kernel

1992 -> Linux released under GPL -> GNU/LINUX Ecosystem

--- /timeline

Over a decade later, Richard Stallman initiated the GNU (a recursive acronym
for "GNU's Not UNIX") project.


**The Role of the Kernel**

The kernel is the core component of an operating system. It acts as a bridge,
allowing the hardware to communicate with the software. The kernel manages
system resources, such as the CPU, memory, and peripheral devices. 

Essentially, the kernel controls everything that happens on your system. While
other UNIX-like systems such as BSD and MINIX were being developed, they all
lacked a freely available and unified kernel.

**The Birth of the Linux Kernel**

This brings us to 1991, when a Finnish student named Linus Torvalds began
developing a new kernel as a personal project. 

This kernel, which we now know as the Linux kernel, filled the missing piece
of the GNU operating system. The combination of the GNU tools and the Linux
kernel created the complete, open-source operating system that is widely used
today. This milestone was a pivotal moment in the history of Linux.



-------------------------------------------------------------------------------------