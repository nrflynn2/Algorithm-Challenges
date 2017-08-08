import sys

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n-1) + fib(n-2)

def main():
    with open(sys.argv[1]) as f:
        data = f.read()

    calc_fib = fib(int(data))
    print(calc_fib)

main()
