#!/bin/sh
export Q="bench.q"      # for rocks
export PE="threads"     # for rocks

export Q="all.q"        # for cloud.biopython.net
export PE="make"        # for cloud.biopython.net

export THREADS=1
for SAMPLE in `ls -1d SRR*`; do

	if ! [ -d ${SAMPLE}/fastq ]; then
		echo "mkdir -p ${SAMPLE}/fastq"
		mkdir -p ${SAMPLE}/fastq
	fi

	qsub -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -j y -cwd -V -o ${SAMPLE}/log/\$JOB_ID.$0.oe \
		sickle.seqret_sample.qsub ${SAMPLE}

done
