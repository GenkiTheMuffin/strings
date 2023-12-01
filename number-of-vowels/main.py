def number_of_vowels(s:str):
    count = 0
    vowels = "aeiouy"
    for i in range(0,len(s)):
        if s[i] in vowels:
            count+=1
    return (count)

print(number_of_vowels('Qomimowi'))