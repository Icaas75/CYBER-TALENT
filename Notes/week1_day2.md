Basic Linux Commands

Show current directory

    pwd

List files

    ls
    ls -a      #show hidden files without details
    ls -la     # shows hidden files + details

Change directory

    cd folder_name
    cd ..       # go back one directory
    cd ~        # go to home directory

Create a file

    touch file.txt

Create a directory


    mkdir folder_name

Remove file

    rm file.txt

Remove directory

    rm -r folder_name

Copy files

    cp file.txt copy.txt

Move

    mv file.txt newname.txt

Viewing File Content

    cat file.txt

First lines

    head file.txt

Last lines
    
    tail file.txt

2. File Permissions

Example:

    -rwxr-xr--

Breakdown:

    | Symbol | Meaning            |
    | ------ | ------------------ |
    | -      | File type          |
    | rwx    | Owner permissions  |
    | r-x    | Group permissions  |
    | r--    | Others permissions |

Permission Types

    | Symbol | Meaning |
    | ------ | ------- |
    | r      | Read    |
    | w      | Write   |
    | x      | Execute |

Changing Permissions

Examlple:

    chmod 755 file.txt

Adding permission

    chmod +x file.sh

Remove permission

    chmod -w file.txt

Numeric values

    | Permission | Value |
    | ---------- | ----- |
    | r          | 4     |
    | w          | 2     |
    | x          | 1     |

---
