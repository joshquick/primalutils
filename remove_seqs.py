from Bio import SeqIO
import sys

remove = [id.strip("'") for id in sys.argv[2:]]
print(remove)

for record in SeqIO.parse(open(sys.argv[1]), 'fasta'):
	if record.id not in remove:
		SeqIO.write(record, sys.stdout, 'fasta')
