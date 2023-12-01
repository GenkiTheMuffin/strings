def translate(s: str):
    length = len(s)
    i = 0
    vowels = "aeiouy"
    final = ""
    while i < length:
        if s[i] != " ":
            if s[i] in vowels:
                final += s[i]
                i += 3
            else:
                final += s[i]
                i += 2
        else:
            final += s[i]
            i += 1
    return final


print(translate("hieeelalooo"))
