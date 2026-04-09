# hash_function.py

def custom_hash(text):
    hash_value = 0
    p = 31
    m = 10**9 + 9

    for i, char in enumerate(text):
        hash_value = (hash_value + (ord(char) * (p ** i))) % m

    return hash_value