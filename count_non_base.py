import sys
from Bio import SeqIO

dna = ['A', 'C', 'G', 'T']

with open(sys.argv[1], 'r') as fin:
	print(f"id\tamb\tn\tgap\tlen")
	for record in SeqIO.parse(fin, 'fasta'):
		print(record.id, len([base for base in record.seq.upper() if not base in dna]), record.seq.upper().count('N'), record.seq.count('-'), len(record.seq))
