#!/bin/bash
rm -rf SRR*
export SRC="/BIO/data/NIFTY2012/fastq"
# for SAMPLE in SRR358523 SRR358525 SRR358526 SRR358527 SRR358535; do
for SAMPLE in SRR358050 SRR357358 SRR358220 SRR358179 SRR358027 SRR357854 SRR357878; do
# 30M 60M 90M 120M 150M 240M 480M
# for SAMPLE in `cut -d" " -f1 ${SRC}/fastq.list.sorted | tail -n 5`; do
	echo ${SAMPLE}
	mkdir -p ${SAMPLE}/raw
	cd ${SAMPLE}/raw
	ln -s ${SRC}/${SAMPLE}.fastq.gz .
	cd ../..
done
ln -s SRR358050 30M
ln -s SRR357878 60M
ln -s SRR358220 90M
ln -s SRR358179 120M
ln -s SRR358027 150M
ln -s SRR357854 240M
ln -s SRR357878 480M
