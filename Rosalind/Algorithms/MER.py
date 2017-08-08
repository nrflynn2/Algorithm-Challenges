import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

def merge(seq1, seq2):
    arr = []
    if seq1 == [] and seq2 == []:
        return arr
    if seq1 != [] and seq2 == []:
        return arr + seq1
    if seq1 == [] and seq2 != []:
        return arr + seq2
    if seq1 != [] and seq2 != []:
        if seq1[0] < seq2[0]:
            arr.append(seq1[0])
            arr = arr + merge(seq1[1:], seq2)
        else:
            arr.append(seq2[0])
            arr = arr + merge(seq1, seq2[1:])
    return arr

def main():
    with open(sys.argv[1]) as f:
        data = f.read().split()

    data = [int(i) for i in data]
    seq1 = data[1:data[0]+1]
    seq2 = data[data[0]+2:]
    result = merge(seq1, seq2)
    result = [str(i) for i in result]
    print(' '.join(result))

main()
