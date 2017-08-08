import sys

def main():
    with open(sys.argv[1]) as f:
        data = f.read()

    data = data.split()
    dim = int(data[0])
    adj_list = [int(i) for i in data[1:]]
    print(dim - 1 - len(adj_list)/2)

main()
