li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# example

amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])

# list slicing
amazon_cart = ['notebooks', 'toys', 'sunglasses', 'grapes']

print(amazon_cart[0::2])
print(amazon_cart[0::])

amazon_cart[0] = 'laptop'

print(amazon_cart)

# copying vs modifying
new_cart = amazon_cart  # points to same place in memeory
print(new_cart, amazon_cart)

new_cart[0] = 'poop'
print(new_cart, amazon_cart)

# matrix
matrix = [
    [1, 5, 1],
    [0, 1, 0],
    [1, 0, 1]
]
print('MATRIX: ' + str(matrix))
