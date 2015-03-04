#!/bin/sh
# for rocks
export Q="bench.q"
export PE="threads"
export REF="/dlabs/home/krho/DB/genomes/H.sapiens/b37/bwa-0.6/human_g1k_v37.fasta"

# for cloud.biopython.net
export Q="all.q"
export PE="make"
export REF="/DB/genomes/H.sapiens/b37/bwa-0.6/human_g1k_v37.fasta"

export THREADS=4
for SAMPLE in `ls -1d SRR*`; do
	if ! [ -d ${SAMPLE}/mapped/bwa/ ]; then
		mkdir -p ${SAMPLE}/mapped/bwa/
	fi
	echo "bwa mem ${SAMPLE}"
	
	qsub -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -cwd -V -j y -o ${SAMPLE}/log/\$JOB_ID.$0.oe -b y \
		"bwa mem -t ${THREADS} ${REF} \
		${SAMPLE}/fastq/${SAMPLE}_1.fastq.gz \
		${SAMPLE}/fastq/${SAMPLE}_2.fastq.gz \
		| gzip -c > ${SAMPLE}/mapped/bwa/${SAMPLE}.sam.gz"
done
