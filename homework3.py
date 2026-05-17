def get_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

while True:
    try:
        n = int(input("Введите натуральное число: "))
        if n > 0:
            break
        else:
            print("Ошибка! Натуральное число должно быть больше ноля.")
    except ValueError:
        print("Ошибка! Введенное значение не соответствует условию. Попробуйте еще раз.")
result = get_divisors(n)
print("Делители: " + " ".join([str(i) for i in result]))