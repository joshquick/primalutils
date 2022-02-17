from Bio import SeqIO
import sys

for record in SeqIO.parse(open(sys.argv[1], 'r'), 'fasta'):
	fname = f"{record.id}.fasta"
	print(fname)
	with open('output/' + fname, 'w') as fh:
		SeqIO.write(record, fh, 'fasta')
