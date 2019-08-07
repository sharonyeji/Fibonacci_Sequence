#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fibonacci(n):
    """
    object: fibonacci(n)  returns the first n Fibonacci numbers in a list
    input: n- the number used to calculate the fibonacci list 
    return: retList- the fibonacci list 

    """
    if type(n) != int:
        print(n)
        print(":input not an integer")
        return False

    if n <= 0:
        print(str(n)+"not a postive integer")
        return False
    
    f1=1
    f2=1
    retList=[]

    for i in range (0,n):
        retList.append(f1)
        fn=f1+f2
        f1=f2
        f2=fn
   
    return retList

    
