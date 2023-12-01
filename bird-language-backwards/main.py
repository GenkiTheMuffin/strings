import random


def translate(s: str):
    vowels = "aeiouy"
    final = ""
    for i in s:
        if i == " ":
            final += " "
        else:
            if i in vowels:
                final += i * 3
            else:
                final += i
                final += random.choice(vowels)
    return final


print(translate("hello"))
