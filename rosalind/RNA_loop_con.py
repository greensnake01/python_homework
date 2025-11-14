# sample dataset: GATGGAACTTGACTACGTAAATT
# sample output: GAUGGAACUUGACUACGUAAAUU

# take an RNA string formed from the alphabet containing 'A', 'C', 'G' and 'U'
# return the transrcibed DNA sequence (as a 'u' string, that has 'A', 'C', 'G' and 'U' nucleotide bases instead of 'A', 'C', 'G' and 'T')

##VARIABLES
# insert the DNA sequence (as a 't' string)
#t = 'GATGGAACTTGACTACGTAAATT'
t = str(input('insert the DNA sequence: '))
# accumulator varaible for a transcribed RNA string
u = ''

##PROGRAMME
# for each base
for base in t:
    # if base is 'A' or 'C' or 'G'
    if base == 'A' or base == 'C' or base == 'G':
        # u becomes u + base
        u = u + base
    # otherwise
    else:
        # u becomes u + 'U'
        u = u + 'U'

# print the RNA sequence
print(u)