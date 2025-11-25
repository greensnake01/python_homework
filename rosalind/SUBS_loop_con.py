##ABBREVIATIONS
# nb = nucleotide base

##VARIABLES
# input DNA sequence as a string 
s = str(input('insert a DNA sequence:'))
#s = 'GATATATGCATATACTT'
# input susbtring of s, not longer than t, as a string
t = str(input('insert a sequence to be found within the DNA sequence; must be no longer than t:'))
#t = 'ATAT'
# accumulator variable which stores nucleotide bases
check = ''
# accumulator variable which stores real positions at which the string t was found
position = ''
# correction variable which acounts for the length of the string t and the real position where it was found accordingly
correction = len(t)-2

##PROGRAMME
# check if the length of the string t is not more than the length of the string s
if len(t) >= len(s):
    print('the string t is too long, please insert a shorter string')
    t = str(input('insert a sequence to be found within the DNA sequence; must be no longer than the string t:'))

# for each nucleotide base in the length of the string s
for nb in range(len(s)):
    # check becomes check with concatenated nucleotide base
    check = check + s[nb]
    #print(check)
    # if the string t is within the string check
    if t in check:
        # the string position becomes position with concatenated starting position and one space
        position = position + str(nb-correction) + ' '

    # if the length of the string check is equal to the length of the string t
    if len(check) == len(t):
        # the string check becomes check with 4 nbs without lastly added first one
        check = check[1:len(t)]

# if the length of the string position is 0
if len(position) == 0:
    # print message
    print('the string t is not present within the string s')
# otherwise:
else:
    # print message with positions
    print('the string t is located within the string s at the following starting positions:', position)