import sys

def process(f):
    seq = f[0]
    path = f[6]
    Ax = float(f[15])
    Ay = float(f[16])
    Az = float(f[17])
    Bx = float(f[19])
    By = float(f[20])
    Bz = float(f[21])
    return (seq, path, Ax, Ay, Az, Bx, By, Bz)

def prob(seq, path, Ax, Ay, Az, Bx, By, Bz):
    p = 1
    for let, state in zip(seq, path):
        if state == 'A':
            if let == 'x':
                p = p*Ax
            elif let == 'y':
                p = p*Ay
            elif let == 'z':
                p = p*Az
        elif state == 'B':
            if let == 'x':
                p = p*Bx
            elif let == 'y':
                p = p*By
            elif let == 'z':
                p = p*Bz

    return p

def main():
    with open(sys.argv[1]) as f:
        data = f.read().split()

    (seq, path, Ax, Ay, Az, Bx, By, Bz) = process(data)
    
    result = prob(seq, path, Ax, Ay, Az, Bx, By, Bz)
    print(result)

main()
