import sys
from collections import Counter

def count(seq, k):
    c = Counter()
    result = []
    
    for idx, char in enumerate(seq):
        kmer = seq[idx:idx+k]
        c[kmer] += 1

    mode = (c.most_common(1))[0][1]
    for i in c.most_common():
        if i[1] == mode:
            result.append(i[0])

    return ' '.join(result)

def main():
    with open(sys.argv[1]) as f:
        data = f.read()

    (seq, kmer) = data.split()
    result = count(seq, int(kmer))
    print(result)

main()
