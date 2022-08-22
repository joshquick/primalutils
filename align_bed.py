import parasail
import sys
from Bio import SeqIO
from Bio import Seq

def parasail_align(seq1, seq2):
	# Semi-Global, do not penalize gaps at beginning and end of both sequences
	trace = parasail.sg_trace_striped_16(seq1, seq2, 10, 5, parasail.dnafull)
	return trace

def main():
	ref = list(SeqIO.parse(open(sys.argv[1]), 'fasta'))[0]
	bed = [line.strip().split() for line in open(sys.argv[2])]
	for line in bed:
		if line[5] == '+':
			traceback = parasail_align(ref.seq._data, line[6]).get_traceback()
		if line[5] == '-':
			seq2 = Seq.Seq(line[6])
			traceback = parasail_align(ref.seq._data, seq2.reverse_complement()._data).get_traceback()
		start = len(traceback.comp) - len(traceback.comp.lstrip())
		end = len(traceback.comp.rstrip())
		if line[5] == '+':
			primer_seq = line[6]
		if line[5] == '-':
			primer_seq = Seq.Seq(traceback.query[start:end]).reverse_complement()
		print(f"{ref.id}\t{start}\t{end}\t{line[3]}\t{line[4]}\t{line[5]}\t{primer_seq}")	

if __name__ == "__main__":
	main()
	
