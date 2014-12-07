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
        echo "<${SAMPLE}>"
        echo "$ ls -lLh ${SAMPLE}/mapped/bwa/${SAMPLE}.bam*"
        ls -lLh ${SAMPLE}/mapped/bwa/${SAMPLE}.bam*
        echo
        echo "$ samtools flagstat ${SAMPLE}/mapped/bwa/${SAMPLE}.bam"
        samtools stats ${SAMPLE}/mapped/bwa/${SAMPLE}.bam
        echo
done
