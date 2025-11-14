##BONUS - Rosalind DNA, but use a loop

##VARIABLES
#s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
s = str(input('DNA string:'))
count = {}
##PROGRAMME
for nucleotide_base in list(s):
    if nucleotide_base in count:
        count[nucleotide_base] = count[nucleotide_base] + 1
        #count.update({nucleotide_base : count[nucleotide_base] + 1})
    else:
        count[nucleotide_base] = 1
        #count.update({nucleotide_base : 1})

count = dict(sorted(count.items())) # alphabetical sorting

print(list(count.values())[0], list(count.values())[1], list(count.values())[2], list(count.values())[3])