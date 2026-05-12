import re
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
outfile = open('stop_genes.fa', 'w')
#let the sequences for each gene run onto several lines
def wrap_sequence(seq, line_length=60):
    return '\n'.join([seq[i:i+line_length] for i in range(0, len(seq), line_length)])
#use two variable to store the name and the sequence of current gene
current_gene = ""
current_seq = ""

#read line by line
for line in file:
    line = line.rstrip() #remove the space in the end of a line

# (if the line starts from > ,then the code has already finished reading one gene, so it should finish processing before reading the next gene)
# > Distinguish the header line
# > find all the stop codons, step is 3
# > add codons to the header
# > write header and sequence into the outfile
# > change the current_gene to the new gene name
# > remove all from the current_seq for next sequence to be stored
# if the line doesn't start from >, meaning it's a line of sequence, so just continue to store the codons into the current_seq

    if line.startswith('>'): 
        if current_gene != "":
            stop_codons=set() # create a set to store stop codons
            for i in range(len(current_seq) - 2):
                if current_seq[i:i+3] == "ATG": #find the start codon ATG
                    for j in range(i, len(current_seq) - 2, 3): # from the start codon and step is 3 codons (cannot go beyond the length of the whole sequence so -2)
                        codon = current_seq[j:j+3]
                        if codon in ["TAA", "TAG", "TGA"]: # if meet stop codon, add to the set and break
                            stop_codons.add(codon)
                            break
            if stop_codons:
                stops1 = set(stop_codons) # exclude the repeated condons
                stop_str = ",".join(stops1) # convert codons into strings
                header = current_gene + ';' + stop_str # add stop codons to the header
                outfile.write(header + '\n')
                wrapped_seq = wrap_sequence(current_seq) 
                outfile.write(wrapped_seq + '\n') # write new header and sequence into the outfile
                
        current_gene = line[0:].split(' ')[0]
        current_seq = "" #remove all from the current_seq
    else:
        current_seq = current_seq + line

# the last line does not start from >, so the last gene hasn't been checked
# bring out the function again for the last gene
if current_gene != "":
    stop_codons = set()
    for i in range(len(current_seq) - 2):
        if current_seq[i:i+3] == "ATG":
            for j in range(i, len(current_seq) - 2, 3):
                codon = current_seq[j:j+3]
                if codon in ["TAA", "TAG", "TGA"]:
                    stop_codons.add(codon)
                    break
    if stop_codons:
        stop_str = ",".join(stop_codons)
        header = current_gene + ';' + stop_str
        outfile.write(header + '\n')
        wrapped_seq = wrap_sequence(current_seq)
        outfile.write(wrapped_seq + '\n')
        
file.close()
outfile.close()