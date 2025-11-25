##VARIABLES
# input RNA sequence as a string
#s = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
s = str(input('insert RNA sequence:'))
# 64 possible codon combinations from nucleotide bases (A, T, G, U)
combinations = {
    'UUU' : 'F',    'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V',
    'UUC' : 'F',    'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V',
    'UUA' : 'L',    'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V',
    'UUG' : 'L',    'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V',
    'UCU' : 'S',    'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A',
    'UCC' : 'S',    'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',
    'UCA' : 'S',    'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A',
    'UCG' : 'S',    'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',
    'UAU' : 'Y',    'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D',
    'UAC' : 'Y',    'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',
    'UAA' : 'Stop', 'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E',
    'UAG' : 'Stop', 'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E',
    'UGU' : 'C',    'CGU' : 'R', 'AGU' : 'S', 'GGU' : 'G',
    'UGC' : 'C',    'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G',
    'UGA' : 'Stop', 'CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G',
    'UGG' : 'W',    'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G'
} # see: https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables
# accumulator string variable for codon extraction
codon = ''
# accumulator string variable for translation
protein = ''

##PROGRAMME
# for position in range from 0 to number before the last number dividible by 3
for position in range(0, len(s), 3):

    # codon becomes codon with concatenated nucleotide base at position location
    codon = codon + s[position]
    # codon becomes codon with concatenated nucleotide base at position + 1 location
    codon = codon + s[position+1]
    # codon becomes codon with concatenated nucleotide base at position + 2 location
    codon = codon + s[position+2]

    # if value from combinations at codon location equals 'Stop'
    if combinations[codon] == 'Stop':
        # protein becomes protein with concatenating "nothing" (instead of 'Stop')
        protein = protein + ''
    # otherwise
    else:
        # protein becomes protein with concatenated value from combinations at codon location
        protein = protein + combinations[codon]

    # clear codon variable
    codon = ''

# print translated sequence, the sequence of the protein
print(protein)