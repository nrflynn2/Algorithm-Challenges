import sys
from collections import Counter

'''Alternative: Moore's Voting Algorithm
def majority_element(a):
    # Initialize the candidate element and count.
    candidate, count = a[0], 0
    # Run through the list, updating the count and changing candidates as necessary.
    for element in a:
        count += [-1, 1][element == candidate]
        if count == 0:
            candidate, count = element, 1

    # Check if the candidate is indeed the majority element, returning the appropriate result.
    return [-1, candidate][a.count(candidate) > len(a)/2]
'''

def maj(seq):
    c = Counter()
    for num in seq:
        c[num] += 1

    maj_ele = c.most_common(1)
    if c[maj_ele[0][0]] > (len(seq)/2):
        return maj_ele[0][0]
    else:
        return -1

def main():
    with open(sys.argv[1]) as f:
        data = f.read().split()

    data = [int(i) for i in data]
    n = data[0]
    l = data[1]

    result = []
    for i in range(0, n):
        result.append(maj(data[2+l*i:2+l+l*i]))

    result = [str(i) for i in result]
    print(' '.join(result))

main()
