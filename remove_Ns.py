from Bio import SeqIO
import sys

with sys.stdout as fout:
	with open(sys.argv[1], 'r') as fin:
		for record in SeqIO.parse(fin, 'fasta'):
			if record.id.startswith('B'):
				record.seq = record.seq.replace('-', '')
				SeqIO.write(record, fout, 'fasta') 
