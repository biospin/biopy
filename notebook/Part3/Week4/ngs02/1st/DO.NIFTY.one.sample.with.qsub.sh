#!/bin/sh
SRC="/BIO/data/NIFTY2012/fastq"
SAMPLE="SRR358050"
REF="/DB/genomes/H.sapiens/b37/bwa-0.6/human_g1k_v37.fasta"

Q="all.q"
PE="make"

echo << END
rm -rf ${SAMPLE}[._]*
ln -s ${SRC}/${SAMPLE}.fastq.gz .

exit

THREADS=1
qsub -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -j y -cwd -V -o "${SAMPLE}.\$JOB_ID.fastqc.oe" \
	fastqc_fastq.outdir.threads.qsub ${SAMPLE}.fastq.gz . ${THREADS}

exit
END

THREADS=1
qsub -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -j y -cwd -V -o "${SAMPLE}.\$JOB_ID.sickle.oe" -b y \
	sickle se -f ${SAMPLE}.fastq.gz -t illumina -o ${SAMPLE}.trimmed.fastq;

exit

THREADS=1
qsub -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -j y -cwd -V -o "${SAMPLE}.\$JOB_ID.seqret.oe" -b y \
	seqret -auto -sequence ${SAMPLE}.trimmed.fastq -snucleotide1 -sformat1 fastq-illumina \
       		-outseq ${SAMPLE}.trimmed.converted.fastq -osformat2 fastq-sanger;

exit

gzip ${SAMPLE}.trimmed.converted.fastq;

exit

THREADS=2
qsub -V -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -j y -cwd -o ${SAMPLE}.\$JOB_ID.trimmed.converted.fastqc.oe -b y \
	fastqc ${SAMPLE}.trimmed.converted.fastq.gz -o . -t 2

exit

echo "bwa aln ${SAMPLE}"

THREADS=4
qsub -V -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -cwd -V -j y -o ${SAMPLE}.\$JOB_ID.bwa.aln.oe -b y \
	"bwa aln -t 4 ${REF} ${SAMPLE}.trimmed.converted.fastq.gz > ${SAMPLE}.sai"

exit

THREADS=4
qsub -V -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -cwd -V -j y -o ${SAMPLE}.\$JOB_ID.bwa.samse.oe -b y \
	"bwa samse ${REF} ${SAMPLE}.sai ${SAMPLE}.trimmed.converted.fastq.gz \
	| gzip -c > ${SAMPLE}.sam.gz"

exit

THREADS=4
qsub -V -q ${Q} -N ${SAMPLE} -pe ${PE} ${THREADS} -cwd -V -j y -o ${SAMPLE}.\$JOB_ID.samtools.sort.oe -b y \
	"samtools view -@ ${THREADS} -Sbh ${SAMPLE}.sam.gz \
	| samtools sort -@ ${THREADS} - -f ${SAMPLE}.bam; \
	samtools index ${SAMPLE}.bam;"
exit

samtools flagstat ${SAMPLE}.bam > ${SAMPLE}.bam.flagstat

samtools idxstats ${SAMPLE}.bam > ${SAMPLE}.bam.idxstats

samtools stats ${SAMPLE}.bam > ${SAMPLE}.bam.stats
