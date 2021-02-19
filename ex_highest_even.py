def highest_even(li):
    """
    Takes in a list of numbers and returns the highest even number found
    """
    return max(filter(lambda x: x % 2 == 0, li))


print(highest_even([1, 2, 4, 3, 5, 6, 22, 63, 88]))
hey = (1, 2, 3)

fruits = {1, 2, 3}
more = [4, 5, 6]
fruits.update(more)
print(fruits)
