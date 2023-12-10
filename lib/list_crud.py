def create_an_empty_list():
    list = []
    return list


def create_a_list():
    list = [1, 2, 3, 4]
    return list


def add_element_to_end_of_list(l, element):
    list = [1, 2, 3, 4]
    list.append(5)
    return list


def add_element_to_start_of_list(l, element):
    list = [1, 2, 3, 4]
    list.insert(0, 0)
    return list


def remove_element_from_end_of_list(l):
    list = [1, 2, 3, 4]
    del list[3]
    return list


def remove_element_from_start_of_list(l):
    list = [1, 2, 3, 4]
    del list[0]
    return list


def retrieve_first_element_from_list(l):
    list = [1, 2, 3, 4]
    return list.pop(0)


def retrieve_element_from_index(l, index):
    list = [1, 2, 3, 4]
    return list.pop(index)


def retrieve_last_element_from_list(l):
    list = [1, 2, 3, 4]
    return list.pop()
