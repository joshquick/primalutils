import sys
from Bio import SeqIO

with open(sys.argv[1], 'r') as fin:
	for record in SeqIO.parse(fin, 'fasta'):
		print(record.id, record.seq.count('N'), record.seq.count('-'), len(record.seq))
