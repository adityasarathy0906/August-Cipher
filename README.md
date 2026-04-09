AUGUST CIPHER


The August Cipher is a monoalphabetic substitution cipher derived from the Caesar Cipher.
In this method, each character in the plaintext is shifted by exactly one position forward in the alphabet.

Encryption:
Each letter is replaced by the next letter.
(A → B, B → C, …, Z → A)

Formula:
E(x) = (x + 1) mod 26

Decryption:
Each letter is shifted one position backward.
(B → A, C → B)

Formula:
D(x) = (x - 1) mod 26
 2. Custom Hash Function

A custom polynomial rolling hash function is implemented from scratch without using any external libraries.

Working Principle
Each character is converted into its ASCII value
A prime base (e.g., 31) is used
Each character contributes based on its position

Formula:

Hash = Σ ( ASCII(char) × p^i ) mod m

Where:

p = 31 (prime number)
m = 10^9 + 9 (large modulus to avoid overflow)
i = position of character


Justification
Simple and efficient to implement
No dependency on built-in libraries
Produces consistent and well-distributed hash values
Suitable for small-scale cryptographic demonstrations



Example 1
Plaintext: HELLO
Shift: 1
Ciphertext: IFMMP
Hash: (depends on implementation)
 Example 2
Plaintext: CRYPTO
Shift: 1
Ciphertext: DSZQUP
Hash: (depends on implementation)