#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    frequency = []
    n = len(s)
    temp = s
    for i in range(n):
        if i < len(temp):
            count = checkCount(temp[i],temp)
            frequency.append(count)
            temp = "".join(temp.rsplit(temp[i],count-1))
            temp = temp.replace('','')
    return (checkValidity(frequency))

def checkValidity(frequency):
    n = len(frequency)
    differentFlag = 0
    notPossible = 0
    differentCount = 0
    maximumFrequency = max(frequency,key=frequency.count)
    for index in range(n):
        if maximumFrequency == frequency[index]:
            differentFlag = 0
        elif maximumFrequency != frequency[index]:
            differentFlag = 1
            differentCount +=1
            if abs(maximumFrequency - frequency[index]) > 1:
                notPossible = 1
                
    if differentCount>1 or notPossible == 1:
        return 'NO'
    else:
        return 'YES'
        
def checkCount(char,string):
    n = len(string)
    count = 0
    for index in range(n):
        if char == string[index]:
            count+=1
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
