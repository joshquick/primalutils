import sys
from Bio import SeqIO

with open(sys.argv[1], 'r') as fin:
        print(f"id\tlen\tacgt\tn\tamb")
        for record in SeqIO.parse(fin, 'fasta'):
                print(record.id, len(record.seq), len([base for base in record.seq.upper() if base in ['A', 'C', 'G', 'T']]), record.seq.count('N'), len([base for base in record.seq.upper() if base in ['R', 'Y', 'S', 'W', 'K', 'M']]))
