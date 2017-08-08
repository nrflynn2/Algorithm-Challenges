# Finding a Shared Motif
# ======================
# 
# A common substring of a collection of strings is a substring of every member
# of the collection. We say that a common substring is a longest common
# substring if a longer common substring of the collection does not exist. For
# example, CG is a common substring of ACGTACGT and AACCGGTATA, whereas GTA is a
# longest common substring. Note that multiple longest common substrings may
# exist.
# 
# Given: A collection of k DNA strings (of length at most 1 kbp each; k≤100).
# 
# Return: A longest common substring of the collection. (If multiple solutions
#         exist, you may return any single solution.)
# 
# Sample Dataset
# --------------
# GATTACA
# TAGACCA
# ATACA
# 
# Sample Output
# -------------
# AC

import sys
import math
from utils import *

def common_substr(seq_0, seqs, start, length):
    for i in range(start, len(seq_0) - length + 1):
        substr = seq_0[i:i+length]
        for seq in seqs:
            if substr not in seq:
                break
        else:
            return (i, substr)
    return (-1, '')

def longest_common_substr(seqs):
    seq_0 = seqs.pop()
    low = 0
    high = len(seq_0) + 1
    start = 0
    longest_substr = ''

    while low + 1 < high:
        mid = math.floor((low + high) / 2)
        idx, substr = common_substr(seq_0, seqs, start, mid)
        if idx > -1:
            start = idx
            longest_substr = substr
            low = mid
        else:
            high = mid

    seqs.append(seq_0)
    return longest_substr

def main():
    records = []

    with open(sys.argv[1]) as f:
        for name, seq in read_fasta(f):
            records.append(seq)

    result = longest_common_substr(records)
    print(result)

main()
