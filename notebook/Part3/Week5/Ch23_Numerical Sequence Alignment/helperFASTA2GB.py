#!/usr/bin/python
# -*- coding:UTF-8 -*-

from __future__ import print_function
from __future__ import division
import argparse, sys, os

__author__ = "Sungjin Park"
__version__ = "0.0.1"
__email__ = "oscar.park@gmail.com"


def insert_whitespaces(string, win_size):
    hash_list = list(string)
    hash_chunk_size = len(string) // win_size
    for x in range(1, hash_chunk_size + 1):
        hash_list.insert(x * 10 + x - 1, " ")
    return ''.join(hash_list)


def transform(path):
    # get tail(filename)
    _, tail = os.path.split(path)

    # set target file name from tail except extension name
    target_filename = os.path.splitext(tail)[0] + "_fasta2gbk.txt"

    #print(target_filename)

    line_num = 1
    seq = ''
    win_size = 60

    # GBK format
    # lineNum    SEQ_10 * 6 w/ whitespace_delimiter

    with open(path, "r") as fh:
        lst_fasta = fh.readlines()
        seq = "".join(map(lambda x: x.replace("\n", ""), lst_fasta)[1:])

    #print (seq)

    with open(target_filename, "w") as fh:
        seq_size = len(seq)
        #print (seq_size)
        # imported __future__.division to set compatibility between py2 and py3
        # so be careful about division symbol
        chunk_size = seq_size // win_size
        for i in range(chunk_size):
            hash = insert_whitespaces(
                    seq[i * win_size: i * win_size + win_size - 1],
                    10
                )
            
            #print (hash)

            fh.write("{linenum: >{width}} {seq}{newline}".format(
                linenum=line_num,
                width=len(str(chunk_size * win_size)),
                seq=hash,
                newline="\n"))
            line_num += win_size

        hash = insert_whitespaces(seq[chunk_size * win_size:], 10)
        
        #print (hash)

        fh.write("{0} {1}".format(line_num, hash))
            
    print("DONE")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", action="store", dest="inputfile", help="input fasta file to transform GBK format. ex: -i NC_000918.fasta")
    parser.add_argument("-V", "--version", action="version",
                        version="helperFASTA2GB.py version " + __version__)

    results = parser.parse_args()

    if results.inputfile is None:
        print("Missing input file.")
        sys.exit(-1)
    else:
        transform(results.inputfile)


if __name__ == "__main__":
    main()
