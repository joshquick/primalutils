input=$1
fasta=$2

mkdir output
cp $fasta output/$fasta
samtools faidx output/$fasta
python split_multifa.py $input > output/refs.txt
while read p; do
	python ncov-random-scripts/quick_align.py -r output/$fasta -g output/$p -o vcf > output/$p.vcf	
	bgzip output/$p.vcf
	tabix -p vcf output/$p.vcf.gz
	# filter only needed when reference is shorter than the genome
	bcftools filter -e "POS==0" output/$p.vcf.gz -O z > output/$p.filt.vcf.gz
	tabix -p vcf output/$p.filt.vcf.gz
done < output/refs.txt
bcftools merge -0 output/*.fasta.filt.vcf.gz --force-samples > output/merged.vcf
bcftools +fill-tags output/merged.vcf -- -t AF,NS > output/merged.tags.vcf
bcftools filter -i "INFO/AF[0] > 0" output/merged.tags.vcf > output/merged.tags.filt.vcf
python split_vcf.py output/merged.tags.filt.vcf output/merged.tags.filt.amb.vcf output/merged.tags.filt.unamb.vcf
bgzip output/merged.tags.filt.amb.vcf
tabix -p vcf output/merged.tags.filt.amb.vcf.gz
bcftools consensus -I -f $fasta output/merged.tags.filt.amb.vcf.gz > output/preconsensus.fasta 
bedtools maskfasta -fi output/preconsensus.fasta -bed output/merged.tags.filt.unamb.vcf -fo output/merged_mask_amb.fa

