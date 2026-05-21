from collections import Counter
    
def decode_caesar(text):
    # 1. Задаем (clean) - переменную с текстом переведенным в нижний регистр без пунктуации
    clean = "".join(char for char in text.lower() if char.isalpha())
    # 2. Определяем наиболее часто встречающуюся букву (most_frequent)
    counter = Counter(clean)
    most_frequent = counter.most_common(1)[0][0]
    # 4. Вычисляем сдвиг (shift)
    shift = ord(most_frequent)-ord("e")
    # 5. Декодируем текст
    decoded_text = []
    for c in text:
        if c.isupper():
            decoded_char = chr((ord(c) - 65 - shift) % 26 + 65)
        elif c.isalpha():
            decoded_char = chr((ord(c) - 97 - shift) % 26 + 97)
        else:
            decoded_char = c
        decoded_text.append(decoded_char)
    # 6. Возвращаем str
    return("".join(decoded_text))

text = "Olssv Dvysk aopz pz h zljyla tlzzhnl"
print(decode_caesar(text))