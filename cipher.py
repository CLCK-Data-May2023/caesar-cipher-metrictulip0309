#!/usr/bin/env python
# coding: utf-8

# In[ ]:


abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

txt = input("Please enter a sentence: ").lower()
shift = 5

def is_abc(value, list):
    #Check if character is contained in list
    for x in list:
        if x == value:
            return True
        False 

def enc_text(text_string, shift):
    #encrypt each letter by specified shift amount
    encr_list=[]

    for plain_text in text_string:
        if is_abc(plain_text, alphabet):
            index=int(alphabet.index(plain_text))
            plain_text=alphabet[index + shift]
        encr_list.append(plain_text)
    encrypted_string = "".join(encr_list)
    print(f"The encrypted sentence is: {encrypted_string}")

enc_text(text_string=txt,shift=shift)

