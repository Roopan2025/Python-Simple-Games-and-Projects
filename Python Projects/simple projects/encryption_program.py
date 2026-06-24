import random
import string

chars =" " + string.ascii_letters + string.digits + string.punctuation
# print(chars)
chars = list(chars)
# print(f"chars : {chars}")
keys = chars.copy()
# print(keys)
random.shuffle(keys)
# print(f"keys  : {keys}")

# Encrypt

Plain_Text = input("Enter the message : ")
cipher_text = ""

for letter in Plain_Text:
    encrypted_letter = chars.index(letter)
    cipher_text += keys[encrypted_letter]

print(f"Encrypted message : {cipher_text}")

# Decrypt

cipher_text = input("Enter the encrypted message : ")
plain_text = ""

for letter in cipher_text:
    decrypted_letter = keys.index(letter)
    plain_text += chars[decrypted_letter]

print(f"Decrypted message : {plain_text}")
