import sys
from Bio import Entrez
from Bio import SeqIO

def process(ids):
    Entrez.email = "noahflynn@wustl.edu"
    handle = Entrez.efetch(db='nucleotide', id=ids, rettype='fasta')
    records = list (SeqIO.parse(handle, 'fasta')) #gets the list of SeqIO objects in FASTA format

    shortest_id = 0
    for idx, rec in enumerate(records):
        if len(rec.seq) < len(records[shortest_id].seq):
            shortest_id = idx

    return '>' + records[shortest_id].description + '\n' + records[shortest_id].seq

def main():
    with open(sys.argv[1]) as f:
        data = f.read().split()

    result = process(data)
    print(result)

main()
