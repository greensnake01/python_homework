# return the sum of all odd integers from a through b, inclusively.

##VARIABLES
# input integers (according to the following scheme: a < b < 10000)
a = int(input('insert integer value for "a": '))
b = int(input('insert integer value for "b": '))

# create a list of odd numbers
odd_list = [1, 3, 5, 7, 9]

# create a variable with value 0
odd_sum = 0

##LOOP
# for loop (from a through b, inclusively)
for num in range(a, b + 1):
    #print(num)
    num_list = list(str(num)) # transform a number into a list
    #print(num_list)
    last_num = int(num_list[len(num_list) - 1]) # get the last number
    #print(last_num)

    # if condition (if the last number is odd, add the number to the sum of previous odd numbers)
    if last_num in odd_list:
        #print('odd')
        odd_sum = odd_sum + num
    #else:
        #print('even')
        
# print results (of conditional calculation)
print(odd_sum)