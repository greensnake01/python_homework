##EXERCISE
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

##EXAMPLE
# Input: 2, 2, 2
# Output: 0.78333



##VARIABLES
k = int(input('insert the number of homozygous individuals:'))
m = int(input('insert the number of heterozygous individuals:'))
n = int(input('insert the number of homozygous recessive individuals:'))

##PROGRAMME
def prob (k, m, n):
    '''Calculates probability of getting an offspring with a dominant allele. Any option can cross with any option
    k = integer of homozygous (AA)
    m = integer of heterozygous (Aa)
    n = integer of homozygous recessive (aa)
    N is calculated within the function and corresponds to the total number of inidivduals.
    '''
    N = k + m + n
    res = k/N + (m/(N*(N-1))) * ((4*k + 3*m + 2*n -3)/4) + (n/(N*(N-1)) * ((2*k + m)/2))
    return round(res, 5)

print(prob(k, m, n))