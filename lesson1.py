name = "yzalessky"
age = 112
height = 1.8
is_learning = True

if 11 <= age % 100 <= 14:
    ageword = "лет"
elif age % 10 == 1:
    ageword = "год"
elif age % 10  < 5:
    ageword = "года"
else:
    ageword = "лет"


print(f"Меня зовут {name}")
print(f"Мне {age} {ageword}")
print(f"Рост: {height} м")
print(f"Учусь прямо сейчас: {is_learning}")