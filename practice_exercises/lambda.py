my_list = [5, 4, 3]

print(list(map(lambda x: x ** 2, my_list)))

a = [(0, 2, 1), (4, 3, 3), (9, 9, -2), (10, -1, 11)]
a.sort(key=lambda x: x[2])
print(a)

