while True:
    try:
        n = int(input("Введите натуральное число: "))
        if n > 0:
            break
        else:
            print("Ошибка! Натуральное число должно быть больше ноля.")
    except ValueError:
        print("Ошибка! Введенное значение не соответствует условию. Попробуйте еще раз.")

print(f"Вы ввели: {n}")
print("Делители: ", end="")

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")