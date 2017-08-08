'''
Input Format
There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in A will be in the inclusive range of -9 to 9.

Output Format
Print the largest (maximum) hourglass sum found in A.

Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19
'''

#!/bin/python3

import sys

def max_hourglass_sum(arr):
    max_sum = -sys.maxsize
    for i in range(0, 4):
        for j in range(0, 4):
            curr_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] + arr[i+1][j+1]
            if curr_sum > max_sum: max_sum = curr_sum
    return max_sum

def main():
    arr = []
    for arr_i in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)
    result = max_hourglass_sum(arr)
    print(result)

main()
