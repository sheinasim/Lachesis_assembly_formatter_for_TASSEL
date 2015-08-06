#!/usr/bin/env python

import sys

# check arguments
if len(sys.argv) !=1:
    sys.stderr.write("usage: python Lachesis_assembly_formatter_for_TASSEL.py <input.fasta>\n")
    sys.exit()

# open file
with open(sys.argv[1]) as inputfile:

