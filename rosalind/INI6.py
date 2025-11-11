# return the number of occurrences of each word in variable 's' (string), where words are separated by spaces; words are case-sensitive; lines in the output can be in any order

## VARIABLES
# input string and dictionary-based accumulator variable
#s = 'We tried list and we tried dicts also we tried Zen'
s = str(input('insert string:'))
word_count = {}

## PROGRAMME - extracting information
# for loop (from the first word from the list to the last one)
for word in s.split(): # hint: use (' ') for space or other delimiter character
    #if word exists in the dictionary, then add 1 to its value
    if word in word_count:
        word_count[word] = word_count[word] + 1
        # alternatively
        #word_count.update({word : word_count[word] + 1})
    #if not, then create new key-value pair with a value 1
    else:
        word_count[word] = 1
        # alternatively
        #word_count.update({word : 1})

#print(word_count) # debugging
#word_count = dict(sorted(word_count.items())) # alphabetically ordered dictionary

## VARIABLES
# integer-based accumulator variable
index = 0

## PROGRAMME - processing information
# for loop (from the first key-value pair from the dictionary to the last one)
for word in word_count: 
    # print words and their occurence number
    print(list(word_count)[index], word_count[word])
    # add one to the accumulator variable
    index = index + 1

# hint: alternative easy way
# for word, value in word_count.items():
#     print(word, value)