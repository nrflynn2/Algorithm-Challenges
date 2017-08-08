import sys
from Bio.Seq import Seq, translate
from Bio.Alphabet import IUPAC

def max_orf(seq):
    my_seq = Seq(seq, IUPAC.unambiguous_dna)
    rev_c = my_seq.reverse_complement()
    longest = None
    seq_arr = [my_seq, rev_c]

    for i in range(0, 3):
        for dna in seq_arr:
            prot = translate(dna[i:])
            prot = prot.split('*')
            for p in prot:
                if not longest or len(p) > len(longest):
                    longest = p
 
    return longest

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip('\n')

    result = max_orf(data)
    print(result)

main()
