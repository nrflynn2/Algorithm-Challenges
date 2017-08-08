'''
RNA Splicing
------------
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string ss (of length at most 1 kbp) and a collection of substrings of ss acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of ss. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
--------------
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output
-------------
MVYIADKQHVASREAYGHMFKVCA
'''

import sys
from utils import *
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

def splc(seq, introns):
    for intron in introns:
        seq = seq.replace(intron, '')
    my_seq = Seq(seq)
    return my_seq.translate(to_stop=True)

def main():
    records = []
    with open(sys.argv[1]) as f:
        for name, seq in read_fasta(f):
            records.append(seq)
    result = splc(records[0], records[1:])
    print(result)

main()
