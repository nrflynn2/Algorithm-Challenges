import sys

rna = list(sys.stdin.read().strip())

for idx, item in enumerate(rna):
	if rna[idx] == "T":
		rna[idx] = "U"

print("".join(rna))

# Interesting alternative below
# def dna_to_rna(strng):
#    return 'U'.join(strng.split('T'))
