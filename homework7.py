def caesar_cipher (text, shift):
    base_text = list(text)
    encrypted_text = []
    for i in base_text:
        if i.isupper():
            e = chr((ord(i) - 65 + shift) % 26 + 65)
        elif i.isalpha():
            e = chr((ord(i) - 97 + shift) % 26 + 97)
        else:
            e = i
        encrypted_text.append(e)
    return("".join(encrypted_text))


print(caesar_cipher("Hello World this is a secret message", 7))
