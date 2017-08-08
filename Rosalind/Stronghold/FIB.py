import sys

def fib(n, k):
	if n < 3:
		return 1
	return fib(n-1, k) + k*fib(n-2, k)

def main():
	with open(sys.argv[1]) as f:
		data = f.read()
		n, k = data.split()

	rabbit_pairs = fib(int(n), int(k))
	print(rabbit_pairs)

main()
