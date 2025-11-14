# sample dataset: AAAACCCGGT
# sample output: ACCGGGTTTT

# take a DNA string s of length at most 1000 bp
# return the reverse complement sc of s

##VARIABLES
# input DNA sequence
#s = 'AAAACCCGGT'
# insert DNA sequence
s = str(input('insert a DNA sequence:'))
# reverse the inserted DNA sequence
rs = s[::-1]
# transform into lower case letters
rs = rs.lower()

# in one go
#s = str(input('insert a DNA sequence:'))[::-1].lower()

##PROGRAMME
# raplace each lowe case letter with an upper case letter of a complementary nucleobase
sc = rs.replace('a', 'T') # firstly use rs and insert result into sc
sc = sc.replace('t', 'A') # from this point onward work with sc only
sc = sc.replace('c', 'G')
sc = sc.replace('g', 'C')

# print complementary DNA string
print()
print('the complementary DNA string, sc:', sc)