#!/usr/bin/env python3
import vcf
import sys

#Convert alt allele(s) to ambiguity code

IUPAC = {
	'R': {'A', 'G'},
        'Y': {'C', 'T'},
        'S': {'G', 'C'},
        'W': {'A', 'T'},
        'K': {'G', 'T'},
        'M': {'A', 'C'},
	}

vcf_in = vcf.Reader(open(sys.argv[1], 'r'))
vcf_amb = vcf.Writer(open(sys.argv[2], 'w'), template=vcf_in)
vcf_unamb = vcf.Writer(open(sys.argv[3], 'w'), template=vcf_in)

for record in vcf_in:
	if len(record.REF) == 1 and len(record.ALT[0]) == 1:
		amb = [k for k in IUPAC.keys() if IUPAC[k] == set(list(record.REF) + list(map(str, record.ALT)))]
		if amb:
			vcf_amb.write_record(vcf.model._Record(CHROM=record.CHROM, POS=record.POS, ID=record.ID, REF=record.REF, ALT=record.ALT, QUAL=None, FILTER=None, INFO={'IUPAC': amb[0]}, FORMAT=record.FORMAT, sample_indexes=[], samples=record.samples))
		else:
			vcf_unamb.write_record(vcf.model._Record(CHROM=record.CHROM, POS=record.POS, ID=record.ID, REF=record.REF, ALT=record.ALT, QUAL=None, FILTER=None, INFO=None, FORMAT=record.FORMAT, sample_indexes=[], samples=record.samples))
	else:		
		vcf_unamb.write_record(vcf.model._Record(CHROM=record.CHROM, POS=record.POS, ID=record.ID, REF=record.REF, ALT=record.ALT, QUAL=None, FILTER=None, INFO=None, FORMAT=record.FORMAT, sample_indexes=[], samples=record.samples))
