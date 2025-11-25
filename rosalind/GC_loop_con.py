##ABBREVIATIONS
# gc = guanine and cytosine
# nb = nucleotide base

##VARIABLES
# input DNA strings in FASTA format
path = str(input('insert a file path with DNA strings in FASTA format:'))
mode = 'r'

fasta = []
current_header = None
current_seq = []

# ChatGPT
with open(path, mode) as file:
    # looping through lines and removing "\n"
    for line in file:
        line = line.strip()

        if line.startswith(">"):

            # in the first iteration it is None, skipped; stores previous, if it is a header, it is added, if not sequence by sequence is stored until a new line appears that makes the whole sequence to be added and a new header to be stored
            
            if current_header is not None:
                fasta.append(current_header)
                fasta.append("".join(current_seq))

            # new record
            current_header = line
            current_seq = []

        # build sequence
        else:
            current_seq.append(line)

# adds the last sequence, because a sequence is added only when there is a new header
if current_header is not None:
    fasta.append(current_header)
    fasta.append("".join(current_seq))

#fasta = ['>Rosalind_6404', 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG', '>Rosalind_5959', 'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC', '>Rosalind_0808', 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT']
# accumulator variable for "GC" count first, after counting, for content in percentage
gc_content = {}
# accumulator variable for nucleotide base count
nb_total = 0

##PROGRAMME
# for each string (only) in a range from the first one to the last one
for string in range(1, len(fasta), 2):
    # create a dictionary key (id)  and value (0)
    gc_content[fasta[string-1][1:len(fasta[string-1])]] = 0
    # reset to 0
    nb_total = 0

    # for each nucleotide base in the current string
    for nb in fasta[string]:
        # add 1 to total count of nucleotide bases
        nb_total += 1

        # if nucleotide base is "G" or "C"
        if nb == 'G' or nb == 'C':
            # add 1 to the value of the corresponding key in the dictionary
            gc_content[fasta[string-1][1:len(fasta[string-1])]] += 1

    # calculate percentage ((gc count / total number of nucleotide bases) times 100)
    gc_percentage = (gc_content[fasta[string-1][1:len(fasta[string-1])]] / nb_total) * 100
    # replace gc count with the calculated percentage
    gc_content[fasta[string-1][1:len(fasta[string-1])]] = gc_percentage

# derive the highest percentage
gc_highest = max(gc_content.values())

# for each key and value in the dictionary (id : percentage)
for key, value in gc_content.items():
    # if value equals the highest percentage
    if value == gc_highest:
        # print key (id)
        print(key)
        # print value (percentage) with 6 decimal places (no rounding and keeping last 0)
        print(str(value)[:str(value).find('.')+7])