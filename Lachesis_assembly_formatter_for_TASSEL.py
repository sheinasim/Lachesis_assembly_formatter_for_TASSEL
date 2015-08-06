#!/usr/bin/env python

import sys

def is_a_cluster_sequence(header):
    # TODO inspect header, which is a string that might look like
    # "flattened_line_34584__unclustered" or "Lachesis_group0__552_contigs__length_50808702"
    # and return True or False
    # For now the function just returns True, which is sometimes right ...
    return True

def get_group_number(header):
    # TODO inspect header, which is a string that might look like
    # "flattened_line_34584__unclustered" or "Lachesis_group0__552_contigs__length_50808702"
    # and return either an integer (if it's in a group) or None (if it's ungrouped)
    # For now the function just returns 42, which is sometimes right ...
    return 42

def main():
    # check arguments
    if len(sys.argv) !=2:
        sys.stderr.write("usage: python Lachesis_assembly_formatter_for_TASSEL.py <input.fasta>\n")
        sys.exit()

    # Read all seqs into memory
    all_seqs = []  # a list of (header, sequence) tuples
    current_header = ""
    current_seq = ""
    with open(sys.argv[1], 'r') as infile:
        for line in infile:
            if line.startswith(">"):
                # New sequence
                if current_seq:
                    # Add to list
                    all_seqs.append( (current_header, current_seq) )
                current_header = line[1:].strip() # ignore the ">" character
                current_seq = ""
            else:
                current_seq += line.strip()
        # Add last sequence
        all_seqs.append( (current_header, current_seq) )

    # Sort sequences by type and group
    cluster_seqs = []
    unordered_seqs = {} # a dict that maps group number (an int) to a list of seqs
    ungrouped_seqs = []
    for seq in all_seqs:
        header = seq[0]
        if is_a_cluster_sequence(header):
            cluster_seqs.append(seq)
        else:
            group_number = get_group_number(header)
            if group_number is None:
                ungrouped_seqs.append(seq)
            else:
                if group_number in unordered_seqs:
                    unordered_seqs[group_number].append(seq)
                else:
                    unordered_seqs[group_number] = [seq]

    # Now get ready to write stuff
    index = 1
    with open("out.fasta", 'w') as outfasta, open("out.tsv", 'w') as outtsv:
        # First write cluster seqs, each followed by their unordered group mates
        for seq in cluster_seqs:
            # Get seq info
            header = seq[0]
            sequence = seq[1]
            # Write seq with new header
            new_header = "chr" + str(index)
            outfasta.write(">" + new_header + "\n")
            outfasta.write(sequence + "\n")
            outtsv.write(header + "\t" + new_header + "\n")
            index += 1
            # Now write unordered seqs from this group
            current_group_number = get_group_number(header)
            group_mates = unordered_seqs[current_group_number]
            for mate in group_mates:
                mate_header = mate[0]
                mate_seq = mate[1]
                mate_new_header = "chr" + str(index)
                outfasta.write(">" + mate_new_header + "\n")
                outfasta.write(mate_seq + "\n")
                outtsv.write(mate_header + "\t" + mate_new_header + "\n")
                index += 1

        # With all cluster and unordered seqs written, only need to write ungrouped seqs
        for seq in ungrouped_seqs:
            header = seq[0]
            sequence = seq[1]
            # Write seq with new header
            new_header = "chr" + str(index)
            outfasta.write(">" + new_header + "\n")
            outfasta.write(sequence + "\n")
            outtsv.write(header + "\t" + new_header + "\n")
            index += 1


if __name__ == "__main__":
    main()
