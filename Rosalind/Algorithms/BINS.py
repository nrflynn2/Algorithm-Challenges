import sys

def bins(key, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = round((left + right)/2)
        if arr[mid] > key: right = mid - 1
        elif arr[mid] < key: left = mid + 1
        else: return mid + 1
    return -1

def find_index(arr1, arr2):
    idx = []
    for i in arr2:
        idx.append(bins(i, arr1))
    return idx

def main():
    with open(sys.argv[1]) as f:
        data = f.read().split()

    data = [int(i) for i in data]

    ordered = data[2:(2+data[0])]
    lookup = data[2+data[0]:]

    idx = find_index(ordered, lookup)
    idx = [str(i) for i in idx]
    print(' '.join(idx))

main()
