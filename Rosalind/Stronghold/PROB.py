import sys
import math
from collections import Counter

def prob(seq, gc_array):
    result = []
    gc_prob = 0
    at_prob = 0

    c = Counter()
    for nt in seq:
        c[nt] += 1

    num_gc = c['G'] + c['C']
    num_at = c['A'] + c['T']

    for i in gc_array:
        gc_prob = i/2
        at_prob = (1-i)/2
        raw_prob = pow(gc_prob, num_gc) * pow(at_prob, num_at)
        log_prob = math.log10(raw_prob)
        result.append(log_prob)

    return result

def main():
    with open(sys.argv[1]) as f:
        data = f.read().split()
    
    seq = data[0]
    gc_content = [float(i) for i in data[1:]]
    seq_prob = prob(seq, gc_content)
    seq_prob = [str(round(i, 3)) for i in seq_prob]
    print(' '.join(seq_prob))

main()
