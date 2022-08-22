from Bio import SeqIO, AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import Counter
import sys

# Iterate over the alignment
# Ignore the co-ordinate system and generate BED by alignment

align = AlignIO.read(sys.argv[1], "clustal")
mask = ''

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
	print(most_common)
	amb = [k for k in dna_dict.keys() if dna_dict[k] == set(most_common)]
	if amb:
		return amb
	else:
		return None

# Reset counters
i = 0
n = align.get_alignment_length()

while i < n:
	# If the alignment can be described by an base/ambiguity
	print(i, align[:, i].upper())
	amb = dict_lookup(align[:, i].upper())
	print(amb)
	if amb:
		print(f'Masking position with {amb[0]}')
		mask += amb[0]
	else:
		print(f'Masking position with N')
		mask += 'N'
	i += 1

mask_rec = SeqRecord(Seq("".join(mask)), id=align[0].id, description='')
SeqIO.write(mask_rec, open('test_mask.fa', 'w'), 'fasta')