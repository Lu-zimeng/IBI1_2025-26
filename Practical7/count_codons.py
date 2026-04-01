import re
import matplotlib.pyplot as plt
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
codon_counts = {}

stop_codon = input("Please input one of the three codons(TAA/TAG/TGA):")

current_gene = ""
current_seq = ""
for line in input_file:
    line = line.rstrip()

    if line.startswith('>'):
        if current_gene != "":
            stop_positions = [m.start() for m in re.finditer(stop_codon, current_seq)]
            atg_match = re.search(r'ATG', current_seq)
            if atg_match and len(stop_positions) > 0:
                atg_pos = atg_match.start()
                valid_stops = [pos for pos in stop_positions if pos > atg_pos]
                if len(valid_stops) > 0:
                    longest_stop_pos = max(valid_stops)
                    orf_seq = current_seq[atg_pos : longest_stop_pos]
                    for i in range(0, len(orf_seq), 3):
                        if i + 3 <= len(orf_seq):
                            codon = orf_seq[i:i+3]
                            if codon in codon_counts:
                                codon_counts[codon] = codon_counts[codon] + 1
                            else:
                                codon_counts[codon] = 1

            current_gene = line[1:].split(' ')[0]
            current_seq = ""
        else:
            current_gene = line[1:].split(' ')[0]
            current_seq = ""
    else:
        current_seq = current_seq + line

if current_gene != "":
    stop_positions = [m.start() for m in re.finditer(stop_codon, current_seq)]
    atg_match = re.search(r'ATG', current_seq)
    if atg_match and len(stop_positions) > 0:
        atg_pos = atg_match.start()
        valid_stops = [pos for pos in stop_positions if pos > atg_pos]
        if len(valid_stops) > 0:
            longest_stop_pos = max(valid_stops)
            orf_seq = current_seq[atg_pos : longest_stop_pos]
            for i in range(0, len(orf_seq), 3):
                if i + 3 <= len(orf_seq):
                    codon = orf_seq[i:i+3]
                    if codon in codon_counts:
                        codon_counts[codon] = codon_counts[codon] + 1
                    else:
                        codon_counts[codon] = 1

input_file.close()


codons = list(codon_counts.keys())
counts = list(codon_counts.values())

plt.figure(figsize=(12, 12))
title = "Codon Frequency for Stop Codon: " + stop_codon + "\nTotal Codons Counted: " + str(sum(counts))
plt.title(title, fontsize=16)

wedges, texts, autotexts = plt.pie(
    counts, 
    labels=codons, 
    autopct='%1.1f%%', 
    startangle=90
)
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_color('white')

plt.savefig('codon_frequency_' + stop_codon + '.png', bbox_inches='tight')
plt.show()


for codon, count in sorted(codon_counts.items(), key=lambda x: x[1], reverse=True):
    print(codon + ": " + str(count) + " times")