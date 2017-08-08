import sys

def count_difference(str1, str2):
	count = 0
	for a, b in zip(str1, str2):
		if a != b:
            		count += 1
	return count

def main():
	with open(sys.argv[1]) as f:
		data = f.read()
		s, t = data.split()
	num_diff = count_difference(s, t)
	print(num_diff)

main()
