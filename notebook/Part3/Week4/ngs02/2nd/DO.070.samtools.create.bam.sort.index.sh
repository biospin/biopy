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
	qsub -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -cwd -V -j y -o ${SAMPLE}/log/\$JOB_ID.$0.oe -b y \
		"samtools view -@ ${THREADS} -Sbh ${SAMPLE}/mapped/bwa/${SAMPLE}.sam.gz \
		| samtools sort -@ ${THREADS} - -f ${SAMPLE}/mapped/bwa/${SAMPLE}.bam; \
		samtools index ${SAMPLE}/mapped/bwa/${SAMPLE}.bam;"
done
