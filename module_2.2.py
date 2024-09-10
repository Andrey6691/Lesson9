first=int(input('Введите первое число: '))
print(first)
second=int(input('Введите второе число: '))
print(second)
third=int(input('введите третье число: '))
print(third)
if first == second and first == third:
    print(3)
elif first != second and first != third:
    print(0)
else:
    print(2)
