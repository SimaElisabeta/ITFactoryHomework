def numbers_count(lst):
    dict = {}
    for i in range(10):
        dict.setdefault(i, 0)
    for key in dict.keys():
        if key in lst:
            count = lst.count(key)
            dict[key] = count
    return dict

print(numbers_count([1, 3, 1, 5, 9, 7, 7, 5, 5]))



