#!/bin/sh
export Q="bench.q"      # for rocks
export PE="threads"     # for rocks

export Q="all.q"        # for cloud.biopython.net
export PE="make"        # for cloud.biopython.net

export THREADS=2
for SAMPLE in `ls -1d SRR*`; do
	qsub -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -j y -cwd -o ${SAMPLE}/log/\$JOB_ID.$0.oe -b y \
		fastqc ${SAMPLE}/fastq/${SAMPLE}.fastq.gz -o ${SAMPLE}/fastq -t ${THREADS}
done
