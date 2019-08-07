#!/bin/bash

#Write a bash script runfibs.sh that uses bash to run fib.py for arguments n from 1 to 10000. For each argument, redirect the output of the script to a comma-separated-value file fibs.csv such #that each fibonacci number is separated by a comma (with no newlines). Commit the shell script (but not the csv file) to GitHub.
#If a fibs.csv file already exists, back it up: move the existing file to fibs.csv.bak, then create the new file. Inform the user that this backup occurred.
#If a backup already exists, inform the user, then exit the program with an error code (not 0) before any files are overwritten.
# [1,1,2,3,5]
#
#
#
i=1

FILE="fibs.csv.bak"
if [ -e "$FILE" ]
   then
       echo "File $FILE exist, exit -1"
       exit -1
fi

FILE="fibs.csv"
if [ -e "$FILE" ]
   then
       mv "$FILE" fibs.csv.bak
   fi

while [ $i -le 10000 ]
  do 
  echo "n="$i
  outputString=$(python fib.py $i) #strange@@@, fib.py print a string (line 19 print(retList)) and Bash will convert to an array
  echo outputString:$outputString
  
  for j in $outputString;
  do
     echo -e "$j,\c" >> fibs.csv  ## >> operator. This will append data from a command to the end of a text file. -e and \c make the appendation with no newlines in the file
  done

  ((i=i+1))
  echo "------"
 done
