
def bubble_sort(a):
    """Sort a list inplace."""
    while True:
        swapped = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if not swapped:
            break


def bubble_sorted(original_list):
    """Return a sorted list."""
    a = list(original_list)
    bubble_sort(a)
    return a


# ------------------------------------------------------------------------

numbers = [3, 9, 7, 1, 8]

sorted_numbers = bubble_sorted(numbers)

print(sorted_numbers)

import random
numbers = [random.randint(1, 10000) for _ in range(1000)]

from timeit import timeit
print( timeit(lambda: sorted(numbers), number = 1000) )
print( timeit(lambda: bubble_sorted(numbers), number = 1000) )
