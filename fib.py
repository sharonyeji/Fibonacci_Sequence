#!/usr/bin/env python3
import sequences

def main(local_argv):
    """
    local_argv is the argument list, progrom name is first arugment
    this function prints the fibonacci list calcuated by the command line argument n 
    
    """
   
    if len(local_argv) != 2:
        print("must add one and only one command argument ")
        return

        
    argument_n = int(local_argv[1]) #remember, this is the 2nd argument in command line
    retList =sequences.fibonacci(argument_n)
    #print("fibonacci("+str(argument_n)+")=")
    returnStr = ''
    for item in retList:
        returnStr += str(item)+' '
    print(returnStr)
    return retList

# After the body of the module, you can optionally create a protected main 
# section to place executable scripting code.

if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. It is not run when imported as
    # a module.
    
    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Note that sys.argv will contain all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    import sys
    main(sys.argv)
    
