#!/bin/sh
for SAMPLE in `ls -1d SRR*`; do
	echo "<${SAMPLE}>"
	echo "$ ls -lLh ${SAMPLE}/raw/${SAMPLE}.fastq.gz"
	ls -lLh ${SAMPLE}/raw/${SAMPLE}.fastq.gz
	echo
	echo "$ zcat ${SAMPLE}/raw/${SAMPLE}.fastq.gz | head -n 32"
	zcat ${SAMPLE}/raw/${SAMPLE}.fastq.gz | head -n 32
	echo "..."
	echo
done
