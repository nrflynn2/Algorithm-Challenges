import sys

def probability_dominant_allele(k, m, n):
	t = k + m + n
	p_dom = (k*(k-1) + 2*k*m + 2*k*n + m*n + m*(m-1)*(0.75)) / (t*(t-1))
	return p_dom

def main():
	with open(sys.argv[1]) as f:
		data = f.read()
		k, m, n = data.split()

	p_dom = probability_dominant_allele(int(k),int(m),int(n))
	print(p_dom)
	
main()
