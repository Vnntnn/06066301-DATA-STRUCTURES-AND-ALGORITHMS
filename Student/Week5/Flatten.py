"""Flatten"""
from json import loads

def Flatten(lst):
    """main function"""
    num_lst = []
    for i in lst:
        if isinstance(i, list):
            num_lst.extend(Flatten(i))
        else:
            num_lst.append(i)
    num_lst.sort(reverse=True)
    return num_lst

print(Flatten(loads(input())))
