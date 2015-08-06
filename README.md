####    Lachesis_assembly_formatter_for_TASSEL

The purpose of this script is to take the output of the Lachesis assembled .fasta and reorganize and rename the fasta header so that they are compatible with TASSEL. 

The Lachesis fasta consists of "cluster" sequences, followed by "unordered" sequences, followed by "ungrouped" sequences. Each unordered sequence contains the name of its corresponding cluster group in the header line.

This program reorders the fasta so that the first "cluster" sequence is followed by its corresponding "unordered" sequences. Then comes the next "cluster" sequence and its "unordered" sequences. The "ungrouped" sequences come last.

This order is important, but the output file loses all group information, as the fasta headers are changed to "chr1", "chr2", etc. So the script also writes a .tsv file mapping the old sequence headers to the new ones.
