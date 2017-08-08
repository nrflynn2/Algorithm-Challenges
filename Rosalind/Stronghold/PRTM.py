import sys

def monoisotopic_mass(seq):
    string = """A   71.03711
    C   103.00919
    D   115.02694
    E   129.04259
    F   147.06841
    G   57.02146
    H   137.05891
    I   113.08406
    K   128.09496
    L   113.08406
    M   131.04049
    N   114.04293
    P   97.05276
    Q   128.05858
    R   156.10111
    S   87.03203
    T   101.04768
    V   99.06841
    W   186.07931
    Y   163.06333"""

    mass = 0
    mass_string = ''

    string_sep = string.split()
    string_dict = dict(zip(string_sep[0::2], string_sep[1::2]))

    for i in range(0, len(seq)):
        mass_string = string_dict[seq[i]]
        mass_string = mass_string.replace('\n','')
        mass += float(mass_string) 

    return mass

def main():
    with open(sys.argv[1]) as f:
        data = f.read()
    print(monoisotopic_mass(data.strip('\n')))

main()
