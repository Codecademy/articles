# NOTE: This file is intended only to showcase 
#       the code snippets used in the article,
#       "Top 10 Bash Commands" (ordered by appearance).

# 1. pwd

pwd
# Users/brandond/Desktop/portfolio site

# 2. cd

pwd
# Users/brandond/Desktop

cd new-directory

pwd
# Users/brandond/Desktop/new-directory

pwd
# Users/brandond/Desktop

cd new-directory

pwd
# Users/brandond/Desktop/new-directory

pwd
# Users/brandond/Desktop

cd new-directory/sub-sub-directory

pwd
# Users/brandond/Desktop/new-directory/sub-sub-directory.

pwd
# Users/brandond/Desktop/new-directory/sub-sub-directory

cd .. 

pwd 
# Users/brandond/Desktop/new-directory

pwd 
# Users/brandond/Desktop/new-directory

cd ../..

pwd
# Users/brandond

pwd
# Users/brandond

cd Desktop/new-directory

pwd 
# Users/brandond/Desktop/new-directory

cd ../..
pwd 
# Users/brandond

# 3. mkdir

pwd
# Users/brandond/Desktop

mkdir new-directory

cd new-directory

pwd
# Users/brandond/Desktop/new-directory

# 4. touch

pwd
# Users/brandond/Desktop/new-directory

touch fileA.txt

touch fileB.txt fileC.txt

touch sub-sub-directory/fileD.txt

# 5. ls

pwd
# Users/brandond/Desktop/new-directory
ls 
# fileA.txt        fileB.txt
# fileC.txt        sub-sub-directory

ls -R
# fileA.txt        fileB.txt
# fileC.txt        sub-sub-directory

# ./sub-sub-directory:
# fileD.txt

ls sub-sub-directory
# fileD.txt

# 6. echo

echo Hello, World!
# Hello, World!

echo "Hello, World!"
# bash: !": event not found 

echo 'Hello, World!'
# Hello, World!

# 7. mv

mv source target

mv source(s) directory

ls
# myFile.txt

mv myFile.txt file.txt

ls
# file.txt

ls
# file.txt        myFile.txt 

cat file.txt
# This is the text from file.txt 

cat myFile.txt
# This is the text from myFile.txt

mv -i file.txt myFile.txt 
# overwrite myFile.txt? (y/n [n]) y

cat myFile.txt
# This is the text from file.txt

ls
# dir1        dir2

ls dir1
# fileA.txt        fileB.txt

ls dir2
# fileC.txt        fileD.txt

mv dir1 dir2 

ls
# dir 2

ls
# dir1        fileC.txt        fileD.txt

ls dir2/dir1
# fileA.txt        fileB.txt

ls 
# dir 2

mv dir2 dir3

ls
# dir3

ls dir3
# dir1        fileC.txt        fileD.txt

# 8. rm

cd dir1

ls
# fileA.txt        fileB.txt

rm fileA.txt

ls
# fileB.txt

cd ..

pwd
# Users/brandond/Desktop/dir3

ls
# dir1        fileC.txt        fileD.txt

rm -r dir3/dir1

ls
# fileC.txt        fileD.txt

# 9. grep

ls
# fileA.txt        fileB.txt

grep "This is" fileA.txt fileB.txt
# fileA.txt: This is file A.
# fileB.txt: This is file B.

# 10. chmod

ls
# example.txt

ls -l
# total 0
# -rw-r--r-- 1 brandond codecademy 0 Sept  1 16:17 example.txt

chmod 777 example.txt

ls -l
# -rwxrwxrwx 1 user group date-time-of-last-update example.txt