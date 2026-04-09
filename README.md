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


🔹 Prompt 1

Question: Can you explain the August Cipher? Is it related to the Caesar Cipher?
Answer:
Yes, the August Cipher is a simplified form of the Caesar Cipher where the shift value is fixed at 1. Each character in the plaintext is replaced by the next character in the alphabet.

🔹 Prompt 2

Question: Is the August Cipher polyalphabetic?
Answer:
No, it is a monoalphabetic substitution cipher because it applies a single fixed transformation (shift = 1) to all characters.

🔹 Prompt 3

Question: Why is a hash function used along with the cipher?
Answer:
The custom hash function is used to verify data integrity. While the cipher ensures confidentiality, the hash ensures that the message has not been altered during the encryption and decryption process.

🔹 Prompt 4

Question: Would the role of the hash function change for a polyalphabetic cipher?
Answer:
No, the purpose of the hash function remains the same. It is always used to verify whether the original and final outputs match.

🔹 Prompt 5

Question: How does the round-trip verification work?
Answer:
First, a hash is generated from the original plaintext using the custom polynomial hash function. After encryption and decryption, the resulting text is hashed again using the same function. The two hash values are then compared.

🔹 Prompt 6

Question: Is this flow correct?
Plaintext → Hash → Encrypt → Decrypt → Hash → Compare
Answer:
Yes, this is the correct flow. If both hash values are identical, it confirms that the encryption and decryption were successful without any data loss.

🔹 Prompt 7

Question: Why choose a polynomial rolling hash function?
Answer:
It is simple to implement from scratch, does not require any libraries, and efficiently generates consistent hash values using basic arithmetic operations.

🔹 Prompt 8

Question: Why is this hash function suitable for this project?
Answer:
The polynomial hash function provides a good balance between simplicity and effectiveness. It minimizes collisions for small inputs and is ideal for demonstrating integrity verification in academic projects.

🔹 Prompt 9

Question: How is it implemented?
Answer:
Each character is converted to its ASCII value and multiplied by a power of a prime number (e.g., 31). The results are summed and taken modulo a large number to produce the final hash value.


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
