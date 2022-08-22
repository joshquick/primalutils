import sys

vcfs = sys.argv[1:]
headers = []
records = []

for vcf in vcfs:
	with open(vcf, 'r') as fh:
		for line in fh.readlines():
			line = line.strip()
			if line.startswith('#'):
				if line not in headers:
					headers.append(line)
				else:
					continue
				continue
			else:
				records.append(line)

headers.insert(-1, "##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">")
print(headers)
for line in headers:
	print(line)
for line in records:
	print(line)
