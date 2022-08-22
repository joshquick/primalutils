from Bio import AlignIO
import sys

match = 0
mismatch = 0
gap = 0

align = AlignIO.read(sys.argv[1], "fasta")
align_len = len(align[0])
for col in range(align_len):
	bases = set(align[:, col])
	#print(col, bases)
	if len(bases) == 1:
		if '-' in bases:
			gap += 1
		else:
			match += 1
	else:
		mismatch += 1

print(f"len\tgap\tmatch\tmismatch")
print(f"{align_len}\t{gap}\t{match}\t{mismatch}")

