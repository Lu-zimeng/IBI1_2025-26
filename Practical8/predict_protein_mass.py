def predict_protein_mass(aa_sequence):
    aa_mass_dict = {'G': 57.02,  'A': 71.04,  'S': 87.03,  'P': 97.05,  'V': 99.07,  'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08}
    total_mass=0
    for aa in aa_sequence:
        if aa not in aa_mass_dict:
            raise ValueError("Error:cannot find amino acid")
        total_mass+=aa_mass_dict[aa]
    return total_mass
seq=input('Please input aa sequence:')
mass=predict_protein_mass(seq)
print('The total mass of '+seq+' is '+ str(mass))