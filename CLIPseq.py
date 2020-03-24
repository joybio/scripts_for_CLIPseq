#!/bin/python
#coding:utf-8
import os

index1='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACG'
index2='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACCGATGT'
index3='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACTTAGGC'
index4='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACTGACCA'
index5='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACACAGTG'
index6='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACGCCAAT'
index7='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACCAGATC'
index8='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACACTTGA'
index9='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACGATCAG'
index10='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACTAGCTT'
index11='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACGGCTAC'
index12='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACCTTGTA'
index13='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACAGTCAACA'
index14='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACAGTTCCGT'
index15='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACATGTCAGA'
index16='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACCCGTCC'
index18='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACGTCCGCAC'
index19='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACGTGAAACG'
index20='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACGTGGCCTT'
index21='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACGTTTCGGA'
index22='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACCGTACGTA'
index23='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACGAGTGGAT'
index25='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACACTGATAT'
index27='AGATCGGAAGAGCACACGTCTGAACTCCAGTCACATTCCTTT'
primer5='AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGAT'
SR_primer='GATCGTCGGACTGTAGAACTCTGAACGTGTAGAT'

#os.system('ls *.R1.fastq.gz | while read id; do(echo "$id" >> dict.csv); done')

sample_dict = {}
with open("dict.csv","r") as f:
	for i in f:	
		j = i.strip().split("\t")
		key = j[0] + "_combined"
		sample_dict[key] = eval("index" + j[1])
print(sample_dict)

for i in sample_dict.keys():
	index = sample_dict[i]
	print(index)
	print(index1)
	print(i)
	os.system("cutadapt -a {} -A GATCGTCGGACTGTAGAACTCTGAACGTGTAGAT -j 10 -e 0.1 -O 5 -m 13 -o {}.trimmed.R1.fq.gz -p {}.trimmed.R2.fq.gz {}.R1.fastq.gz {}.R2.fastq.gz".format(index,i,i,i,i))
f.close()

os.system("ls *.trimmed.R1.fq.gz | while read id; do(hisat2 --pen-noncansplice 1000000  -x /home/l/backup1/refgenome/Arabidopsis/hisat2/Arabidopsis_tran -1 $id -2 $(basename $id '.R1.fq.gz').R2.fq.gz -S $(basename $id '.trimmed.R1.fq.gz').sam); done")

os.system("ls *.sam | while read id; do(samtools sort -O BAM -o $(basename $id '.sam').sorted.bam $id); done")

os.system("ls *.sorted.bam | while read id; do(samtools flagstat $id > $(basename $id '.sorted.bam').txt); done")
