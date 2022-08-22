from Bio import SeqIO, AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import Counter
import sys

# Iterate over the alignment
# For each position output a base to representing the majority into the mask
# If there is a gap in the reference genome mask the -1 position with N
# If there is a gap in the majority of other genomes mask these positions with N


align = AlignIO.read(sys.argv[1], "fasta")
mask = list(align[0].seq.replace('-', ''))

dna_dict = {
		'A': {'A'},
		'C': {'C'},
		'G': {'G'},
		'T': {'T'},
        'R': {'A', 'G'},
        'Y': {'C', 'T'},
        'S': {'G', 'C'},
        'W': {'A', 'T'},
        'K': {'G', 'T'},
        'M': {'A', 'C'},
		}

def count_filter(bases):
	# Remove singletons
	counts_dna = Counter(bases)
	counts_filt = {k:counts_dna[k] for k in counts_dna.keys() if counts_dna[k] > 1}
	return counts_filt
	
def dict_lookup(bases):
	most_common = count_filter(bases)
	amb = [k for k in dna_dict.keys() if dna_dict[k] == set(most_common)]
	if amb:
		return amb
	else:
		return None

# Reset counters
ref_position = 0
i = 0
n = align.get_alignment_length()

while i < n:
	# If the alignment can be described by an base/ambiguity
	if not align[0, i] == '-':
		print(i, align[1, i], align[1:, i])
		amb = dict_lookup(align[1:, i])
		if amb:
			print(f'Masking position with {amb[0]}')
			mask[ref_position] = amb[0]
		else:
			print(f'Masking position with N')
			mask[ref_position] = 'N'
		ref_position += 1
		i += 1
	else:
		j = i
		# Count length of insertion
		while j < n and align[0, j] == '-':
			j += 1

		# Insertion with respect to reference mask -1 position with N
		r_gaps = j - i
		if r_gaps > 0:
			print(f'Masking insertion with N')
			mask[ref_position - 1] = 'N'

		# update counters
		ref_position += (j - i - r_gaps)
		i = j

mask_rec = SeqRecord(Seq("".join(mask)), id=align[0].id, description='')
SeqIO.write(mask_rec, open('test_mask.fa', 'w'), 'fasta')
#print(mask_rec.seq[600:660])
#print(align[0].seq.replace('-', '')[600:660])
#print(len(mask_rec.seq), len(align[0].seq.replace('-', '')))