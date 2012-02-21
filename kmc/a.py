Welcome to Git (version 1.7.9-preview20120201)


Run 'git help git' to display the help index.
Run 'git help <command>' to display help for specific commands.

taurus0516@CP71570-N ~
$ ls
10shdrn           Favorites       NetHood    Templates       ???? ????
10shdrn.pub       Local Settings  PrintHood  ntuser.dat.LOG  ???? ????
Application Data  My Documents    Recent     ntuser.ini
Cookies           NTUSER.DAT      SendTo     ntuser.pol

taurus0516@CP71570-N ~
$ cd ..

taurus0516@CP71570-N /c/Documents and Settings
$ ls
All Users  CP  Default User  LocalService  NetworkService  taurus0516

taurus0516@CP71570-N /c/Documents and Settings
$ cd ..

taurus0516@CP71570-N /c
$ ls
AUTOEXEC.BAT            Log.dat        Recycled                   boot.ini
CONFIG.SYS              MSDOS.SYS      System Volume Information  bootfont.bin
Documents and Settings  MSOCache       Temp                       ntldr
FOUND.000               NTDETECT.COM   V3Ahn.cfg                  pagefile.dat
HandySoft               Packages       WINDOWS                    pagefile.sys
IO.SYS                  Program Files  XecureSSL                  serial.dat
Intel                   Python32       _hnix_trace_queue.txt

taurus0516@CP71570-N /c
$ cd c:

taurus0516@CP71570-N /c
$ ls
AUTOEXEC.BAT            Log.dat        Recycled                   boot.ini
CONFIG.SYS              MSDOS.SYS      System Volume Information  bootfont.bin
Documents and Settings  MSOCache       Temp                       ntldr
FOUND.000               NTDETECT.COM   V3Ahn.cfg                  pagefile.dat
HandySoft               Packages       WINDOWS                    pagefile.sys
IO.SYS                  Program Files  XecureSSL                  serial.dat
Intel                   Python32       _hnix_trace_queue.txt

taurus0516@CP71570-N /c
$ cd Python32

taurus0516@CP71570-N /c/Python32
$ ls
DLLs         Lib         Tools    python.exe   tcl
Doc          NEWS.txt    include  pythonw.exe  test.py
LICENSE.txt  README.txt  libs     study        w9xpopen.exe

taurus0516@CP71570-N /c/Python32
$ cd study

taurus0516@CP71570-N /c/Python32/study
$ ls

taurus0516@CP71570-N /c/Python32/study
$ ls

taurus0516@CP71570-N /c/Python32/study
$ gi
sh.exe": gi: command not found

taurus0516@CP71570-N /c/Python32/study
$ git
usage: git [--version] [--exec-path[=<path>]] [--html-path] [--man-path] [--info
-path]
           [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [-c name=value] [--help]
           <command> [<args>]

The most commonly used git commands are:
   add        Add file contents to the index
   bisect     Find by binary search the change that introduced a bug
   branch     List, create, or delete branches
   checkout   Checkout a branch or paths to the working tree
   clone      Clone a repository into a new directory
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   fetch      Download objects and refs from another repository
   grep       Print lines matching a pattern
   init       Create an empty git repository or reinitialize an existing one
   log        Show commit logs
   merge      Join two or more development histories together
   mv         Move or rename a file, a directory, or a symlink
   pull       Fetch from and merge with another repository or a local branch
   push       Update remote refs along with associated objects
   rebase     Forward-port local commits to the updated upstream head
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index
   show       Show various types of objects
   status     Show the working tree status
   tag        Create, list, delete or verify a tag object signed with GPG

See 'git help <command>' for more information on a specific command.

taurus0516@CP71570-N /c/Python32/study
$ dir -a
sh.exe": dir: command not found

taurus0516@CP71570-N /c/Python32/study
$ ls -a
.  ..

taurus0516@CP71570-N /c/Python32/study
$ ig init
sh.exe": ig: command not found

taurus0516@CP71570-N /c/Python32/study
$ git init
Initialized empty Git repository in c:/Python32/study/.git/

taurus0516@CP71570-N /c/Python32/study (master)
$ ls -a
.  ..  .git

taurus0516@CP71570-N /c/Python32/study (master)
$ git config global -l
error: key does not contain a section: global

taurus0516@CP71570-N /c/Python32/study (master)
$ gif config --global -l
sh.exe": gif: command not found

taurus0516@CP71570-N /c/Python32/study (master)
$ git config --global -l
user.name=taurus0516
user.email=taurus0516@nate.com

taurus0516@CP71570-N /c/Python32/study (master)
$ git remot add orign https://taurus0516@github.com/taurus0516/eulerproject.git
git: 'remot' is not a git command. See 'git --help'.

Did you mean this?
        remote

taurus0516@CP71570-N /c/Python32/study (master)
$

taurus0516@CP71570-N /c/Python32/study (master)
$

taurus0516@CP71570-N /c/Python32/study (master)
$

taurus0516@CP71570-N /c/Python32/study (master)
$

taurus0516@CP71570-N /c/Python32/study (master)
$

taurus0516@CP71570-N /c/Python32/study (master)
$

taurus0516@CP71570-N /c/Python32/study (master)
$ git remot add orign https://taurus0516@github.com/taurus0516/eulerproject.git
git: 'remot' is not a git command. See 'git --help'.

Did you mean this?
        remote

taurus0516@CP71570-N /c/Python32/study (master)
$ git remote add orign https://taurus0516@github.com/taurus0516/eulerproject.gi
t

taurus0516@CP71570-N /c/Python32/study (master)
$ git pull orign master
remote: Counting objects: 148, done.
remote: Compressing objects: 100% (134/134), done.
remote: Total 148 (delta 30), reused 130 (delta 12)Receiving objects:  34% (51/1

Receiving objects: 100% (148/148), 29.90 KiB, done.
Resolving deltas: 100% (30/30), done.
From https://github.com/taurus0516/eulerproject
 * branch            master     -> FETCH_HEAD

taurus0516@CP71570-N /c/Python32/study (master)
$ mkdir kmc

taurus0516@CP71570-N /c/Python32/study (master)
$ ls
README  kmc  need4spd

taurus0516@CP71570-N /c/Python32/study (master)
$ cd kmc

taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ ls
a.py  ?? ?????? ????.py  ?? ?????? ????.txt

taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ python a.py
hello

taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ git add
Nothing specified, nothing added.
Maybe you wanted to say 'git add .'?

taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ git commit -a
# On branch master
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#       ./
nothing added to commit but untracked files present (use "git add" to track)

taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ git add .

taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ git stats
git: 'stats' is not a git command. See 'git --help'.

Did you mean this?
        status

taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#       new file:   a.py
#       new file:   "\273\365 \305\330\275\272\306\256 \271\256\274\255.py"
#       new file:   "\273\365 \305\330\275\272\306\256 \271\256\274\255.txt"
#

taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ git commit -m "aa"
[master cb1c362] aa
 2 files changed, 2 insertions(+), 0 deletions(-)
 create mode 100644 kmc/a.py
 create mode 100644 "kmc/\273\365 \305\330\275\272\306\256 \271\256\274\255.py"
 create mode 100644 "kmc/\273\365 \305\330\275\272\306\256 \271\256\274\255.txt"


taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ git push
fatal: No configured push destination.
Either specify the URL from the command-line or configure a remote repository us
ing

    git remote add <name> <url>

and then push using the remote name

    git push <name>


taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ git push origin master
fatal: 'origin' does not appear to be a git repository
fatal: The remote end hung up unexpectedly

taurus0516@CP71570-N /c/Python32/study/kmc (master)
$ git push orign master
Password for 'https://taurus0516@github.com':
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 398 bytes, done.
Total 5 (delta 0), reused 1 (delta 0)
To https://taurus0516@github.com/taurus0516/eulerproject.git
   965d8c4..cb1c362  master -> master

taurus0516@CP71570-N /c/Python32/study/kmc (master)
$



