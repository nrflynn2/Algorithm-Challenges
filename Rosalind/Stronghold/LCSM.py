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
from utils import *

def lcsm(seqs):
    seqs = sorted(seqs)
    short_seq = seqs[0]
    other_seqs = seqs[1:]

    n = len(short_seq)
    p = ''

    for i in range(0, n):
        for j in range(n, i + len(p), -1):
            s1 = short_seq[i:j]

            matched = True
            for s2 in other_seqs:
                if s1 not in s2:
                    matched = False
                    break

            if matched:
                p = s1
                break
    return p

def main():
    records = []

    with open(sys.argv[1]) as f:
        for name, seq in read_fasta(f):
            records.append(seq)

    result = lcsm(records)
    print(result)

main()
