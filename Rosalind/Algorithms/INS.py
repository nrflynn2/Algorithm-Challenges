import sys

def insertion_sort(data):
    total = 0
    k = 0
    temp = 0

    for i in range(1, len(data)):
        k = i
        while k > 0 and data[k] < data[k-1]:
            # Swap
            data[k - 1], data[k] = data[k], data[k - 1]
            k -= 1
            total += 1

    return total

def main():
    with open(sys.argv[1]) as f:
        data = f.read()
    data = data.split()
    data = data[1:]
    data = [int(numeric_string) for numeric_string in data]
    num_swaps = insertion_sort(data)
    print(num_swaps)

main()
