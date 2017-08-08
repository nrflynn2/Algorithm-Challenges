import sys
import numpy as np

def degree(data):
    matrix = np.zeros((data[0] + 1, data[1] + 1))
    for int1, int2 in zip(data[2::2], data[3::2]):
        matrix[int1][int2] = 1
        matrix[int2][int1] = 1
    deg = []
    total = 0
    for row in matrix:
        total = 0
        for idx, i in enumerate(row):
            if i == 1:
                total += np.sum(matrix[idx])
        deg.append(total)
    return deg

def main():
    with open(sys.argv[1]) as f:
        data = f.read().split()

    data = [int(i) for i in data]
    result = degree(data)
    result = [str(int(i)) for i in result]
    print(' '.join(result))

main()
