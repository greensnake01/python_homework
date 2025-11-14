# sample dataset: AAAACCCGGT
# sample output: ACCGGGTTTT

# take a DNA string s of length at most 1000 bp
# return the reverse complement sc of s

##VARIABLES
# input DNA sequence
#s = 'AAAACCCGGT'
# insert DNA sequence
s = str(input('insert a DNA sequence:'))
# create accumulator variable for reverse complement of a DNA string
sc = ''

##PROGRAMME
# for each base in reversed DNA sequence string
for base in s[::-1]:
    # if base is 'A'
    if base == 'A':
        # sc becomes sc + 'T'
        sc = sc + 'T'
    # or if base is 'T'
    elif base == 'T':
        # sc becomes sc + 'A'
        sc = sc + 'A'
    # or if base is 'C'
    elif base == 'C':
        # sc becomes sc + 'G'
        sc = sc + 'G'
    # otherwise
    else:
        # sc becomes sc + 'C'
        sc = sc + 'C'

# print complementary DNA string
print()
print('the complementary DNA string, sc:', sc)