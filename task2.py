#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
def largest(a):


    a.sort()
    num=a[0]
    homem = a[-1]
    print(num)
    print(homem)
    return (num)

joshList = [175,28,34,420,5,6,7,7,69]
largest(joshList)
