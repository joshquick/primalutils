from Bio import SeqIO
import sys

remove = [id.strip("'") for id in sys.argv[2:]]

with sys.stdout as fout:
	with open(sys.argv[1], 'r') as fin:
		for record in SeqIO.parse(fin, 'fasta'):
			if record.id in remove:
				SeqIO.write(record, fout, 'fasta') 
