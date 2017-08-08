import sys
from Bio import SeqIO

def eval_quality(fq, threshold):
    count = 0
    for f in fq:
        qa = f.letter_annotations["phred_quality"]
        avg_qa = sum(qa)/len(qa)
        if avg_qa < threshold: count += 1
    return count

def main():
    with open(sys.argv[1]) as f:
        threshold = int(f.readline())
        records = list(SeqIO.parse(f, 'fastq'))

    num_below_threshold = eval_quality(records, threshold)
    print(num_below_threshold)

main()
