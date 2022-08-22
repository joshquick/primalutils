from Bio import SeqIO
import sys
import uuid

remove_primary = False

with sys.stdout as fout:
	with open(sys.argv[1], 'r') as fin:
		for i, record in enumerate(SeqIO.parse(fin, 'fasta')):
			if remove_primary and i == 0:
				continue
			uid = str(uuid.uuid4())
			print(f"{record.id}\t{uid}", file=sys.stderr)
			record.id = uid
			record.description = uid
			record.seq = record.seq.replace('-', '').upper()
			SeqIO.write(record, fout, 'fasta') 
