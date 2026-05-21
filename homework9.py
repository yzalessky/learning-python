def password_check(password):
    """
    Проверяет пароль на соответствие заданным условиямю

    Args:
        password (str): входной текст для анализа

    Returns:
        dict: словарь с результатами проверки
    """
    # 1. Задаем переменные условий проверки и задаем по умолчанию как False
    strong = length = has_upper = has_lower = has_digit = has_special = False
    # 2. Проверяем длину, должно быть >= 8 символов
    if len(password) >= 8:
        length = True
    # 3. Проверяем наличие необходимых типов символов
    for i in password:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_digit = True
        elif i in "!@#$%^&":
            has_special = True
    # 4. Окончательный вердикт
    strong = all([has_upper, has_lower, has_digit, has_special])
    # 5. Возвращаем результат
    return {
        "strong": strong,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_special": has_special
    }



print(password_check("abc"))
print(password_check("MyPassword1!"))