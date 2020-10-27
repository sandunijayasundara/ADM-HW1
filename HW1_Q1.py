""""----------------------- Q1_Part_1 1 Say "Hellow World!" with python------------------"""
print ("Hello, World!")

""""----------------------- Q1_Part_1 2 Python If Else ------------------"""
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
    if(n%2!=0):
        print("Weird")
    else:
        if(n in range(6,21)):
            print("Weird")
        else:
            print("Not Weird")

""""----------------------- Q1_Part_1 3 Arithmatic Operators ------------------"""
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)

""""----------------------- Q1_Part_1 4 Python : Division ------------------"""
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a//b)
    print(a/b)

""""----------------------- Q1_Part_1 5 Write a function ------------------"""
if __name__ == '__main__':
    n = int(raw_input())
    for n in range(0,n):
        print(n**2)


""""----------------------- Q1_Part_1 7 Print Function ------------------"""
 __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")


""""----------------------- Q1_Part_1 6 Write a function ------------------"""
def is_leap(year):
    leap = False
    
    if((year%400==0) or ((year%4==0) and year%100!=00)):
        leap="True"
    return leap


""""----------------------- Q1_Part_2 1 list Comprehensions ------------------"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arr = []

    for i in range(x+1):
        for j in range(y+1):
            for k in range (z+1):
                if (i+k+j != n):
                    li=[i,j,k]
                    arr.append(li)

    print(arr)

""""----------------------- Q1_Part_2 2 Find the Runner-Up Score! ------------------"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    m_val = max(arr)
    while max(arr) == m_val:
        arr.remove(max(arr))

print(max(arr))


""""----------------------- Q1_Part_2 3 Nested Lists ------------------"""
if __name__ == '__main__':
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

""""----------------------- Q1_Part_2 4 Finding the percentage ------------------"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        inputArray = input().split()
        marks = list(map(float, inputArray[1:]))
        student_marks[inputArray[0]] = sum(marks)/float(len(marks))
    print("%.2f" % student_marks[input()])


""""----------------------- Q1_Part_2 5 Lists ------------------"""
N = int(input())
arr = []
for i in range(0,N):
    s = input().split()
    if s[0] == "insert":
        arr.insert(int(s[1]),int(s[2]))
    elif s[0]=="pop":
        arr.pop()
    elif s[0]=="sort":
        arr.sort()
    elif s[0]=="reverse":
        arr.reverse()
    elif s[0]=="remove":
        arr.remove(int(s[1]))
    elif s[0]=="append":
        arr.append(int(s[1]))
    elif s[0]=="print":
        print(arr)
    else:
        break

""""----------------------- Q1_Part_2 6 Tuples ------------------"""
n = int(input())
integer_list = map(int, input().split())
t=tuple(integer_list)
print(hash(t))


""""----------------------- Q1_Part_6 1 Calendar Module ------------------"""
import datetime 
date=str(input())
day_name= ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY','SUNDAY']
day = datetime.datetime.strptime(date, '%m %d %Y').weekday()
print(day_name[day])

""""----------------------- Q1_Part_6 2 Time Delta ------------------"""
import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


""""----------------------- Q1_Part_7 Exceptions ------------------"""
n=int(input())
for i in range(0,n):
    s=input().split()
    try:
        print(int(s[0]) // int(s[1]))
    except Exception as e:
        print('Error Code: ' + str(e))


""""----------------------- Q1_Part_9 Tuples ------------------"""
cube = lambda x:pow(x,3) # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    lis = [0,1]
    for i in range(2,n):
        lis.append(lis[i-2] + lis[i-1])
    return(lis[0:n])



""""----------------------- Q1_Part_11 1 XML  - Find the Score ------------------"""
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    score = len(node.attrib)
    for element in node.findall('.//*'):
        score += len(element.attrib)
    return score

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

""""----------------------- Q1_Part_11 2 XML 2 - Find the Maximun Depth ------------------"""
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    global maxdepth
    level += 1
    if (maxdepth < level):
        maxdepth = level
    for child in elem:
        depth(child, level)
        
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
    
    
""""----------------------- Q1_Part_12 1 Standardize Mobile Number Using Decorators ------------------"""
def wrapper(f):
    def fun(l):
        # complete the function
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

""""----------------------- Q1_Part_12 2 Decoraters Name Directory ------------------"""
def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda x: int(x[2])))

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
