# insert the DNA sequence (as a 't' string)
t = str(input('insert the DNA sequence: '))


# return the transrcibed DNA sequence (as a 'u' string, that has 'A', 'C', 'G' and 'U' nucleotide bases instead of 'A', 'C', 'G' and 'T')
u = t.replace('T', 'U')

# print the RNA sequence
print(u)