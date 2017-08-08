import sys

def calc_permutations(data):
    prob_dict = {'F': 2,'L': 6, 'M': 1, 'A': 4, 'S':6, 'Y':2, 'C':2, 'W':1, 
        'P':4, 'H':2, 'Q':2, 'R':6, 'I':3, 'T':4, 'N':2, 'K':2, 'V':4, 
        'D':2, 'E':2, 'G':4}
    total = 3 # Start at 3 to account for stop codon
    for aa in data:
        total = total * prob_dict[aa]
    return total % 1000000

def main():
    with open(sys.argv[1]) as f:
        data = f.read()
    data = data.strip('\n')
    print(calc_permutations(data))

main()
