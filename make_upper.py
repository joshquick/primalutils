from Bio import SeqIO
import sys

with sys.stdout as fout:
	with open(sys.argv[1], 'r') as fin:
		for record in SeqIO.parse(fin, 'fasta'):
			record.seq = record.seq.upper()
			SeqIO.write(record, fout, 'fasta') 
