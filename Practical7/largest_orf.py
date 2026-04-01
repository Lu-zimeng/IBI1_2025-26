seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

import re
largest_ORF_UAA=re.findall(r'AUG.+UAA',seq)
len_UAA=len(largest_ORF_UAA[0]) if largest_ORF_UAA else 0
largest_ORF_UAG=re.findall(r'AUG.+UAG',seq)
len_UAG=len(largest_ORF_UAG[0]) if largest_ORF_UAG else 0
largest_ORF_UGA=re.findall(r'AUG.+UGA',seq)
len_UGA=len(largest_ORF_UGA[0]) if largest_ORF_UGA else 0
if len_UAA>len_UGA and len_UAA>len_UAG:
    largest_length=len_UAA
    largest_ORF=largest_ORF_UAA[0]
elif len_UAG>len_UAA and len_UAG>len_UGA:
    largest_length=len_UAG
    largest_ORF=largest_ORF_UAG[0]
else:
    largest_length=len_UGA
    largest_ORF=largest_ORF_UGA[0]
print('The largest ORF that can be generated from this sequence is ' +largest_ORF+ ', the length of that ORF in nucleiotides is '+ str(largest_length))
