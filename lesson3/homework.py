number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))
action = input("Какое действие выполнить (+, -, *, /): ")
if action == "+":
    print(number_one + number_two)
elif action == "-":
    print(number_one - number_two)
elif action == "*":
    print(number_one * number_two)
elif action == "/":
    if number_two:
        print(number_one / number_two)
    else:
        print("На ноль делить нельзя!")
else:
    print("Выбрано не правильное действие!")
