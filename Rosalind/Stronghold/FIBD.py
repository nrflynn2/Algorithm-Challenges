import sys

def fibd(month, span):
    generations = [1, 1]
    count = 2
    while count < month:
        if count < span:
            generations.append(generations[-2] + generations[-1])
        elif count == span or count == span + 1:
            generations.append(generations[-2] + generations[-1] - 1)
        else:
            generations.append(generations[-2] + generations[-1] - 
                generations[count - span - 1])
        count += 1
    return generations[-1]

def main():
    with open(sys.argv[1]) as f:
        data = (f.read()).split()
    num_pairs = fibd(int(data[0]), int(data[1]))
    print(num_pairs)

main()
