import sys
from Bio.Seq import translate

def find_index(rna, prot):
    result = []
    for i in range(0, 6):
        i += 1
        i = str(i)
        result.append(translate(rna, table=i, stop_symbol=''))

    for idx, res in enumerate(result):
        print(res)
        if res == prot:
            return idx + 1

def main():
    with open(sys.argv[1]) as f:
        data = f.read().split()

    rna = data[0]
    prot = data[1]
    result = find_index(rna, prot)
    print(result)

main()
