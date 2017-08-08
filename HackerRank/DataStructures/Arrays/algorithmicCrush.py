'''
Input Format
First line will contain two integers N and M separated by a single space.
Next M lines will contain three integers a, b and k separated by a single space.
Numbers in list are numbered from 1 to N.

Output Format
A single line containing maximum value in the updated list.

Sample Input
5 3
1 2 100
2 5 100
3 4 100

Sample Output
200
'''
import sys

def main():
    n, m = [int(n) for n in input().split(' ')]
    diffArray = [0]*(n+1)
    
    for i in range(m):
        a, b, k = [int(n) for n in input().split(' ')]
        
        diffArray[a] += k
        if((b + 1) <= n): diffArray[b + 1] -= k
     
    max_sum = 0
    curr_sum = 0
    for x in diffArray:
        curr_sum += x
        if max_sum < curr_sum: max_sum = curr_sum
    print(max_sum)
    
main()
