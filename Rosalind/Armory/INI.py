from Bio.Seq import Seq
import sys

def dna_count(seq):
    my_seq = Seq(seq)
    A = my_seq.count("A")
    C = my_seq.count("C")
    G = my_seq.count("G")
    T = my_seq.count("T")
    return (A, C, G, T)

def main():
    with open(sys.argv[1]) as f:
        data = f.read()

    print(dna_count(data))

main()
