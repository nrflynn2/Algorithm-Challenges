import sys

def complement(dna):
    for idx, item in enumerate(dna):
        if dna[idx] == "G":
            dna[idx] = "C"
        elif dna[idx] == "C":
            dna[idx] = "G"
        elif dna[idx] == "A":
            dna[idx] = "T"
        elif dna[idx] == "T":
            dna[idx] = "A"
    return "".join(dna)

def main():
    with open(sys.argv[1]) as f:
        dna = f.read().strip()
    rev_strand = ''.join(reversed(dna))
    rev_complement_strand = complement(list(rev_strand))
    print(rev_complement_strand)

main()
