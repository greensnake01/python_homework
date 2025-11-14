#file_path = '../../rosalind_hamm.txt'
# file needs to be there where the files exist, same directory

# define function called file_reader with path/file argument
def file_reader(file_path):
    # create a list accumulator variable to save text into
    lines = []
    # assign file contents into file_in (better than assigning into a variable)
    with open(file_path, 'r') as file_in:
        # for each line in file_in lines
        for line in file_in.readlines():
            # insert cleaned line from '\n' and white space characters from the right into clean
            clean = line.rstrip()
            # append clean line into the list
            lines.append(clean)
            # return lines
            return lines

#file_reader(file_path)
#print(lines)