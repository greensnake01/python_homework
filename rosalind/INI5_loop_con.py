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
# create an accumulator variable
position = 0

##PROGRAMME
# for each line in text file
for line in file_in:
    # if position is odd
    if position % 2 == 1:
        # write the line into output file
        file_out.write(line)
        # add 1 to position
        position += 1
    # otherwise - does not need to be included, if + add 1 would be enough
    else:
        # add 1 to position 
        position += 1
        # continue with another iteration
        continue

# close writing into the output file
file_out.close()

# read output file
file_out = open(output_path, 'r')
# transform list into a string
result = ''.join(file_out.readlines())
# print results
print(result)