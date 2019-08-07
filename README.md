# CS510 CW 3

**Author(s):** **Sharon, Kynan, Jianhua**

[![Build Status](https://travis-ci.org/chapman-cs510-2017f/cw-03-YOURNAME.svg?branch=master)](https://travis-ci.org/chapman-cs510-2017f/cw-03-YOURNAME)

## Specification

Complete the following exercises, saving your solutions in the indicated files. For Python files that include test functions, GitHub will automatically run your tests with ```nosetests``` on every commit, indicating any failures via the Travis framework in the build status image above. (Note that in CoCalc, you will need to call python3 explicitly via ```python3 -m nose``` instead of running ```nosetests``` directly.)

1. Create a python file ```sequences.py``` with a function ```fibonacci(n)``` that returns the first ```n``` Fibonacci numbers in a list. (Recall that each successive Fibonacci number is defined by summing the previous two, starting with the numbers 1 and 1.) Commit to GitHub.
    * Hint: Use the python template file in the info repository to make sure you have the correct structure. You should have a #! line at the top, a module docstring, function definitions, function docstrings, and informative comments in your code.
    * Example: ```fibonacci(5)``` should return ```[1,1,2,3,5]``` 
    * Example: the last element of ```fibonacci(1000)``` should be: 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    * In the separate test module ```test_sequences.py```, examine the example test function and write 2 more that verify whether this function outputs the correct results. Verify that running ```python3 -m nose``` in a terminal successfully finds and runs all three test functions.
    * Make sure the function only returns a list. Have it throw an exception if a nonsensical argument ```n``` is given (i.e., not a positive integer).
1. Write an executable python script ```fib.py``` that loads ```sequences.py``` as a module, reads one command line argument ```n```, runs ```fibonacci(n)```, then prints the last element of the result. Commit the script to GitHub.
    * If an exception is thrown, catch it and print an appropriate error message to the screen. 
    * Make sure you use the template to set up a proper ```main(argv)``` method called from inside a ```___main___``` environment. Your script should not execute any code if it is loaded as a module.
    * Remember to make your script executable with ```chmod```.
    * In a separate test module ```test_fib.py```, write a test function to verify that the main function operates as intended. Verify that running ```python3 -m nose``` in a terminal successfully finds and runs this test function.
1. Write a bash script ```runfibs.sh``` that uses bash to run ```fib.py``` for arguments ```n``` from 1 to 10000.  For each argument, redirect the output of the script to a comma-separated-value file ```fibs.csv``` such that each fibonacci number is separated by a comma (with no newlines). Commit the shell script (but not the csv file) to GitHub.
    * If a ```fibs.csv``` file already exists, back it up: move the existing file to ```fibs.csv.bak```, then create the new file. Inform the user that this backup occurred.
    * If a backup already exists, inform the user, then exit the program with an error code (not 0) before any files are overwritten.


## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

1. Python and Bash are so seemlessly connected.
2. Python is more friendly than bash to me.
3. Bash is so flexible in manipulating strings.
4. Test is necessary! Assert is great.
5. In bash , local_argv is the argument list, program name is first arugment
6. Echo -e "$j,\c" >> fibs.csv  ## >> operator. This will append data from a command to the end of a text file. -e and \c make the appendation with no newlines in the file.
7. Using the main function will definitely prove to be useful as functions and python scripts get more complicating.


## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**Sharon, Jianhua, Kynan**
