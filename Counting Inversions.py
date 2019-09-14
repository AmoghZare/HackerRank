#!/bin/python3
#

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
    if len(arr) == 1:
        return arr
    else:
        a = arr[:len(arr)/2]
        b = arr[len(arr)/2:]
        a = mergeSort(a)
        b = mergeSort(b)
        c = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1
        c += a[i:]
        c += b[j:]
    return c

def swap(arr,position1,position2):
    temp = arr[position1]
    arr[position1] = arr[position2]
    arr[position2] = temp
    return

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
