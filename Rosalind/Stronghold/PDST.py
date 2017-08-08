import sys
from Bio import SeqIO
import numpy as np

def dst(records):
    matrix = np.zeros((len(records), len(records)))
    n = len(records[0])
    for idx1, str1 in enumerate(records):
        for idx2, str2 in enumerate(records):
            mismatch = 0.0
            for c1, c2 in zip(str1, str2):
                if c1 != c2:
                    matrix[idx1][idx2] += 1.0

    result = matrix/n
    return(result)

def reformat(matrix):
    string = ''
    for row in matrix:
        for i in row:
            s = str(i)
            string += s + ' '
        string += '\n'

    return string

def main():
    with open(sys.argv[1]) as f:
        records = list(SeqIO.parse(f, 'fasta'))

    result = dst(records)
    result2 = reformat(result)
    print(result2)

main()
