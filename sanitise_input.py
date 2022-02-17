from Bio import SeqIO
import sys
import uuid

with sys.stdout as fout:
	with open(sys.argv[1], 'r') as fin:
		for record in SeqIO.parse(fin, 'fasta'):
			record.id = str(uuid.uuid4())
			record.description = record.id
			record.seq = record.seq.replace('-', '')
			if record.seq.count('N') / len(record.seq) < 0.0025: 
				SeqIO.write(record, fout, 'fasta') 
