from Bio import SeqIO
import sys

seq1 = list(SeqIO.parse(open(sys.argv[1], 'r'), 'fasta'))[0]
seq2 = list(SeqIO.parse(open(sys.argv[2], 'r'), 'fasta'))[0]

print(seq1.seq == seq2.seq)
