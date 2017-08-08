import sys
from collections import Counter

def get_freq(data):
    c = Counter()
    for word in data:
        c[word] += 1
    print(c)
    return c

def main():
    flag = 1
    with open(sys.argv[1]) as f:
        data = f.read()
    data = data.split()
    word_dict = get_freq(data)
    for key, value in word_dict.items():
        print (key, value)

main()
