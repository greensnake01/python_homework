# return the hamming distance (number of mismatching nucleotide bases)

##VARIABLE
s = 'GAGCCTACTAACGGGAT'
#s = str(input('first DNA sequence:')
t = 'CATCGTAATGACGGCCT'
#t = str(input('second DNA sequence:')
d = 0

##PROGRAMME
# for particular position (index) in range of length of the string, do
for position in range(len(s)): # alternatively a while loop
    # if nucleotide base at the particular position in 's' string is not the same as the nucleotide base at the aprticular position in 't' string, then do
    if s[position] != t[position]:
        # add 1 to hamming distance
        d = d + 1 # alternatively +=
    #if not, then continue to with another iteration
    else:
        continue

# print results
print(d)