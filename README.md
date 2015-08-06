####    Lachesis_assembly_formatter_for_TASSEL

The purpose of this script is to take the output of the Lachesis assembled .fasta and reorganize and rename the fasta header so that they are compatible with TASSEL. This can be done by grouping the sequences from the same cluster, and then renaming the sequences in the header so that they are in numerical order (chr1, chr2, chr3...)

More specifically, the Lachesis fasta consists of "group" sequences, followed by "flattened" sequences. Each flattened sequence contains the name of its corresponding group in the header line.

This program reorders the fasta so that the first "group" sequence is followed by its corresponding "flattened" sequences. Then comes the next "group" sequence and its "flattened" sequences.

This order is important, but the output file loses all group information, as the fasta headers are changed to "chr1", "chr2", etc. It's okay, this is what TASSEL wants, and there will never be any need to go back and find out which group a given "chr" sequence came from.
