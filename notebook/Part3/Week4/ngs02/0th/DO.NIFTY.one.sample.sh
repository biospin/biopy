#!/bin/sh
SRC="/BIO/data/NIFTY2012/fastq"
SAMPLE="SRR358050"
REF="/DB/genomes/H.sapiens/b37/bwa-0.6/human_g1k_v37.fasta"

rm -rf ${SAMPLE}[._]*

ln -s ${SRC}/${SAMPLE}.fastq.gz .

fastqc -t 4 ${SAMPLE}.fastq.gz

sickle se -f ${SAMPLE}.fastq.gz -t illumina -o ${SAMPLE}.trimmed.fastq;

seqret -auto -sequence ${SAMPLE}.trimmed.fastq -snucleotide1 -sformat1 fastq-illumina \
       		-outseq ${SAMPLE}.trimmed.converted.fastq -osformat2 fastq-sanger;

gzip ${SAMPLE}.trimmed.converted.fastq;

fastqc -t 4 ${SAMPLE}.trimmed.converted.fastq.gz

bwa aln -t 4 ${REF} ${SAMPLE}.trimmed.converted.fastq.gz > ${SAMPLE}.sai

bwa samse ${REF} ${SAMPLE}.sai ${SAMPLE}.trimmed.converted.fastq.gz \
	| gzip -c > ${SAMPLE}.sam.gz

samtools view -@ 4 -Sbh ${SAMPLE}.sam.gz \
	| samtools sort -@ 4 - -f ${SAMPLE}.bam; \
	samtools index ${SAMPLE}.bam;

samtools flagstat ${SAMPLE}.bam > ${SAMPLE}.bam.flagstat

samtools idxstats ${SAMPLE}.bam > ${SAMPLE}.bam.idxstats

samtools stats ${SAMPLE}.bam > ${SAMPLE}.bam.stats
