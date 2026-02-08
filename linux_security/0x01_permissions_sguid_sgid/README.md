# Permissions, SUID & SGID

## Resources
## Read or watch:

- [Permissions] (https://linuxcommand.org/lc3_lts0090.php)
- [Linux permissions] (https://www.redhat.com/en/blog/suid-sgid-sticky-bit)
- [Finding Files With SUID and SGID] (https://www.geeksforgeeks.org/linux-unix/finding-files-with-suid-and-sgid-permissions-in-linux/)
- [How to Use SUID and SGID on Linux] (https://www.howtogeek.com/656646/how-to-use-suid-sgid-and-sticky-bits-on-linux/)
- [Understanding Linux Special permissions] (https://dev.to/mbayoun95/linux-special-permissions-a-comprehensive-guide-with-examples-31pg)
(https://medium.com/@The_Anshuman/special-permissions-in-linux-f6045447448f)
(https://blog.marcnuri.com/linux-file-permissions-complete-guide)
- [What Is Umask and How to Use it Effectively] (https://www.liquidweb.com/blog/what-is-umask-and-how-to-use-it-effectively/)

man or help:

    chmod
    sudo
    su
    chown
    chgrp
    id
    groups
    adduser
    useradd
    addgroup

# Learning Objectives

    What are the three user-based permission groups in Linux
    What are the Linux commands chmod, sudo, su, chown, and chgrp used for
    What is the purpose of the setuid and setgid in Linux file permissions, and how do you use them
    What is the difference between the chown and chgrp commands
    What are some best practices for managing file permissions on Linux
    How can you audit file permissions changes on your system
    What is Umask in Linux



Task 0


0. Who can add a new user in Linux!

Write a bash script that generates a new user and sets a password for that specific user.

    Your script should accept a username as an arguments $1.
    Your script should accept a password as an arguments $2.


Task 1

Write a bash script that generates a new group, changes the ownership of the file to the new group and sets permissions for it.

    Your script should accept a group as an arguments $1.
    Your script should accept the file as an arguments $2.
    You should grant read and execute permissions to the newgroup on the file


2. Let's Add some fun !

Write a bash script that allows the user to execute the script without entering a password.

    Your script should accept the user as an arguments $1.
    File lines length = 2


3. SUID hunting, Known Exploits!

Write a bash script that searches for SUID vulnerabilities in a specified directory.

    Your script should accept the target directory as an arguments $1.


4. Handle the SUID bit like a hot potato fun, but use it wisely!

Write a bash script that lists all files with SUID set in a given directory

    Your script should accept the directory as an arguments $1.


5. Group hug your files with Setgid!

Write a bash script that lists all files with SGID set in a given directory

    Your script should accept the directory as an arguments $1.



6. Finding files with setuid or setgid!

Write a bash script that Finds all files modified in the last 24 hours with SUID or SGID set and lists detailed information about those files .

    Your script should accept the directory as an arguments $1.
    You should use -mtime option.



7. Others can read the files, but no writing privileges allowed—because files deserve their secrets too!

Write a bash script that Changes permissions of all files in a directory to read-only for others without changing owner/group permissions.

    Your script should accept the directory as an arguments $1.



8. Changing file owners, one friendship at a time!

Write a bash script that Changes permissions that changes the owner of files in a directory to user3, but only if the current owner is user2

    Your script should accept the directory as an arguments $1.



9. Empty files got a promotion – now they're living large with full permissions!

Write a bash script that finds all empty files in a directory and adds full permissions for everyone to these files.

    Your script should accept the directory as an arguments $1.



	
