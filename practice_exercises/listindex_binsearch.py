import time
from bisect import bisect_left

big_list = range(0, 1000000000)


def getIndex(input_list, search_term):
    for value, index in enumerate(input_list):
        if search_term == value:
            return index


tic = time.perf_counter()
search_index = getIndex(big_list, len(big_list) - 1)
toc = time.perf_counter()

print(f"Number of records searched: {len(big_list)}")
print(f"Found value at index {search_index} in {toc - tic} seconds.")

tic2 = time.perf_counter()
search_index2 = big_list.index(len(big_list) - 1)
toc2 = time.perf_counter()

print(f"Number of records searched: {len(big_list)}")
print(f"Found value at index {search_index2} in {toc2 - tic2} seconds.")


def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return pos if pos != hi and a[pos] == x else -1  # don't walk off the end


tic3 = time.perf_counter()
result = binary_search(big_list, len(big_list) - 1, lo=0, hi=None)
toc3 = time.perf_counter()

print(f"Found value at index {result} in {toc3 - tic3} seconds.")

