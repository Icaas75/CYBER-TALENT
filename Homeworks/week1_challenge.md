1.The full reset: a file currently has -rwxr-xr-x permissions.You want to change it so the owner has Read or write , the group has read only and others have no access.what is the 3-digit numeric command ?

solution

    640

2.The Executioner: You have a script with 644 permissions.You want to make it excutable for everyone while keeping the read/write settings the same.What is the new 3 digit numeric code?

solution

    755
3.The source log: a log file needs to be writable by the owner and group, but readable by everyone.What is the octal command?

solution

    the numeric command= 664
    octal command = chmod 664 filename

4.Binary to octal: if a fie's binary permission string is 110 100 000, what is the corresponding chmod numeric command?

solution

    110 = 6(rw-)
    100 = 4(r--)
    000 = 0(---)
    chmod 640 filename

5.The Mystery code: what happens to a file if you run chmod 000 secret.txt?can the owner still cat the file without using sudo?

soultion

    chmod 000 secret.txt removes all permissions ---------
    The owner can't cat the file without sudo (read permission is required).

6.File creation: create a file named "Audit.txt" and assign it the following permission:
rwxr-x---

solution

    touch Audit.txt
    chmod 750 Audit.txt

7.Numeric to symbolic:what is the equivalent of a 741 permission in symbolic notation?

solution

    rwxr----x

8.Numeric to symbolic:what is the equivalent of a 500 permission in symbolic notation?

soloution

    r-x------

9.Symbolic to numeric:what is the numeric equivalent of -r-xrw-r--?

solution

    564
