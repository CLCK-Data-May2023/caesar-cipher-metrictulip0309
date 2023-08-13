#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:

        # The python string isalpha() method is used to check whether the string consists of alphabets.

        if char.isalpha():

            # Python ord() function takes string argument of a single Unicode character and return its integer Unicode code point value
            # Python chr() function takes integer argument and return the string representing a character at that code point
            # Python ord() and chr() are built-in functions. They are used to convert a character to an int and vice versa

            # Encrypt uppercase characters in plain text else Encrypt lowercase characters in plain text
            
            #The "% 26" ensures that the shift wraps around from 'Z' (or 'z') back to 'A' (or 'a') if the shift would otherwise result in a character outside the range of the alphabet.

            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += shifted_char


        else:
            ciphertext += char

    return ciphertext


# Decrypts the text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Ask the user for a number to shift in the positive or negative direction

while True:
    cipher_shift = int(input("Enter the Number of Shift:"))
    if cipher_shift == 0:
        print("Please Input a valid shift Number")
        continue
    else:
        break

# Ask User for a Phrase

plaintext = input("Enter Phrase:")    

# Encrypts the Text

encrypted_text = caesar_encrypt(plaintext, cipher_shift)
print("The encrypted sentence is: ", encrypted_text)

# Decrypts the Text

#decrypted_text = caesar_decrypt(encrypted_text, cipher_shift)
#print("Decrypted:", decrypted_text)

