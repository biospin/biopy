#!/bin/sh
export Q="bench.q"	# for rocks
export PE="threads"	# for rocks

export Q="all.q"	# for cloud.biopython.net
export PE="make"	# for cloud.biopython.net

export THREADS=4
for SAMPLE in `ls -1d SRR*`; do
	if ! [ -d ${SAMPLE}/fastq ]; then
		echo "mkdir ${SAMPLE}/fastq"
		mkdir ${SAMPLE}/fastq
	fi

	echo "fastqc ${SAMPLE}"
	cd ${SAMPLE}/fastq/
	ln -s ../raw/${SAMPLE}_[12].fastq.gz .
	cd ../..

done
