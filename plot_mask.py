import numpy
import argparse
import sys
import csv
from Bio import SeqIO

def count(args):
	win_out = []
	counts = []
	window = args.win
	mask = list(SeqIO.parse(open(args.mask, 'r'), 'fasta'))[0]
	len_record = len(mask)
	variant_positions = numpy.zeros(len_record+1, dtype=bool)
	for i, base in enumerate(mask.seq):
		if base not in ['A', 'C', 'G', 'T']:
			variant_positions[i] = True
	for n in range(0, len_record, window):
		count = (n, numpy.count_nonzero(variant_positions[n:n+window]))
		counts.append(count)
		
	with open("variant_density.csv", "w") as fh_out:
		fh_out.write(f"position, density\n")
		for line in counts:
			fh_out.write(f"{line[0]}, {line[1]}\n")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Count variant density')
	parser.add_argument('mask', help='Mask file')
	parser.add_argument('--win', dest='win', default='1000', type=int, help='Window size')
	if len(sys.argv)==1:
		parser.print_help()
		sys.exit()
	args = parser.parse_args()
	count(args)
