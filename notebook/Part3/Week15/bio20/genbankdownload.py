#!/usr/bin/env python
# A short script to download nucleotide sequences from genbank.
#
# Copyright (c) 2009, Simon J. Greenhill <simon@simon.net.nz>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of genbank-download nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
Download nucleotide sequences from genbank using an accession number

(c) Simon Greenhill, 2009

Usage:

python genbankdownload.py [options] ACCESSION-NUMBER

e.g.
python genbankdownload.py J01415.1
python genbankdownload.py J01415.1 > mysequence.xml
python genbankdownload.py -m fasta J01415.1 > mysequence.fasta

"""
__author__ = 'Simon Greenhill <simon@simon.net.nz>'
__version__ = "0.5"

_toolname = 'genbank-download'
_email = 'dev@simon.net.nz'

import sys
import urllib

_database = "nucleotide"
_rettypes = ('native', 'fasta', 'gb', 'xml')


def get_accession(query, database, rettype):
    """
    Returns a nucleotide sequence from genbank.

    :param query: the accession number
    :param database: the database to use (default=nucleotide)
    :param rettype: the return type for the sequence (native,fasta,gb,xml)

    :return: text of sequence in requested `rettype`
    :rtype: string

    """

    params = {
        'db': database,
        'tool': _toolname,
        'email': _email,
        'id': query,
        'rettype': rettype,
    }
    url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'
    url = url + urllib.urlencode(params)
    data = urllib.urlopen(url).read()
    return data


if __name__ == '__main__':

    from optparse import OptionParser
    parser = OptionParser(usage="usage: %prog [-t xxxx] accessnumber")
    parser.add_option("-t", "--rettype",
        dest="rettype", action="store", default="xml",
        help="Return type of data. Valid values are %s" % ",".join(_rettypes))
    options, args = parser.parse_args()

    try:
        acc = args[0]
    except IndexError:
        parser.print_help()
        sys.exit()

    # validate input
    if options.rettype not in _rettypes:
        print "Error: rettype %s is not a valid rettype" % options.rettype
        quit()

    citation = get_accession(acc, _database, options.rettype)
    print citation
