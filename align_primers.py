import parasail
import sys
from Bio import SeqIO
from Bio import Seq

def parasail_align(seq1, seq2):
	# Semi-Global, do not penalize gaps at beginning and end of both sequences
	trace = parasail.sg_trace_striped_16(seq1, seq2, 10, 5, parasail.dnafull)
	return trace

def main():
	seq1 = list(SeqIO.parse(open(sys.argv[1]), 'fasta'))[0]
	seq2 = Seq.Seq(sys.argv[2])
	if direction == 'fwd':
		traceback = parasail_align(seq1.seq._data, seq2._data).get_traceback()
	if direction == 'rev':
		traceback = parasail_align(seq1.seq._data, seq2.reverse_complement()._data).get_traceback()
	start = len(traceback.comp) - len(traceback.comp.lstrip())
	end = len(traceback.comp.rstrip())
	print(start, end, end-start, direction)
	print(traceback.query[start:end])
	print(traceback.comp[start:end])
	print(traceback.ref[start:end])

if __name__ == "__main__":
	main()
	
