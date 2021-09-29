import math
import os
import random
import re
import sys
from typing import Counter



def insertionSort(arr):
    counter = 0
    arrayLength = len(arr)

    if arraySorted(arr):
        return counter
    else:
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

def arraySorted(arr):
    arrayLength = len(arr)
    if arrayLength == 1 or arrayLength == 0:
        return True
    return arr[0] <= arr[1] and arraySorted(arr[1:])


arr = [1,20,6,4,5]
print(insertionSort(arr))

arr2 = [4,3,2,1]
print(insertionSort(arr2))

arr3=[1, 1, 1, 2, 2]
print(insertionSort(arr3))

arr4=[2, 1, 3, 1, 2]
print(insertionSort(arr4))

arr5 = [12,15,1,5,6,14,11]
print(insertionSort(arr5))

arr6=[3, 5, 7, 11, 9]
print(insertionSort(arr6))




