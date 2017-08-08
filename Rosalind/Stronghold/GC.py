import sys
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

def gc_content(seq):
    cnt = Counter()
    for nt in seq:
        cnt[nt] += 1
    return 100*((cnt['G'] + cnt['C'])/sum(cnt.values()))

def main():
    highest_gc = 0
    string_gc = None

    with open('rosalind_gc.txt') as fp:
        for name, seq in read_fasta(fp):
            gc_percent = gc_content(seq)
            if(gc_percent > highest_gc): 
                highest_gc = gc_percent
                string_gc = name
            
    print(string_gc)
    print(highest_gc)

main()
