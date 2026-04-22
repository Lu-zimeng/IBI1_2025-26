seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

import re
#find the largest ORF starting from AUG and three codons per step and stop when meet end codons
all_orf = re.findall(r'AUG(?:...)*?(?:UAA|UAG|UGA)', seq)

#find the longest ORF
longest_orf = max(all_orf, key=len)
longest_len = len(longest_orf)

print('The largest ORF that can be generated from this sequence is ' +longest_orf+ ' and the length of that ORF in nucleiotides is '+ str(longest_len))
