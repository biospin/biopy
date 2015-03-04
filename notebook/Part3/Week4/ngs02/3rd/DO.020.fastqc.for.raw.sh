#!/bin/sh
export Q="bench.q"	# for rocks
export PE="threads"	# for rocks

export Q="all.q"	# for cloud.biopython.net
export PE="make"	# for cloud.biopython.net

export THREADS=4
for SAMPLE in `ls -1d SRR*`; do
	if ! [ -d ${SAMPLE}/log ]; then
		echo "mkdir ${SAMPLE}/log"
		mkdir ${SAMPLE}/log
	fi

	echo "fastqc ${SAMPLE}"
	qsub -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -j y -cwd -V -o "${SAMPLE}/log/\$JOB_ID.$0.oe" \
		fastqc_fastq.outdir.threads.qsub ${SAMPLE}/raw/${SAMPLE}_1.fastq.gz ${SAMPLE}/raw ${THREADS}

	qsub -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -j y -cwd -V -o "${SAMPLE}/log/\$JOB_ID.$0.oe" \
		fastqc_fastq.outdir.threads.qsub ${SAMPLE}/raw/${SAMPLE}_2.fastq.gz ${SAMPLE}/raw ${THREADS}

done
