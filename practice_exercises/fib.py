def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        c = a
        a = b
        b = c + b


for x in fib(21):
    print(x)


def findNumsDivisibleBySevenAndNotFiveInRange(start, stop):
    li = []
    for i in range(start, stop + 1):
        if i % 7 == 0 and i % 5 != 0:
            li.append(str(i))

    return li


nums = findNumsDivisibleBySevenAndNotFiveInRange(2000, 3200)
print(','.join(nums))
