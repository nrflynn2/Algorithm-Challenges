import sys, resource
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

def ms(arr):
    m = int(len(arr)/2)
    if len(arr) < 2:
        return arr

    left = ms(arr[:m])
    right = ms(arr[m:])

    result = merge(left, right)
    return result

def main():
    with open(sys.argv[1]) as f:
        data = f.read().split()

    data = [int(i) for i in data]
    result = ms(data[1:])
    result = [str(i) for i in result]
    print(' '.join(result))

main()
