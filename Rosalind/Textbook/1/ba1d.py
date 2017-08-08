import sys

def find_substrings(s, t):
    motif_length = len(t)
    ss_locations = []
    for idx, bp in enumerate(s):
        ss = s[idx:idx + motif_length]
        if t == ss:
            ss_locations.append(idx)
    return ss_locations

def main():
    with open(sys.argv[1]) as f:
        data = f.read()
        t, s = data.split()
    ss_locations = find_substrings(s, t)
    for idx in ss_locations:
        print(idx, end=' ')

main()
