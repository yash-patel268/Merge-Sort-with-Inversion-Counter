#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    # Write your code here
    counter = 0
    arrayLength = len(arr)

    if arrayLength > 1 and arrayLength<=100000:
        firstHalf = firstArray = secondArray = secondHalf = x = y = k = 0

        firstHalf = arrayLength//2
        secondHalf = arrayLength-firstHalf
        
        firstArray = arr[:firstHalf]
        secondArray = arr[firstHalf:]  

        counter += insertionSort(firstArray) 
        counter += insertionSort(secondArray)
        
        while x < firstHalf and y < secondHalf:
            if firstArray[x] <= secondArray[y]:
                arr[k] = firstArray[x]
                x+=1
            else:
                arr[k] = secondArray[y]
                y+=1
                counter += firstHalf-x
            k+=1
            
        while x < firstHalf:
            arr[k] = firstArray[x]
            x+=1
            k+=1
            
        while y < secondHalf:
            arr[k] = secondArray[y]
            y+=1
            k+=1
             
    return(counter)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
