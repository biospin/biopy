#!/bin/bash
rm -rf SRR*
export SRC="/BIO/data/SRA.1000genome.WXS.PE"
for SAMPLE in SRR748291 SRR748788 SRR748790 SRR748792; do
# for SAMPLE in `cat ${SRC}/SRA/SRP.list`; do
	echo ${SAMPLE}
	mkdir -p ${SAMPLE}/raw
	cd ${SAMPLE}/raw
	ln -s ${SRC}/fastq/${SAMPLE}_*.fastq.gz .
	cd ../..
	SHORT=${SAMPLE/SRR748/}
	rm ${SHORT}
	ln -s ${SAMPLE} ${SHORT}
done
