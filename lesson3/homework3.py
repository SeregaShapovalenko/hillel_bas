lst = []
if len(lst) % 2 == 0:
    new_lst = []
    one_lst = lst[:len(lst) // 2]
    two_lst = lst[len(lst)// 2:]
    new_lst.append(one_lst)
    new_lst.append(two_lst)
    print(new_lst)
elif len(lst) % 2 != 0:
    new_lst = []
    one_lst = lst[:len(lst) // 2 + 1]
    two_lst = lst[len(lst) // 2 + 1:]
    new_lst.append(one_lst)
    new_lst.append(two_lst)
    print(new_lst)
else:
    new_lst = []
    new_lst.append(lst)
    new_lst.append(lst)
    print(new_lst)