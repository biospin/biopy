#!/bin/sh
for SAMPLE in `ls -1d SRR*`; do
	echo "<${SAMPLE}>"
	echo "$ ls -lLh ${SAMPLE}/raw/${SAMPLE}_*.fastq.gz"
	ls -lLh ${SAMPLE}/raw/${SAMPLE}_*.fastq.gz
	echo
	echo "$ zcat ${SAMPLE}/raw/${SAMPLE}_1.fastq.gz | head -n 16"
	zcat ${SAMPLE}/raw/${SAMPLE}_1.fastq.gz | head -n 16
	echo "..."
	echo
	echo "$ zcat ${SAMPLE}/raw/${SAMPLE}_2.fastq.gz | head -n 16"
	zcat ${SAMPLE}/raw/${SAMPLE}_2.fastq.gz | head -n 16
	echo "..."
	echo
done
