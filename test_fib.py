#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fib

def test1():
    """
    verify that the main function operates as intended. 
    first simulate a command line input and check if the main function can test if the input is correct, and 
    then check if the fib() function can return expected outcome
    """
    
    argvList =["fib.py", "5"] #simulate the command line arguments
    
    expectedList=[1,1,2,3,5]
    retList=fib.main(argvList)
    
    assert type(retList) == list
    
    print(retList)
    
    assert len(retList) == len(expectedList)
    
    assert expectedList == retList
    print("test1 success")
        
    return


test1()
