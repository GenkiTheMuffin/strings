import random
# 8 character starts with consonant, first character capitalised consonant-vowel-consonant
def consonant_vowel(l:int):
    vowels = "aeiouy"
    consonants = 'qwrtpsdfghjklzxcvbnm'
    final =''
    for i in range(0,l):
        if i%2==0:
            final+=random.choice(consonants)
        else:
            final+=random.choice(vowels)
    return final.capitalize()
print(consonant_vowel(8))