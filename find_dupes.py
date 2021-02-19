def findDupesTheSmartWay(inputList):
    dupes_list = []
    for item in set(inputList):
        if inputList.count(item) > 1:
            dupes_list.append(item)
    return dupes_list


def findDupesTheStupidWay(input_list):
    dupes_list = []
    for item in input_list:
        if item not in dupes_list and input_list.count(item) > 1:
            dupes_list.append(item)
    return dupes_list


cool_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
print(dupes := findDupesTheSmartWay(cool_list))
print(dupes2 := findDupesTheStupidWay(cool_list))

duplicates = {x for x in cool_list if cool_list.count(x) > 1}
print(duplicates)
