from august_cipher import encrypt, decrypt
from hash_function import custom_hash

# Updated plaintext
plaintext = "InformationTechnology"

cipher = encrypt(plaintext)
hash_val = custom_hash(cipher)
decrypted = decrypt(cipher)

print("Plaintext :", plaintext)
print("Ciphertext:", cipher)
print("Hash      :", hash_val)
print("Decrypted :", decrypted)