#!/usr/bin/env python
# coding: utf-8

# In[ ]:

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

txt = input("Please enter a sentence: ").lower()
shift = 5

def is_alphabet(value, list):
    #loop through list to see if character is contained
    for i in list:
        if i == value:
            return True
        False 

def encrypt_text(text_string, shift):
    #encrypt alphabetical value by shift amount
    encrypted_list=[]

    for plain_text in text_string:
        if is_alphabet(plain_text, alphabet):
            index=int(alphabet.index(plain_text))
            plain_text=alphabet[index + shift]
        encrypted_list.append(plain_text)
    encrypted_string = "".join(encrypted_list)
    print(f"The encrypted sentence is: {encrypted_string}")

encrypt_text(text_string=txt,shift=shift)
