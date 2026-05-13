# define a function read Seq1, Seq2
def read_fasta(filename):
    seq = ""
    with open(filename, "r",encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith(">"): # skip the title line
                seq += line
    return seq
# define a function to read BLOSUM62 matrix
# > store the lines into list
# > store the first line to be aa2
# > the aa in the front of the line will be aa1
# > store the aa and the score in a dictionary and reture the dictionary
def read_blosum(filename):
    blosum = {}
    aa_list = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split()#split the line into list
            if len(aa_list) == 0:#if it's the first line, store all the amino acids, these will be aa2
                aa_list = parts
            else:
                aa1 = parts[0] # if it's not the first line, then the aa in the front of the line will be aa1
                scores = list(map(int, parts[1:])) # store the scores
                for i, aa2 in enumerate(aa_list):
                    blosum[(aa1, aa2)] = scores[i]
    return blosum

# define the function comparing each amino acid
def align_sequences(seq1, seq2, blosum):
    total_score = 0
    identical = 0
    length = len(seq1)
    for a, b in zip(seq1, seq2):
        total_score += blosum[(a, b)] 
        if a == b:
            identical += 1
    identity_percentage = (identical / length) * 100
    return total_score, identity_percentage

# print the output
# > read files
# > use function to get results
# > print results
if __name__ == "__main__":
    human_seq = read_fasta("human.fasta")
    mouse_seq = read_fasta("mouse.fasta")
    random_seq = read_fasta("random.fasta")
    blosum = read_blosum("BLOSUM62.txt")

    hm_score,hm_percentage = align_sequences(human_seq, mouse_seq, blosum)
    hr_score, hr_percentage = align_sequences(human_seq, random_seq, blosum)
    mr_score, mr_percentage = align_sequences(mouse_seq, random_seq, blosum)

    print("=== human DLX5 vs mouse DLX5 ===")
    print("The alignment score: "+ str(hm_score))
    print("The percentage of identical amino acids: "+str(hm_percentage)+"%")

    print("=== human DLX5 vs random ===")
    print("The alignment score: "+ str(hr_score))
    print("The percentage of identical amino acids: "+str(hr_percentage)+"%")

    print("=== mouse DLX5 vs random ===")
    print("The alignment score: "+ str(mr_score))
    print("The percentage of identical amino acids: "+str(mr_percentage)+"%")