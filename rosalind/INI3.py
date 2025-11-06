# slicing of a provided string based on determined positions to be sliced, not excluding, but comprising "b" and "d" indices.

# input string (to be sliced)
s = str(input('provide a string: '))

# input indices (to determine the extent of slicing) 
a = int(input('provide an index "a": '))
b = int(input('provide an index "b": '))
c = int(input('provide an index "c": '))
d = int(input('provide an index "d": '))

# print results (of slicing)
print(s[a:b+1], s[c:d+1])