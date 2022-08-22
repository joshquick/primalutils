from Bio import SeqIO
import sys

with sys.stdout as fout:
	with open(sys.argv[1], 'r') as fin:
		for record in SeqIO.parse(fin, 'clustal'):
			SeqIO.write(record, fout, 'fasta')
