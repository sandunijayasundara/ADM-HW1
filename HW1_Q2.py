"""-----------------------Q1.2.2-------------------------"""
num_stu = input()
mark_list= []
stu_mark = []
records = []
names=[]
for i in range(int(num_stu)):
    name = input()
    score = float(input())
    if score not in mark_list:
        mark_list.append(score)
    records.append([name,score])
sorted_marks = sorted(mark_list)
if len(sorted_marks)>1:
    for i in range(0,len(records)):
        if records[i][1] == sorted_marks[1]:
            names.append(records[i][0])
name_final = sorted(names)
for i in range(len(name_final)):
    print(name_final[i])

"""-----------------------Q1.2.1-------------------------"""

n = int(input())
arr = list(map(int, input().strip().split()))[:n]
m_val = max(arr)
while max(arr) == m_val:
    arr.remove(max(arr))
print(max(arr))

"""----------------------- Q2.1 Candle Problem ------------------"""
def birthdayCakeCandles(candles):
    num_can = []
    max_num = max(candles)
    for i in range(len(candles)):
        if candles[i] == max_num:
            num_can.append(max_num)
    return len(num_can)

candles_count = int(input())
candles = list(map(int, input().rstrip().split()))
result = birthdayCakeCandles(candles)
print(result)

"""----------------------- Q2.2 Kangaroo Problem ------------------"""
def kangaroo(x1, v1, x2, v2):
    if (v2<v1):
        meet = (x1 - x2) % (v2 - v1)
        if meet == 0:
            result =  "YES"
        else:
            result = "NO"
    else:
        result = "NO"
    return result

x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
result = kangaroo(x1, v1, x2, v2)
print(result)

"""----------------------- Q2.3 Strange Advertising ------------------"""
n = int(input())
shared = []
liked = []
cumu = []
for i in range (n):
    if i>0:
        shared.append((shared[i-1]//2)*3)
        liked.append(shared[i]//2)
        cumu.append(cumu[i-1]+liked[i])
    else:
        shared.append(5)
        liked.append(5//2)
        cumu.append(2)
print(max(cumu))

"""----------------------- Q2.4 Recursive Digit Sum ------------------"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    digits = map(int, list(n))
    return get_super_digit(str(sum(digits) * k))

def get_super_digit(p):
    if len(p) == 1:
        return int(p)
    else:
        digits = map(int, list(p))
        return get_super_digit(str(sum(digits)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

"""----------------------- Q2.5 Insertion Sort - Part 1 ------------------"""
import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def print_arr(lis):
    for i in range(len(lis)): 
        print(lis[i])
    
def insertionSort1(n, arr):
    lis = []
    num = arr[n-1]
    for i in range(len(arr)-1,-1,-1):
        if arr[i-1]>num:
            if i==0:
                arr[i]=num
            else:
                arr[i] = arr[i-1]
            print(*arr)
                        

        else:
            arr[i]=num
            print(*arr)
            break
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


"""----------------------- Q2.5 Insertion Sort - Part 2 ------------------"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for q in range(1,len(arr)):
            for i in range(q):
                if(arr[q] < arr[i]):
                   temp=arr[q]
                   arr[q]=arr[i]
                   arr[i]=temp
            print(*arr)
            print

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
