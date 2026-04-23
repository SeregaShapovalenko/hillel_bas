lst = []
if lst:
    elem_lst = lst.pop(-1)
    lst.insert(0, elem_lst)
    print(lst)
else:
    print([])