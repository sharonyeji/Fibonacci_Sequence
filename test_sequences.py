#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sequences

def test1():
    """
    test if the return value of fiboncci  function match the expected result
    expectedList: the expected list of fiboncci function
    retList: the listed returned by function function
    """

    expectedList=[1,1,2,3,5] 
    retList=sequences.fibonacci(5)
    
    assert type(retList) == list
    
    print(retList)
    
    assert len(retList) == len(expectedList)
    
    assert expectedList == retList
    print("test1 success")
        
    return

def test2():
    """
    out the fibonacci list for a certain valid number and verify the last number of the list
    """
    retList = sequences.fibonacci(8)
    print(retList[7])
    assert retList[7] == 21
    print("test2 success")
    return 
    
    
  
def test3():
    """
    test if fibonacci function can validate the input  
    """
    t=-1
    assert sequences.fibonacci(t) == False
    t=2.2 
    assert sequences.fibonacci(t) == False
    t=0
    assert sequences.fibonacci(t) == False

    print("input validation success")
    return



print("test1-start")
test1()

print("test2 start")
test2()

print("test3 start")
test3()





