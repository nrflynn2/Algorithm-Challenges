import sys

def conversion(s):
    if s == 'UUU' or s == 'UUC':
        return 'F'
    elif s == 'UUA' or s == 'UUG' or s == 'CUU' or s == 'CUC' or s == 'CUA' or s == 'CUG':
        return 'L'
    elif s == 'UAU' or s == 'UAC':
        return 'Y'
    elif s == 'UCU' or s == 'UCC' or s == 'UCA' or s == 'UCG' or s == 'AGU' or s == 'AGC':
        return 'S'
    elif s == 'UAA' or s == 'UAG' or s == 'UGA':
        return ''
    elif s == 'UGC' or s == 'UGU':
        return 'C'
    elif s == 'UGG':
        return 'W'
    elif s == 'CCU' or s == 'CCC' or s == 'CCA' or s == 'CCG':
        return 'P'
    elif s == 'CAU' or s == 'CAC':
        return 'H'
    elif s == 'CAA' or s == 'CAG':
        return 'Q'
    elif s == 'CGU' or s == 'CGC' or s == 'CGA' or s == 'CGG' or s == 'AGA' or s == 'AGG':
        return 'R'
    elif s == 'AUU' or s == 'AUC' or s == 'AUA':
        return 'I'
    elif s == 'AUG':
        return 'M'
    elif s == 'ACU' or s == 'ACC' or s == 'ACA' or s == 'ACG':
        return 'T'
    elif s == 'AAU' or s == 'AAC':
        return 'N'
    elif s == 'AAA' or s == 'AAG':
        return 'K'
    elif s == 'GUU' or s == 'GUC' or s == 'GUA' or s == 'GUG':
        return 'V'
    elif s == 'GCU' or s == 'GCC' or s == 'GCA' or s == 'GCG':
        return 'A'
    elif s == 'GGU' or s == 'GGC' or s == 'GGA' or s == 'GGG':
        return 'G'
    elif s == 'GAU' or s == 'GAC':
        return 'D'
    elif s == 'GAA' or s == 'GAG':
        return 'E'

def translate(rna):
    prot = []
    for idx in range(0, len(rna)-3, 3):
        codon = rna[idx:idx+3]
        amino = conversion(codon)
        prot.append(amino)
    return ''.join(prot)

def main():
    with open(sys.argv[1]) as f:
        data = f.read()

    prot_string = translate(data)
    print(prot_string)

main()
