import sys

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

def find_overlaps(seqs):
    track = []
    fin = []

    for idx, seq in enumerate(seqs):
        fin.append(seq)
        for idx2, seq2 in enumerate(seqs):
            if seq2 not in fin and seq != seq2:
                if seq[:3] == seq2[-3:]:
                    track.append((idx2, idx))
                if seq2[:3] == seq[-3:]:
                    track.append((idx, idx2))
    return track

def reformat(idx, names):
    pairs = []
    for pair in idx:
        pairs.append('' + names[pair[0]][1:] + ' ' + names[pair[1]][1:])

    return pairs

def main():
    names = []
    seqs = []

    with open(sys.argv[1]) as f:
        for name, seq in read_fasta(f):
            names.append(name)
            seqs.append(seq)

    overlap = find_overlaps(seqs)
    output = reformat(overlap, names)
    for entry in output:
        print(entry)

main()
