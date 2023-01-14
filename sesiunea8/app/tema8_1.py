def get_positive_numbers(lst):
    new_list = []
    for nr in lst:
        if nr > 0:
            new_list.append(nr)
    return new_list


def add_nr_if_unique(nr, lst):
    if nr not in lst:
        lst.append(nr)
        return True
    return False


def get_max_nr(lst):
    return max(lst)
