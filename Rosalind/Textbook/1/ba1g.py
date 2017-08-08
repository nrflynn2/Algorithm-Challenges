import sys

def hamm(str1, str2):
    count = 0
    for nt1, nt2 in zip(str1, str2):
        if nt1 != nt2:
            count += 1
    return count

def main():
    with open(sys.argv[1]) as f:
        data = f.read().strip('\n').split()

    result = hamm(data[0], data[1])
    print(result)

main()
