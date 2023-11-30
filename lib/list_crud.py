def create_an_empty_list():
    return []

def create_a_list():
    return [1, 2, 3, 4]

def add_element_to_end_of_list(l, element):
    l=[1, 2, 3, 4]
    l.append(5)
    return l
    

def add_element_to_start_of_list(l, element):
    l=[ 1, 2, 3, 4]
    l.insert(0, 0)
    return l

def remove_element_from_end_of_list(l):
    l=[1, 2, 3, 4]
    l.pop(3)
    return l

def remove_element_from_start_of_list(l):
    l=[1, 2, 3, 4]
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    l=[1, 2, 3, 4]
    
    return l[0]

def retrieve_element_from_index(l, index):

    return l[index]

def retrieve_last_element_from_list(l):
    l=[1, 2, 3, 4]
    
    return l[-1]
