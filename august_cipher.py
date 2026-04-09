def encrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 1
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result


def decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 1
            if char.islower():
                result += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result