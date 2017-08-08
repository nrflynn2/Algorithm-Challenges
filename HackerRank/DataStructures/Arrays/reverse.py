'''
Given an array, A, of N integers, print each element in reverse order as a single line of space-separated integers.

Input Format
The first line contains an integer, N (the number of integers in ). 
The second line contains N space-separated integers describing A.

Output Format
Print all  integers in  in reverse order as a single line of space-separated integers.

Sample Input
4
1 4 3 2

Sample Output
2 3 4 1
'''

#!/bin/python3

import sys

def main():
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

    temp = []
    for i in range(n-1, -1, -1):
        temp.append(arr[i])
    
    temp = [str(x) for x in temp]
    print(' '.join(temp))

main()
