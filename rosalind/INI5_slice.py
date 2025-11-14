# return a file containing all the even-numbered lines form the original file and assume 1-based numbering of lines

# input string: 'Bravely bold Sir Robin rode forth from Camelot\nYes, brave Sir Robin turned about\nHe was not afraid to die, O brave Sir Robin\nAnd gallantly he chickened out\nHe was not at all afraid to be killed in nasty ways\nBravely talking to his feet\nBrave, brave, brave, brave Sir Robin\nHe beat a very brave retreat'

# create an example file
# file_in = open('../../rosalind_INI4.txt', 'w')
# file_in.write('Bravely bold Sir Robin rode forth from Camelot\nYes, brave Sir Robin turned about\nHe was not afraid to die, O brave Sir Robin\nAnd gallantly he chickened out\nHe was not at all afraid to be killed in nasty ways\nBravely talking to his feet\nBrave, brave, brave, brave Sir Robin\nHe beat a very brave retreat')
# file_in.close()

##VARIABLES
# input file path
#input_path = str(input('insert file path for input text file:'))
input_path = '../../rosalind_INI5.txt'
# output file path
#output_path = str(input('insert file path for output text file:'))
output_path = '../../rosalind_INI5_output.txt'

# load text
file_in = open(input_path, 'r')
# create output file
file_out = open(output_path, 'w')

##PROGRAMME
# extract the number of lines
#line_count = len(file_in.readlines()) + 1
# reload input file
#file_in = open(input_path, 'r')
# extract even-numbered lines (odd numbers in slicing, because starts from 0)
output = file_in.readlines()[1::2] 

##NOTE
# if length is defined ([1:line_count:2]), after line_count, input file needs to be reloaded

# convert list of strings into a unified string
string = ''.join(output)
# write output into the output file
file_out.write(string)
# close file modifications
file_out.close()

# read output file
file_out = open(output_path, 'r')
# transform list into a string
result = ''.join(file_out.readlines())
# print results
print(result)