lst = [1, 0, 13, 0, 0, 0, 5]
for _ in range(lst.count(0)):
    lst.remove(0)
    lst.append(0)
print(lst)






