import sys

def process(f):
    path = f[0]
    AAprob = float(f[8])
    ABprob = float(f[9])
    BAprob = float(f[11])
    BBprob = float(f[12])
    return (path, AAprob, ABprob, BAprob, BBprob)

def path_prob(path, AA, AB, BA, BB):
    init = 0.5
    for idx, state in enumerate(path):
        if idx < len(path) - 1:
            if state == 'A':
                if path[idx + 1] == 'A':
                    init = init * AA
                elif path[idx + 1] == 'B':
                    init = init * AB
            elif state == 'B':
                if path[idx + 1] == 'A':
                    init = init * BA
                elif path[idx + 1] == 'B':
                    init = init * BB
    return init

def main():
    with open(sys.argv[1]) as f:
        data = f.read().split()

    (path, AAprob, ABprob, BAprob, BBprob) = process(data)
    result = path_prob(path, AAprob, ABprob, BAprob, BBprob)
    print(result)

main()
