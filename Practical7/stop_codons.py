import re
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
outfile = open('stop_genes.fa', 'w')

current_gene = ""
current_seq = ""

for line in file:
    line = line.rstrip()

#Distinguish the header line
    if line.startswith('>'):
        if current_gene != "":
            stops = re.findall(r'TAA|TAG|TGA', current_seq)#find the stop condons
            if len(stops) > 0:
                stops1 = set(stops)#exclude the repeated condons
                stop_str = ",".join(stops1)
                header = current_gene + ';' + stop_str
                outfile.write(header + '\n')
                outfile.write(current_seq + '\n')
        current_gene = line[0:].split(' ')[0]
        current_seq = ""
    else:
        current_seq = current_seq + line

if current_gene != "":
    stops = re.findall(r'TAA|TAG|TGA', current_seq)
    if len(stops) > 0:
        stops1 = set(stops)
        stop_str = ",".join(stops1)
        header = current_gene + ';' + stop_str
        outfile.write(header + '\n')
        outfile.write(current_seq + '\n')

file.close()
outfile.close()


    