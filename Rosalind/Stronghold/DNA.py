import sys
 
dna = sys.stdin.read()
dna2 = dna.strip()
for i in 'ACGT':
    print dna2.count(i)
