
def f(n):
    return abs(n - 10)

f = lambda n: abs(n - 10)



numbers = [2,4,6,7,34,3,6,3,56,8]


print( sorted(numbers, key = lambda n: abs(n - 10)) )


print( list(filter(lambda n: n % 8 == 0, numbers)) )

print( [n for n in numbers if n % 8 == 0] )    # similar to filter


print( list(map(lambda n: n * 100, numbers)) )

print( [n * 100 for n in numbers] )    # similar to map
