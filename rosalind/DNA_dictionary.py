##BONUS - Rosalind DNA, but use a dictionary format

# input
#AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
s = str(input('DNA string:'))
# s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

s_dic = {'A': s.count('A'),
         'C': s.count('C'),
         'G': s.count('G'),
         'T': s.count('T')
        }
         
print(s_dic)