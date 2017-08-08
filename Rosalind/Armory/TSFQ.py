import sys
from Bio import SeqIO

def main():
    with open(sys.argv[1]) as f:
        data = f.read()

    SeqIO.convert('rosalind_tfsq.txt', 'fastq', 'ros.txt', 'fasta')

main()
