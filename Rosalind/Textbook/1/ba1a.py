import sys

def count_substrings(s, t):
    count = 0
    motif_length = len(t)
    ss_locations = []
    for idx, bp in enumerate(s):
        ss = s[idx:idx + motif_length]
        if t == ss:
            count += 1
    return count

def main():
    with open(sys.argv[1]) as f:
        data = f.read()
        s, t = data.split()
    result = count_substrings(s, t)
    print(result)
main()
