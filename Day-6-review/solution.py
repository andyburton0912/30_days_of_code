# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

n = int(input())

for i in range(0, n):
    s = str(input())
    even, odd = s[::2], s[1::2]
    print(even + ' ' + odd)