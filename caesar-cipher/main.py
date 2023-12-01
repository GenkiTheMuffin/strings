def caesar_cipher_encode(s: str, shift: int):
    encoded_string = ""
    for i in s:
        ordinal_value = ord(i)
        ordinal_value = (ordinal_value - 97 + shift) % 26 + 97
        encoded_character = chr(ordinal_value)
        encoded_string += encoded_character
    return encoded_string


def caesar_cipher_decode(s: str, shift: int):
    decoded_string = ""
    for i in s:
        ordinal_value = ord(i)
        ordinal_value = (ordinal_value - 97 - shift) % 26 + 97
        decoded_character = chr(ordinal_value)
        decoded_string += decoded_character
    return decoded_string


print(caesar_cipher_encode("ahoj", 29))
print(caesar_cipher_decode("dkrm", 29))
