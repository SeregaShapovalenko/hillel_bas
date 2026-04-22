numbers = int(input("Enter a number: "))
one_number = numbers // 10000
two_number = numbers // 1000 % 10
thri_number = numbers // 100 % 10
four_number = numbers // 10 % 10
five_number = numbers % 10
print(five_number *  10000 + four_number * 1000 + thri_number * 100 + two_number * 10 + one_number)

