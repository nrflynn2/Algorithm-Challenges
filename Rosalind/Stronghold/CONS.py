import sys
import numpy as np
from collections import Counter

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

def profile(data):
    matrix = np.zeros((4, len(data[0])))
    for seq in data:
        c = Counter()
        for idx, nt in enumerate(seq):
            c[nt] += 1
            matrix[0][idx] += c['A']
            matrix[1][idx] += c['C']
            matrix[2][idx] += c['G']
            matrix[3][idx] += c['T']
            c.clear()
        c.clear()
    return matrix.astype(int)

def consensus(matrix):
    string = []
    for col in matrix.T:
        idx = 0
        best = 0
        for i,n in enumerate(col):
            if n > best:
                best = n
                idx = i
        if idx == 0: string.append('A')
        elif idx == 1: string.append('C')
        elif idx == 2: string.append('G')
        elif idx == 3: string.append('T')
    return ''.join(string)

def main():
    seq_array = []
    with open(sys.argv[1]) as fp:
        for name, seq in read_fasta(fp):        
            seq_array.append(seq)

    profile_matrix = profile(seq_array)
    consensus_string = consensus(profile_matrix)

    print(consensus_string)
    for row in profile_matrix:
        print(' '.join(map(str, row)))
main()

