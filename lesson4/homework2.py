lst = [0, 1, 7, 2, 4, 8]
sum_lst = 0
for index, elem in enumerate(lst):
    if index % 2 == 0:
        sum_lst += elem
if len(lst) > 0:
    result = sum_lst * lst[-1]
else:
    result = 0
print(result)