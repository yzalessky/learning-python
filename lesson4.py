#def greet(name):
#    return f"Привет, {name}!"

#print(greet("yzalessky"))
#print(greet("мир"))

def analyze(numbers):
    total = sum(numbers)
    average = round(total / len(numbers), 2)
    maximum = max(numbers)
    return f"Сумма: {total}, Среднее: {average}, Максимум: {maximum}"

numbers = [3, 7, 2, 9, 4, 11, 5]
result = analyze(numbers)
print(result)