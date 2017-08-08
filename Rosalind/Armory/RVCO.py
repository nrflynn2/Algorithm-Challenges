import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO

def rvco(records):
    count = 0
    for rec in records:
        my_seq = rec.seq
        rev_comp = my_seq.reverse_complement()
        if rev_comp == my_seq:
            count += 1
    return count

def main():
    with open(sys.argv[1]) as f:
        records = list(SeqIO.parse(f, 'fasta'))

    result = rvco(records)
    print(result)

main()
