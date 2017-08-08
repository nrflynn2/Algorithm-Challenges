import sys
from Bio import Entrez

def entry_count(org, start, end):
    Entrez.email = "noahflynn@wustl.edu"

    term = '%s[Organism] AND (%s[Publication Date] : %s[Publication Date])' % (org, start, end)

    handle = Entrez.esearch(db="nucleotide", term=term)
    record = Entrez.read(handle)
    return record["Count"]

def main():
    with open(sys.argv[1]) as f:
        data = f.read()
    data = data.split()
    count = entry_count(data[0], data[1], data[2])
    print(count)

main()
