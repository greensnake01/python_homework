# insert the DNA sequnce (as a string)
s = str(input('insert the DNA sequence: '))

# make a (DNA) list with counts per each nucleotide base ("A", "C", "G", "T")
DNA = [s.count('A'), s.count('C'), s.count('G'), s.count('T')]

# print the counts (for nucleotide base - "A", "C", "G", "T")

'''
print('A occurs: ', DNA[0], 'times',
      'C occurs: ', DNA[1], 'times',
      'G occurs: ', DNA[2], 'times',
      'T occurs: ', DNA[3], 'times',)
'''
print(int(DNA[0]), int(DNA[1]), int(DNA[2]), int(DNA[3]))